from django.shortcuts import render,redirect
from .models import Salon,Branch,SalonForm
from django.views.generic import ListView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.http import JsonResponse

class show(ListView):
    model = Salon
    template_name = 'darjano/show.html'

class create(CreateView):
    model = Salon
    fields = '__all__'
    template_name = 'darjano/create.html'
    success_url = '/darjano/show'
    def form_valid(self, form):
        response = super().form_valid(form)
        if self.request.is_ajax():
            data = {
                'pk':self.object.pk
            }
            print('Ajax')
            return JsonResponse(data)
        else:
            print('shit yaar not ajax')
            return response

class update(UpdateView):
    model = Salon
    fields = '__all__'
    template_name = 'darjano/create.html'
    success_url = '/darjano/show'
    def get_queryset(self):
        id = self.kwargs['pk']
        return Salon.objects.filter(pk=id)

class delete(DeleteView):
    model = Salon
    success_url = '/darjano/show'