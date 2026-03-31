from django import forms
from .models import BloodPressure, SugarLevel, Weight


class BloodPressureForm(forms.ModelForm):
    class Meta:
        model = BloodPressure
        fields = ['systolic', 'diastolic', 'notes']
        widgets = {
            'systolic': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Systolic (e.g., 120)',
                'min': '50',
                'max': '250'
            }),
            'diastolic': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Diastolic (e.g., 80)',
                'min': '30',
                'max': '150'
            }),
            'notes': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Optional notes...'
            }),
        }


class SugarLevelForm(forms.ModelForm):
    class Meta:
        model = SugarLevel
        fields = ['glucose_level', 'meal_timing', 'notes']
        widgets = {
            'glucose_level': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Blood glucose (e.g., 100)',
                'step': '0.1',
                'min': '20',
                'max': '600'
            }),
            'meal_timing': forms.Select(attrs={
                'class': 'form-control'
            }),
            'notes': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Optional notes...'
            }),
        }


class WeightForm(forms.ModelForm):
    class Meta:
        model = Weight
        fields = ['weight', 'notes']
        widgets = {
            'weight': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Weight in kg (e.g., 70.5)',
                'step': '0.1',
                'min': '20',
                'max': '300'
            }),
            'notes': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Optional notes...'
            }),
        }
