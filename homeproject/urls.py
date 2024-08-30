from django.urls import path
from .views import *

urlpatterns = [
    path('homepage/', homepage, name='homepage'),
    path('start_build/', start_build, name='start_build'),
    path('build_done/<int:pk>/', build_done, name='build_done'),
    path('view_build/', view_projects, name='view_build'),
    path('project_detail/<int:pk>/', project_detail , name='project_detail'),
    path('cancel_project/<int:pk>/', cancel_project, name='cancel_project'),
    path('edit_project/<int:pk>/', edit_project , name='edit_project'),
    path('generate_report/<int:pk>/', generate_report , name='generate_report'),
    path('make_call/<int:pk>/', make_call, name='make_call'),
    path('call_done/<int:pk>/', call_done, name='call_done'),
    path("capture/", generate_qr_code_view, name='capture'),
    path('vehicle_info/', vehicle_info , name='vehicle_info')

]
