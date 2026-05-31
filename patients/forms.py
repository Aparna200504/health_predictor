from django import forms
from .models import Patient
from datetime import date


class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ['full_name', 'date_of_birth', 'email', 'glucose', 'haemoglobin', 'cholesterol']
        widgets = {
            'date_of_birth': forms.DateInput(attrs={'type': 'date'}),
        }

    def clean_date_of_birth(self):
        """Validate that date of birth is not in the future."""
        dob = self.cleaned_data.get('date_of_birth')
        if dob and dob > date.today():
            raise forms.ValidationError("Date of birth cannot be in the future.")
        return dob

    def clean_haemoglobin(self):
        """Validate that haemoglobin doesn't exceed healthy range."""
        haemoglobin = self.cleaned_data.get('haemoglobin')
        if haemoglobin is not None and haemoglobin > 20:
            raise forms.ValidationError("Haemoglobin value seems unusually high (>20 g/dL).")
        return haemoglobin

    def clean_cholesterol(self):
        """Validate that cholesterol doesn't exceed healthy range."""
        cholesterol = self.cleaned_data.get('cholesterol')
        if cholesterol is not None and cholesterol > 500:
            raise forms.ValidationError("Cholesterol value seems unusually high (>500 mg/dL).")
        return cholesterol
