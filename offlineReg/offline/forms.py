from django import forms
from .models import Registration

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Registration
        fields = ['name', 'roll_number', 'year', 'branch', 'section', 'email', 'mobile_number', 'event','payment_recived']
