from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class HomeProject(models.Model):
    # Customer Information
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    customer_name = models.CharField(max_length=255)
    contact_phone = models.CharField(max_length=15)
    contact_email = models.EmailField()

    # Project Details
    project_name = models.CharField(max_length=255)
    project_description = models.TextField(blank=True, null=True)
    location = models.CharField(max_length=255)
    budget = models.DecimalField(max_digits=12, decimal_places=2)
    company_budget = models.IntegerField(null=True)
    status = models.CharField(max_length=100, choices=(
        ('pending', 'pending'), ('in-review', 'in-review'), ('accepted', 'accepted'), ('declined', 'declined'),
        ('negotiable', 'negotiable')), default='pending', null=True)
    # Design Preferences
    style = models.CharField(max_length=50)
    size_sqft = models.PositiveIntegerField()
    num_bedrooms = models.PositiveIntegerField()
    num_bathrooms = models.PositiveIntegerField()
    sample_design = models.ImageField(upload_to='projects/', null=True)
    # Timeline
    start_date = models.DateField()
    completion_date = models.DateField()
    date_of_registration = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.project_name} by {self.customer_name}"

    # class Meta:
    #     verbose_name = "Home Project"
    #     verbose_name_plural = "Home Projects"


# create a model to request a call

class Call(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    project_name = models.ForeignKey(HomeProject, on_delete=models.CASCADE)
    time = models.CharField(max_length=100, choices=(
        ('next 30 minutes', 'next 30 minutes'), ('after an hour', 'after an hour'), ('tomorrow', 'tomorrow'),
        ('after 2 hours', 'after 2 hours')), blank=True)
    or_specified_time = models.CharField(max_length=100, blank=True)
    contact_phone = models.ForeignKey(HomeProject, on_delete=models.CASCADE, null=True, related_name='contact_calls')
    requested_call = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return f"call request from {self.user} for {self.project_name}"
