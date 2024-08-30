from django import forms
from .models import HomeProject, Call


# home_project form

class HomeProjectForm(forms.ModelForm):
    class Meta():
        model = HomeProject
        fields = ['customer_name', 'contact_phone', 'contact_email', 'project_name', 'project_description', 'location',
                  'budget', 'style', 'size_sqft', 'num_bedrooms', 'num_bathrooms', 'sample_design', 'start_date',
                  'completion_date']


class CallForm(forms.ModelForm):
    class Meta():
        model=Call
        fields = ['time', 'or_specified_time']


# create form to generate qrcode

class ImageUploadForm(forms.Form):
    image = forms.ImageField()

