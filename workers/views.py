from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import Workers, Role, Purchase, Cancel, Complaint, Feedback, Payments, Jobs, JobApplications, Contact, \
    Discounts
from .forms import PurchaseForm, CancelForm, ComplaintForm, FeedbackForm, PaymentsForm, JobsApplicationsForm, \
    ContactForm
from django.contrib import messages
from django.http import JsonResponse
from plyer import notification
import time


# Create your views here.
# FETCH WORKERS

@login_required
def fetch_workers(request):
    # Fetch all workers initially
    data = Workers.objects.all()

    # Get the profession filter from query parameters
    profession_name = request.GET.get('profession')

    if profession_name:
        try:
            # Try to get the Role instance that matches the provided profession
            profession = get_object_or_404(Role, role=profession_name)
            data = Workers.objects.filter(role=profession)
        except Exception as e:
            return JsonResponse({'message': str(e)}, status=400)
    # Render the template with the filtered data
    return render(request, 'workers/fetch_workers.html', {'data': data})


# WORKER DETAILS
@login_required
def worker_detail(request, pk):
    worker = get_object_or_404(Workers, pk=pk)
    return render(request, 'workers/worker_detail.html', {'worker': worker})


# PURCHASE ORDER
@login_required
def purchase(request, pk):
    work = get_object_or_404(Workers, pk=pk)
    if request.method == 'POST':
        form = PurchaseForm(request.POST, request.FILES)
        if form.is_valid():
            purchase = form.save(commit=False)
            purchase.user = request.user
            purchase.work = work
            purchase.save()
            time.sleep(3)
            messages.success(request, f'your work has been scheduled for {purchase.work}')
            notification.notify(
                title='CasaConnect',
                message=f'Congratulations {purchase.user} your work has been scheduled for {purchase.work}\n please wait for sometime our worker will reach you shortly\n Thank you Have a great day',
                timeout=10
            )
            return redirect('purchase_done', pk=work.pk)
    else:
        form = PurchaseForm()
    return render(request, 'workers/purchase.html', {'form': form})


@login_required
def purchase_done(request, pk):
    order = get_object_or_404(Workers, pk=pk)
    return render(request, 'workers/purchase_done.html', {'purchase': order})


# TRACK ORDER
@login_required
def track_order(request):
    data = Purchase.objects.filter(user=request.user)
    return render(request, 'workers/track_order.html', {'data': data})


# CHANGE/UPDATE ADDRESS
@login_required
def change_address(request, pk):
    address = get_object_or_404(Purchase, pk=pk, user=request.user)
    if request.method == 'POST':
        form = PurchaseForm(request.POST, instance=address)
        if form.is_valid():
            try:
                form.save()
            except Exception as e:
                return JsonResponse({'message': str(e)}, status=400)
            time.sleep(2)
            notification.notify(
                title='CasaConnect',
                message=f'Address updated for {address.work} successfully',
                timeout=10
            )
            return redirect('track_order')
    else:
        form = PurchaseForm(instance=address)
    return render(request, 'workers/change_address.html', {'form': form, 'address': address})


@login_required
def cancel(request, pk):
    # Retrieve the purchase instance that the user wants to cancel
    purchase = get_object_or_404(Purchase, pk=pk, user=request.user)

    if request.method == 'POST':
        form = CancelForm(request.POST)
        if form.is_valid():
            # Save the cancellation details before deleting the purchase
            cancel = form.save(commit=False)
            cancel.user = request.user
            cancel.work = purchase.work  # Assign the work related to this purchase
            cancel.save()

            # Notify the user about the successful cancellation
            messages.success(request, f'Cancellation request for "{cancel.work}" submitted. Please wait for '
                                      f'CasaConnect to respond.')

            # Optional: Add a delay or notification (if relevant)
            time.sleep(3)
            notification.notify(
                title='CasaConnect',
                message=f'Your cancellation request for {cancel.work} accepted\n and your work {purchase.work} has been cancelled successfully',
                timeout=10

            )
            # Delete the purchase instance after saving the cancellation
            purchase.delete()

            # Redirect the user to the order tracking page after the deletion
            return redirect('track_order')
    else:
        form = CancelForm()

    return render(request, 'workers/cancel.html', {'form': form, 'cancel': purchase})


@login_required
def completed(request):
    data = Purchase.objects.filter(user=request.user, status='completed')
    return render(request, 'workers/completed.html', {'data': data})


@login_required
def complaint(request, pk):
    # Fetch the specific Purchase instance (work in Complaint model), ensuring it belongs to the logged-in user
    purchase = get_object_or_404(Purchase, pk=pk, user=request.user)

    if request.method == 'POST':
        form = ComplaintForm(request.POST, request.FILES)
        if form.is_valid():
            # Create a new complaint but don't save to the database yet
            new_complaint = form.save(commit=False)
            # Assign the logged-in user to the complaint
            new_complaint.user = request.user
            # Link the complaint to the specific Purchase instance (work)
            new_complaint.work = purchase
            # Save the complaint to the database
            new_complaint.save()
            # Success message for the user
            messages.success(request, f'Complaint submitted successfully for {new_complaint.work}')
            # Redirect to a relevant page (this could be a page listing complaints, etc.)
            return redirect('complaint_done', pk=new_complaint.pk)
    else:
        form = ComplaintForm()

    return render(request, 'workers/comp.html', {'form': form})


@login_required
def complaint_success(request, pk):
    complaint = get_object_or_404(Complaint, pk=pk, user=request.user)
    return render(request, 'workers/complaint_done.html', {'complaint': complaint})


# feedback section
@login_required
def feed(request, pk):
    purchase = get_object_or_404(Purchase, pk=pk, user=request.user)
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            try:
                feedback = form.save(commit=False)
                feedback.user = request.user
                feedback.work = purchase
                feedback.save()
            except Exception as e:
                return JsonResponse({'message': str(e)}, status=400)

            return redirect('feedback_success')
    else:
        form = FeedbackForm()
    return render(request, 'workers/feedback.html', {'form': form})


# feedback success
@login_required
def feedback_success(request):
    return render(request, 'workers/f_success.html')


@login_required
def premium(request):
    return render(request, 'workers/premium.html')


@login_required
def payment_page(request):
    return render(request, 'workers/payment_page.html')


@login_required
def payment_form(request):
    if request.method == 'POST':
        form = PaymentsForm(request.POST, request.FILES)
        if form.is_valid():
            payment = form.save(commit=False)
            payment.user = request.user
            payment.save()
            time.sleep(3)
            messages.success(request, f'payment details submitted successfully\n wait for our reply')
            return redirect('payment_status')
    else:
        form = PaymentsForm()
    return render(request, 'workers/payment_form.html', {'form': form})


@login_required
def payment_status(request):
    return render(request, 'workers/payment_status.html')


@login_required
def about_premium(request):
    return render(request, 'workers/about_premium.html')


@login_required
def join_worker(request):
    return render(request, 'workers/join_worker.html')


@login_required
def jobs(request):
    data = Jobs.objects.all()
    return render(request, 'workers/jobs.html', {'data': data})


@login_required
def apply_job(request, pk):
    job = get_object_or_404(Jobs, pk=pk)
    if request.method == 'POST':
        form = JobsApplicationsForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                apply = form.save(commit=False)
                apply.user = request.user
                apply.job = job
                apply.save()
                time.sleep(3)
            except Exception as e:
                return JsonResponse({'message': str(e)}, status=400)
            messages.success(request, 'applied success!')
            return redirect('applied_done', pk=apply.pk)
    else:
        form = JobsApplicationsForm()
    return render(request, 'workers/apply_job.html', {'form': form})


@login_required
def applied_done(request, pk):
    data = get_object_or_404(JobApplications, pk=pk, user=request.user)
    return render(request, 'workers/applied_done.html', {'data': data})


# contact data
@login_required
def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            try:
                contact = form.save(commit=False)
                contact.user = request.user
                contact.save()
            except Exception as e:
                return JsonResponse(
                    {'msg': str(e)},
                    status=400
                )
            return redirect('done_contact')
    else:
        form = ContactForm()
    return render(request, 'workers/contact.html', {'form': form})


# success
@login_required
def done_contact(request):
    return render(request, 'workers/done_contact.html')


@login_required
def discounts(request):
    discount = Discounts.objects.all()
    return render(request, 'workers/discounts.html', {'discount': discount})


