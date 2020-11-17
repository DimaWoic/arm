from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import Record
from django.views.generic import ListView, CreateView, UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin


class UserLoginView(LoginView):
    template_name = 'arm/login.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['next'] = reverse_lazy('record_index')
        return context


class UserLogoutView(LoginRequiredMixin, LogoutView):
    next_page = 'login'


class RecordIndexView(LoginRequiredMixin, ListView):
    queryset = Record.objects.all()
    template_name = 'arm/record_index.html'
    template_name_suffix = '_index'
    context_object_name = 'records'
    login_url = reverse_lazy('login')

    def get_login_url(self, **kwargs):
        super().get_login_url(**kwargs)
        login_url = reverse_lazy('login')
        return login_url


class RecordCreateView(LoginRequiredMixin, CreateView, ListView):
    model = Record
    template_name_suffix = '_create'
    template_name = 'arm/record_create.html'
    context_object_name = 'record'
    success_url = reverse_lazy('record_index')
    fields = '__all__'
    login_url = reverse_lazy('login')

    def get_queryset(self):
        return Record.objects.all()


class RecordUpdateView(LoginRequiredMixin, UpdateView, ListView):
    model = Record
    template_name_suffix = '_update'
    success_url = reverse_lazy('record_index')
    fields = '__all__'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['record'] = Record.objects.all()
        return context
