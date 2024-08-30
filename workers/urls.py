from django.urls import path
from .views import *

urlpatterns = [

    path("workers/", fetch_workers, name='workers'),
    path("worker_detail/<int:pk>/", worker_detail, name='worker_detail'),
    path("purchase/<int:pk>/", purchase, name='purchase'),
    path("track_order/", track_order, name='track_order'),
    path("change_address/<int:pk>/", change_address, name='change_address'),
    path("cancel/<int:pk>/", cancel, name='cancel'),
    path("completed/", completed, name='completed'),
    path("complaint/<int:pk>/", complaint, name='complaint'),
    path("complaint_done/<int:pk>/", complaint_success, name='complaint_done'),
    path("feed/<int:pk>/", feed, name='feed'),
    path("feedback_success/", feedback_success, name='feedback_success'),
    path("purchase_done/<int:pk>/", purchase_done, name='purchase_done'),
    path('premium/', premium, name='premium'),
    path("payment_page/", payment_page, name='payment_page'),
    path("payment_form/", payment_form, name='payment_form'),
    path("payment_status/", payment_status, name='payment_status'),
    path("about_premium/", about_premium, name='about_premium'),
    path("join_worker/", join_worker, name='join_worker'),
    path("jobs/", jobs, name='jobs'),
    path("apply_job/<int:pk>/", apply_job, name='apply_job'),
    path("applied_done/<int:pk>/", applied_done, name='applied_done'),
    path("contact/", contact, name='contact'),
    path("done_contact/", done_contact, name='done_contact'),
    path("discounts/", discounts, name='discounts')

]
