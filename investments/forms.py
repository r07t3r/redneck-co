from django import forms
from .models import InvestmentConsultationRequest


class InvestmentConsultationForm(forms.ModelForm):
    class Meta:
        model = InvestmentConsultationRequest
        fields = [
            'first_name', 'last_name', 'email', 'phone',
            'investment_goal', 'time_horizon', 'initial_investment',
            'risk_tolerance', 'additional_notes',
        ]
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email Address'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone Number'}),
            'investment_goal': forms.Select(attrs={'class': 'form-control'}),
            'time_horizon': forms.Select(attrs={'class': 'form-control'}),
            'initial_investment': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'e.g. 10000'}),
            'risk_tolerance': forms.Select(attrs={'class': 'form-control'}),
            'additional_notes': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Any additional goals or questions...'}),
        }
