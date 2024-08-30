import base64

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import HomeProject, Call
from .forms import HomeProjectForm, CallForm, ImageUploadForm
from django.contrib import messages
from django.contrib import messages
from plyer import notification
import time
from django.http import JsonResponse, HttpResponse
from PIL import ImageGrab
import subprocess
import os
import platform
from io import BytesIO
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Image
from django.conf import settings
import requests
from reportlab.lib import colors
from reportlab.lib.units import inch
from io import BytesIO
from PIL import Image, ImageDraw, ImageFont
import segno
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
import http.client
import json


# Create your views here.

@login_required
def homepage(request):
    return render(request, 'projects/homepage.html')


@login_required
def start_build(request):
    if request.method == 'POST':
        form = HomeProjectForm(request.POST, request.FILES)
        if form.is_valid():
            home = form.save(commit=False)
            home.user = request.user
            home.save()
            messages.success(request, 'Project building process started!')
            return redirect('build_done', pk=home.pk)
    else:
        form = HomeProjectForm()

    return render(request, 'projects/start_build.html', {'form': form})


@login_required
def build_done(request, pk):
    data = get_object_or_404(HomeProject, pk=pk, user=request.user)
    return render(request, 'projects/build_done.html', {'data': data})


@login_required
def view_projects(request):
    data = HomeProject.objects.filter(user=request.user)
    return render(request, 'projects/view_build.html', {'data': data})


@login_required
def project_detail(request, pk):
    project = get_object_or_404(HomeProject, pk=pk, user=request.user)
    return render(request, 'projects/project_detail.html', {'project': project})


@login_required
def cancel_project(request, pk):
    project = get_object_or_404(HomeProject, pk=pk, user=request.user)
    project.delete()
    notification.notify(
        title='CasaConnect Property deals',
        message=f'{project.user}! your project {project.project_name} has been cancelled sucessfully\n thank you for '
                f'doing business with us.',
        timeout=5

    )
    return redirect('view_build')


@login_required
def edit_project(request, pk):
    project = get_object_or_404(HomeProject, pk=pk, user=request.user)
    if request.method == 'POST':
        form = HomeProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            try:
                form.save()
                t = time.localtime()
                actual_time = time.strftime("%d-%m-%y %H:%M:%S", t)
                notification.notify(
                    title='CasaConnect Property deals',
                    message=f'Your project {project.project_name} successfully updated on {actual_time} !'
                )
                time.sleep(2)
            except Exception as e:
                return JsonResponse({'alert': str(e)}, status=400)
            return redirect('project_detail', pk=project.pk)
    else:
        capture_and_open_screenshot()
        notification.notify(
            title='CasaConnect Property deals',
            message='Previous version of your project captured!',
            timeout=7
        )
        form = HomeProjectForm(instance=project)
    return render(request, 'projects/edit_project.html', {'form': form, 'project': project})


def capture_and_open_screenshot():
    screenshot = ImageGrab.grab()

    # Define the file path
    file_path = "screenshot.png"

    # Save the screenshot
    screenshot.save(file_path)

    # Function to open the image with the default viewer
    def open_image(file_path):
        if platform.system() == "Darwin":  # macOS
            subprocess.call(('open', file_path))
        elif platform.system() == "Windows":  # Windows
            os.startfile(file_path)
        else:  # Linux
            subprocess.call(('xdg-open', file_path))

    # Open the image
    open_image(file_path)


def generate_report(request, pk):
    # Fetch the project object for the given primary key
    project = get_object_or_404(HomeProject, pk=pk, user=request.user)

    # Create a BytesIO buffer to hold the PDF data
    buffer = BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=letter)
    story = []

    # Define the company logo URL
    logo_url = 'https://th.bing.com/th/id/OIP.kryWQ3i3FVjyJOUd0wxIxQHaHa?rs=1&pid=ImgDetMain'  # Replace with your logo URL

    # Fetch the logo image from the URL
    response = requests.get(logo_url)
    if response.status_code == 200:
        logo_data = BytesIO(response.content)
        logo = Image(logo_data, width=200, height=100)
        story.append(logo)
    else:
        print("Failed to fetch the logo image from the URL.")

    # Define styles
    styles = getSampleStyleSheet()
    title_style = styles['Title']
    normal_style = styles['Normal']
    normal_style.fontName = 'Helvetica'
    normal_style.fontSize = 12
    normal_style.leading = 14

    # Add title
    title = Paragraph(f"Project Report: {project.project_name}", title_style)
    story.append(title)

    # Add project details
    details = [
        f"Customer Name: {project.customer_name}",
        f"Contact Phone: {project.contact_phone}",
        f"Contact Email: {project.contact_email}",
        f"Location: {project.location}",
        f"Budget: ${project.budget}",
        f"Company Budget: ${project.company_budget}",
        f"Status: {project.status}",
        f"Style: {project.style}",
        f"Size: {project.size_sqft} sqft",
        f"Bedrooms: {project.num_bedrooms}",
        f"Bathrooms: {project.num_bathrooms}",
        f"Start Date: {project.start_date.strftime('%d-%m-%Y')}",
        f"Completion Date: {project.completion_date.strftime('%d-%m-%Y')}",
        f"Date of Registration: {project.date_of_registration.strftime('%d-%m-%Y %H:%M:%S')}"
    ]

    for detail in details:
        story.append(Paragraph(detail, normal_style))

    # Add sample design image if available
    if project.sample_design:
        design_image = Image(project.sample_design.path, width=400, height=300)
        story.append(design_image)

    # Build the PDF
    doc.build(story)

    # Get the PDF data from the buffer
    buffer.seek(0)
    pdf = buffer.getvalue()
    buffer.close()

    # Create the HTTP response with the PDF data
    response = HttpResponse(pdf, content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="project_report_{pk}.pdf"'
    return response


# call
@login_required
def make_call(request, pk):
    # Get the HomeProject instance for the given pk and user
    project = get_object_or_404(HomeProject, pk=pk, user=request.user)

    if request.method == 'POST':
        form = CallForm(request.POST)
        if form.is_valid():
            try:
                # Create the Call instance without saving it yet
                call_instance = form.save(commit=False)
                # Assign the current user
                call_instance.user = request.user
                # Assign the HomeProject instance to the project_name field
                call_instance.project_name = project
                # Assign the HomeProject instance to the contact field
                call_instance.contact_phone = project  # Assign the HomeProject instance directly
                # Save the Call instance to the database
                call_instance.save()
            except Exception as e:
                return JsonResponse({'alert': str(e)}, status=400)
            return redirect('call_done', pk=project.pk)
    else:
        form = CallForm()

    return render(request, 'projects/make_call.html', {'form': form})


@login_required
def call_done(request, pk):
    data = get_object_or_404(HomeProject, pk=pk, user=request.user)
    return render(request, 'projects/call_done.html', {'data': data})


# view to generate qrcode
def generate_qr_code_view(request):
    qr_code_base64 = None

    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            # Save the uploaded image to default storage
            uploaded_image = request.FILES['image']
            file_name = default_storage.save(uploaded_image.name, ContentFile(uploaded_image.read()))
            image_url = default_storage.url(file_name)  # URL to access the image

            # Ensure the URL is fully qualified
            full_image_url = request.build_absolute_uri(image_url)

            # Generate a QR code from the image URL using segno
            qr = segno.make(full_image_url)

            # Save QR code to BytesIO
            qr_buffer = BytesIO()
            qr.save(qr_buffer, kind='png', scale=5)
            qr_buffer.seek(0)

            # Convert QR code to base64
            qr_base64 = base64.b64encode(qr_buffer.getvalue()).decode('utf-8')
            qr_code_base64 = f"data:image/png;base64,{qr_base64}"

    else:
        form = ImageUploadForm()
        capture_and_open_screenshot()
    return render(request, 'projects/upload_image.html', {'form': form, 'qr_code_base64': qr_code_base64})


@login_required
def vehicle_info(request):
    vehicle_data = None  # Default to None for initial load

    if request.method == 'POST':
        reg_no = request.POST.get('reg_no')

        conn = http.client.HTTPSConnection("rto-vehicle-information-verification-india.p.rapidapi.com")

        payload = json.dumps({
            "reg_no": reg_no,
            "consent": "Y",
            "consent_text": "I hereby declare my consent agreement for fetching my information via AITAN Labs API"
        })

        headers = {
            'x-rapidapi-key': "653ff8c2e8msh563d7a2f5a68f5cp1e03dfjsnb39859268b8f",
            'x-rapidapi-host': "rto-vehicle-information-verification-india.p.rapidapi.com",
            'Content-Type': "application/json"
        }

        conn.request("POST", "/api/v1/rc/vehicleinfo", payload, headers)
        res = conn.getresponse()
        data = res.read()

        try:
            vehicle_data = json.loads(data.decode("utf-8"))
        except json.JSONDecodeError:
            return HttpResponse("Error decoding the response data from the API.")

        # Check if the API response indicates a successful request
        if vehicle_data.get('status') != 'success':
            return HttpResponse(vehicle_data.get('message', 'An error occurred while fetching vehicle information.'))

    return render(request, 'projects/vehicle_info.html', {'vehicle_data': vehicle_data})


