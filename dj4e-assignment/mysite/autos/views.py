from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Auto, Make
from django.views import View
from django.views.generic.list import ListView

from django.urls import reverse_lazy

# Create your views here.

# Auto Views -

class MainView(LoginRequiredMixin, ListView):
    model = Auto
    fields = '__all__'
    # def get(self, request):
    #     pass

    # def post(self, request):
    #     pass

    # TODO: Consider to add makes count via AJAX.


class AutoCreate(LoginRequiredMixin, CreateView):
    model = Auto
    fields = '__all__'
    success_url = reverse_lazy('autos:all')


class AutoUpdate(LoginRequiredMixin, UpdateView):
    model = Auto
    fields = '__all__'
    success_url = reverse_lazy('autos:all')


class AutoDelete(LoginRequiredMixin, DeleteView):
    model = Auto
    fields = '__all__'
    success_url = reverse_lazy('autos:all')


# Make Views -

class MakeView(LoginRequiredMixin, ListView):
    model = Make
    fields = '__all__'
    # def get(self, request):
    #     pass

    # def post(self, request):
    #     pass

class MakeCreate(LoginRequiredMixin, CreateView):
    model = Make
    fields = '__all__'
    success_url = reverse_lazy('autos:all')


class MakeUpdate(LoginRequiredMixin, UpdateView):
    model = Make
    fields = '__all__'
    success_url = reverse_lazy('autos:all')


class MakeDelete(LoginRequiredMixin, DeleteView):
    model = Make
    fields = '__all__'
    success_url = reverse_lazy('autos:all')


