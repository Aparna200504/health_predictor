from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Patient
from .forms import PatientForm
from .services import generate_remark


class PatientListView(ListView):
    """Display list of all patients."""
    model = Patient
    template_name = 'patients/patient_list.html'
    context_object_name = 'patients'


class PatientCreateView(CreateView):
    """Create a new patient with health prediction."""
    model = Patient
    form_class = PatientForm
    template_name = 'patients/patient_form.html'
    success_url = reverse_lazy('patient_list')

    def form_valid(self, form):
        # Save the patient temporarily to get the object (without committing)
        self.object = form.save(commit=False)
        # Call external API
        self.object.remarks = generate_remark(
            self.object.glucose,
            self.object.haemoglobin,
            self.object.cholesterol
        )
        self.object.save()
        return super().form_valid(form)


class PatientUpdateView(UpdateView):
    """Update an existing patient with health prediction."""
    model = Patient
    form_class = PatientForm
    template_name = 'patients/patient_form.html'
    success_url = reverse_lazy('patient_list')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        # Re-predict if blood values changed
        self.object.remarks = generate_remark(
            self.object.glucose,
            self.object.haemoglobin,
            self.object.cholesterol
        )
        self.object.save()
        return super().form_valid(form)


class PatientDeleteView(DeleteView):
    """Delete a patient."""
    model = Patient
    template_name = 'patients/patient_confirm_delete.html'
    success_url = reverse_lazy('patient_list')
