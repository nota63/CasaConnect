from django.urls import path
from .views import *

urlpatterns = [
    path('help_view/', help_view, name='help_view'),
    path('helped/', help_accessed, name='helped')

]
