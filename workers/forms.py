from django import forms
from .models import Purchase, Cancel, Complaint, Feedback, Payments, JobApplications, Contact


# create purchase form

class PurchaseForm(forms.ModelForm):
    class Meta():
        model = Purchase
        fields = ['address', 'nearest_location', 'payment', 'contact', 'premium_card']
        widgets = {
            'address': forms.Textarea(attrs={'class': 'form-control', 'rows': 5, 'cols': 45})
        }


# cancel form
class CancelForm(forms.ModelForm):
    class Meta():
        model = Cancel
        fields = ['why_cancel', 'reason', 'rating']


# CREATE COMPLAINT FORM
class ComplaintForm(forms.ModelForm):
    class Meta():
        model = Complaint
        fields = ['complaint', 'email', 'attachment']
        widgets = {
            'complaint': forms.Textarea(attrs={'class': 'form-control', 'rows': 5, 'cols': 35})
        }


# FEEDBACK FORM
class FeedbackForm(forms.ModelForm):
    class Meta():
        model = Feedback
        fields = ['choice', 'rating', 'is_helpful', 'rating', 'feedback']
        widgets = {
            'feedback': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'cols': 30})
        }


# create paymentsForm

class PaymentsForm(forms.ModelForm):
    class Meta():
        model = Payments
        fields = ['email', 'contact', 'screenshot']


# create job applicationForm
class JobsApplicationsForm(forms.ModelForm):
    class Meta():
        model = JobApplications
        fields = ['contact', 'resume', ]


# contact form

class ContactForm(forms.ModelForm):
    class Meta():
        model = Contact
        fields = ['email', 'message']
        widgets = {
            'message': forms.Textarea(attrs={'class': 'form-control', 'rows': 2, 'cols': 20})

        }
