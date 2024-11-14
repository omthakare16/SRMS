from django import forms
from .models import ServiceRequest

class ServiceRequestForm(forms.ModelForm):
    class Meta:
        model = ServiceRequest
        # Include only the fields that exist in the ServiceRequest model
        fields = ['request_type', 'details', 'status', 'attachment']
