from django import forms
from .models import InsuranceQuoteRequest


class InsuranceQuoteForm(forms.ModelForm):
    class Meta:
        model = InsuranceQuoteRequest
        fields = [
            'first_name', 'last_name', 'email', 'phone',
            'date_of_birth', 'gender', 'health_status',
            'tobacco_use', 'coverage_amount', 'additional_notes',
        ]
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email Address'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone Number'}),
            'date_of_birth': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'gender': forms.Select(attrs={'class': 'form-control'}),
            'health_status': forms.Select(attrs={'class': 'form-control'}),
            'tobacco_use': forms.Select(attrs={'class': 'form-control'}),
            'coverage_amount': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'e.g. 500000'}),
            'additional_notes': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Any additional information...'}),
        }
