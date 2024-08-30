from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
import requests
from django.http import HttpResponse, JsonResponse



# Create your views here.

# def api(request):
#     URL = 'http://127.0.0.1:8000/all_students/'
#
#     try:
#         r = requests.get(url=URL)
#         r.raise_for_status()  # Raises an error for bad HTTP status codes
#         data = r.json()  # Convert the response to JSON
#     except requests.exceptions.RequestException as e:
#         return JsonResponse({'error': str(e)}, status=500)
#
#     return JsonResponse(data, safe=False)

def home(request):
    login_data = request.session.pop('login_data', None)
    return render(request, 'home.html', {'login_data': login_data})


def terms_of_service(request):
    return render(request, 'term.html')


def privacy_policy(request):
    return render(request, 'privacy.html')


def about_us(request):
    return render(request, 'about_us.html')

