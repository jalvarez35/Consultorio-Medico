from django import forms
from models import Paciente, HistoriaClinica

class PacienteForm(forms.ModelForm):
    class Meta:
        model = Paciente

class HistoriaClinicaForm(forms.ModelForm):
    class Meta:
        model = HistoriaClinica
