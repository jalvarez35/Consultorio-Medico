from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView 
from django.core.urlresolvers import reverse_lazy

from models import Paciente, HistoriaClinica
from forms import PacienteForm, HistoriaClinicaForm


class PacienteList(ListView):
    model = Paciente
    template_name = 'paciente_list.html'

class PacienteCreate(CreateView):
    model = Paciente
    form_class = PacienteForm
    template_name = 'paciente_create.html'
    success_url = reverse_lazy('paciente_list')

class PacienteUpdate(UpdateView):
    model = Paciente
    template_name = 'paciente_create.html'
    success_url = reverse_lazy('paciente_list')

class PacienteDelete(DeleteView):
    model = Paciente
    template_name = 'paciente_delete.html'
    success_url = reverse_lazy('paciente_list')

class HistoriaClinicaList(ListView):
    model = HistoriaClinica
    template_name = 'historiaclinica_list.html'

class HistoriaClinicaCreate(CreateView):
    model = HistoriaClinica
    form_class = HistoriaClinicaForm
    template_name = 'historiaclinica_create.html'
    success_url = reverse_lazy('historiaclinica_list')

class HistoriaClinicateUpdate(UpdateView):
    model = HistoriaClinica
    template_name = 'historiaclinica_create.html'
    success_url = reverse_lazy('historiaclinica_list')

class HistoriaClinicaDelete(DeleteView):
    model = HistoriaClinica
    template_name = 'historiaclinica_delete.html'
    success_url = reverse_lazy('historiaclinica_list')
