from django.shortcuts import render
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView, ListView
from django.core.urlresolvers import reverse_lazy
from .models import Proyecto

class ProyectoListView(ListView):
	model = Proyecto
	templates = 'mascota/mascota_list.html'

mascota_list = ProyectoListView.as_view()

class ProyectoCreateView(CreateView):
	model = Proyecto
	templates = 'mascota/mascota_form.html'
	fields = '__all__'
	success_url = reverse_lazy('mascota_list')

mascota_create = ProyectoCreateView.as_view()

class ProyectoEditView(UpdateView):
	model = Taller
	templates = 'mascota/mascota_edit.html'
	fields = '__all__'
	success_url = reverse_lazy('mascota_list')

mascota_edit = ProyectoEditView.as_view()












# Create your views here.
