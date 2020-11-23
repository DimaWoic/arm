from .models import Record, PhoneNumbers, Category
from django.views.generic import ListView, CreateView, UpdateView, RedirectView
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q


class UserLoginView(LoginView):
    template_name = 'arm/login.html'
    redirect_authenticated_user = True

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


class RecordSearchResultView(LoginRequiredMixin, ListView):
    model = Record
    template_name_suffix = '_result'
    template_name = 'arm/record_search.html'
    context_object_name = 'records'

    def get_queryset(self):
        search = self.request.GET.get('q')
        query = Q(from_who=search) | Q(description=search)
        result = Record.objects.filter(query)
        return result


class RecordSearchDateResultView(LoginRequiredMixin, ListView):
    model = Record
    template_name = 'arm/record_search_date.html'
    template_name_suffix = '_date'
    context_object_name = 'records'

    def get_queryset(self):
        search = self.request.GET.get('date')
        query = Record.objects.filter(date=search)
        return query


class PhoneNumbersIndexView(LoginRequiredMixin, ListView):
    model = PhoneNumbers
    template_name = 'arm/phonenumbers_index.html'
    template_name_suffix = '_index'
    context_object_name = 'numbers'


class CategoryUnitCreateView(LoginRequiredMixin, CreateView, ListView):
    model = Category
    template_name = 'arm/category_unit_add.html'
    template_name_suffix = '_add'
    success_url = reverse_lazy('phone_numbers')
    fields = '__all__'
    context_object_name = 'units'
    queryset = Category.objects.all()

