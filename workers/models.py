from django.contrib.auth.models import User
from django.db import models
from tinymce.models import HTMLField


# Create your models here.


# CREATE ROLE MODEL
class Role(models.Model):
    ROLE_CHOICES = [
        ('Electrician', 'Electrician'),
        ('Plumber', 'Plumber'),
        ('Carpenter', 'Carpenter'),
        ('Handyman', 'Handyman'),
        ('HVAC Technician', 'HVAC Technician'),
        ('Painter', 'Painter'),
        ('Appliance Repair Technician', 'Appliance Repair Technician'),
        ('General Contractor', 'General Contractor'),
        ('Gardener', 'Gardener'),
        ('Landscaper', 'Landscaper'),
        ('Tree Surgeon', 'Tree Surgeon'),
        ('Pest Control Specialist', 'Pest Control Specialist'),
        ('Pool Maintenance Technician', 'Pool Maintenance Technician'),
        ('Window Cleaner', 'Window Cleaner'),
        ('Pressure Washer Technician', 'Pressure Washer Technician'),
        ('House Cleaner', 'House Cleaner'),
        ('Carpet Cleaner', 'Carpet Cleaner'),
        ('Chimney Sweep', 'Chimney Sweep'),
        ('Gutter Cleaner', 'Gutter Cleaner'),
        ('Home Security Installer', 'Home Security Installer'),
        ('Locksmith', 'Locksmith'),
        ('Fire Safety Technician', 'Fire Safety Technician'),
        ('Interior Designer', 'Interior Designer'),
        ('Professional Organizer', 'Professional Organizer'),
        ('Home Stager', 'Home Stager'),
        ('Smart Home Installer', 'Smart Home Installer'),
        ('Roofer', 'Roofer'),
        ('Tiler', 'Tiler'),
        ('Flooring Installer', 'Flooring Installer'),
        ('Drywall Installer', 'Drywall Installer'),
        ('Plasterer', 'Plasterer'),
        ('Mason', 'Mason'),
        ('Welder', 'Welder'),
        ('Fence Installer', 'Fence Installer'),
        ('Solar Panel Installer', 'Solar Panel Installer'),
        ('Garage Door Technician', 'Garage Door Technician'),
        ('Customer Service Representative', 'Customer Service Representative'),
        ('Scheduler', 'Scheduler'),
        ('Quality Control Inspector', 'Quality Control Inspector'),
        ('Office Manager', 'Office Manager'),
    ]

    role = models.CharField(max_length=100, choices=ROLE_CHOICES)

    def __str__(self):
        return self.role


# CREATE WORKER MODEL
class Workers(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    profile_pic = models.ImageField(upload_to='workers/')
    name = models.CharField(max_length=200)
    discount=models.CharField(max_length=200, null=True, blank=True)
    price = models.CharField(max_length=200)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    age = models.CharField(max_length=200, null=True, blank=True)
    member_since = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} - {self.role.role}"


#     create purchase model

class Purchase(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # role = models.ForeignKey(Role, on_delete=models.CASCADE)
    work = models.ForeignKey(Workers, on_delete=models.CASCADE)
    address = models.CharField(max_length=1000)
    nearest_location = models.CharField(max_length=500)
    contact = models.CharField(max_length=20, null=True, blank=True)
    payment = models.CharField(max_length=400, choices=(('cash', 'cash'),))
    premium_card = models.FileField(upload_to='premium_cards/', null=True, blank=True)
    status = models.CharField(max_length=200, choices=(
        ('arrived', 'arrived'), ('delay', 'delay'), ('confirmed', 'confirmed'), ('completed', 'completed'),
        ('rejected', 'rejected'), ('on the way', 'on the way')), null=True, blank=True)
    date_scheduled = models.DateTimeField(auto_now=True, null=True, blank=True)
    is_premium = models.BooleanField(default=False, null=True, blank=True)

    def __str__(self):
        return f"Order from {self.user} for {self.work}"


#     CANCEL MODEL

class Cancel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    work = models.ForeignKey(Workers, on_delete=models.CASCADE)
    why_cancel = models.CharField(max_length=600)
    reason = models.CharField(max_length=400, choices=(
        ('i have found better deal somewhere', 'i have found better deal somewhere'),
        ('too expensive', 'too expensive'),))
    rating = models.IntegerField(default=1)
    date_Cancelled = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Order cancelled by {self.user} - {self.work}"


# complaint form

class Complaint(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    work = models.ForeignKey(Purchase, on_delete=models.CASCADE)
    email = models.EmailField()
    complaint = models.CharField(max_length=5000)
    attachment = models.FileField(upload_to='complaints/')
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user} --{self.work}"


# create model to save feedback

class Feedback(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    work = models.ForeignKey(Purchase, on_delete=models.CASCADE)
    choice = models.CharField(max_length=100, choices=(('satisfied', 'satisfied'), ('unsatisfied', 'unsatisfied')))
    rating = models.IntegerField(default=1)
    is_helpful = models.BooleanField(default=False)
    feedback = models.CharField(max_length=500)
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Feedback from {self.user} for {self.work}"


# PAYMENT MODEL TO STORE USERS PAYMENTS
class Payments(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    email = models.EmailField()
    contact = models.CharField(max_length=20)
    screenshot = models.ImageField(upload_to='payments/')
    date = models.DateTimeField(auto_now=True)
    is_premium = models.BooleanField(default=False, null=True, blank=True)

    def __str__(self):
        return f"Payment data from {self.user}"


# CREATE MODEL TO POST WORKERS

class Jobs(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    image = models.ImageField(upload_to='jobs/')
    title = models.CharField(max_length=200)
    package = models.CharField(max_length=200)
    requirements = models.CharField(max_length=500)
    description = models.CharField(max_length=1000)
    date_posted = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} -- {self.package}"


# create model to apply for job
class JobApplications(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    job = models.ForeignKey(Jobs, on_delete=models.CASCADE)
    contact = models.CharField(max_length=20)
    resume = models.FileField(upload_to='resumes/')
    date_applied = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f" {self.user} -- {self.job}"


# contact model
class Contact(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    email = models.EmailField()
    message = models.CharField(max_length=1000)

    def __str__(self):
        return f"Contact request from {self.user}"


# discounts model

class Discounts(models.Model):
    # link = models.CharField(max_length=1000)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    content = HTMLField()
    valid = models.DateField()
    date_posted = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f" {self.role}"

