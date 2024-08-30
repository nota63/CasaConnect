"""
URL configuration for auth project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path,include
from auth import views
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",views.home,name='home'),
    path("signup/",include('accounts.urls')),
    path("workers/",include('workers.urls')),
    path('homepage/', include('homeproject.urls')),
    path('terms/', views.terms_of_service, name='terms'),
    path('privacy/',views.privacy_policy, name='privacy'),
    path('about_us/', views.about_us, name='about_us'),
    path("help_view/",include('help_view.urls'))
    # path("api/",views.api,name='api')
]

# Serve media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)