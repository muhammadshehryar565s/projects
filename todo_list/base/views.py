from typing import Any, Dict
from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView,DeleteView
from django.urls import reverse_lazy

from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import task
# Create your views here.

class customloginview(LoginView):
    template_name='base/login.html'
    fields= '__all__'
    redirect_authenticated_user=True
    def get_success_url(self):
       return reverse_lazy('task1')


class Tasklist(LoginRequiredMixin,ListView):
    model=task
    context_object_name='tasks'

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['tasks'] = context['tasks'].filter(user=self.request.user)
        context['count'] = context['tasks'].filter(complete=False).count()
        
        return context
         

class detailtask(LoginRequiredMixin,DetailView):
    model= task

class taskcreate(LoginRequiredMixin,CreateView):
    model= task
    fields= ['title','description','complete']
    success_url = reverse_lazy('task1')    

    def form_valid(self, form):
        form.instance.user=self.request.user
        return super(taskcreate,self).form_valid(form) 

class updatetask(LoginRequiredMixin,UpdateView):
    model= task
    fields=  ['title','description','complete']
    success_url = reverse_lazy('task1')   

class deletetask(LoginRequiredMixin,DeleteView):
    model= task
    context_object_name='tasks'
    success_url = reverse_lazy('task1')



  