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
            return JsonResponse(data)
        else:
            return response

class update(UpdateView):
    model = Salon
    fields = '__all__'
    template_name = 'darjano/create.html'
    success_url = '/darjano/show'
    def get_queryset(self):
        slug = self.kwargs['slug']
        return Salon.objects.filter(slug=slug)

class delete(DeleteView):
    model = Salon
    success_url = '/darjano/show'

def deleteall(request):
    data = Salon.objects.all()
    data.delete()
    return redirect('/darjano/show')