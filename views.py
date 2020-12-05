from .models import Record, PhoneNumbers, Company, CompanyUnit
from django.views.generic import ListView, CreateView, UpdateView, TemplateView, DeleteView
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
    template_name = 'arm/phonenumbers_index.html'
    template_name_suffix = '_index'
    context_object_name = 'numbers'

    def get_queryset(self):
        pk = self.kwargs['pk']
        company_unit = CompanyUnit.objects.get(pk=pk)
        queryset = PhoneNumbers.objects.filter(unit__name=company_unit)
        return queryset

    def get_context_data(self):
        context = super().get_context_data()
        context['c_unit'] = CompanyUnit.objects.get(pk=self.kwargs['pk'])
        return context


class CompanyCreateView(LoginRequiredMixin, CreateView, ListView):
    model = Company
    template_name = 'arm/company_add.html'
    template_name_suffix = '_add'
    success_url = reverse_lazy('company_edit_index')
    fields = '__all__'
    context_object_name = 'company'
    queryset = Company.objects.all()


class CategoryUnitCreateView(LoginRequiredMixin, CreateView, ListView):
    model = CompanyUnit
    template_name = 'arm/category_unit_add.html'
    template_name_suffix = '_add'
    success_url = reverse_lazy('phone_numbers')
    fields = '__all__'
    context_object_name = 'units'
    queryset = CompanyUnit.objects.all()


class CompanyIndexView(LoginRequiredMixin, ListView):
    model = Company
    template_name = 'arm/company_index.html'
    template_name_suffix = '_index'
    context_object_name = 'companies'
    queryset = Company.objects.all()


class CompanyUpdateIndexView(LoginRequiredMixin, ListView):
    template_name = 'arm/company_update_index.html'
    template_name_suffix = '_index'
    context_object_name = 'companies'
    queryset = Company.objects.all()


class CompanyUpdateView(LoginRequiredMixin, UpdateView):
    model = Company
    template_name_suffix = '_update'
    template_name = 'arm/company_update.html'
    success_url = reverse_lazy('company_update_done')
    fields = '__all__'


class CompanyUpdateSuccessfullyView(LoginRequiredMixin, TemplateView):
    template_name = 'arm/company_update_done.html'


class CompanyDeleteView(LoginRequiredMixin, DeleteView):
    model = Company
    success_url = reverse_lazy('company_delete_done')


class CompanyDeleteSuccessfullyView(LoginRequiredMixin, TemplateView):
    template_name = 'arm/company_delete_done.html'


class CompanyUnitIndexView(LoginRequiredMixin, ListView):
    template_name = 'arm/company_unit_index.html'
    template_name_suffix = '_index'
    context_object_name = 'units'

    def get_queryset(self):
        pk = self.kwargs['pk']
        company = Company.objects.get(pk=pk)
        queryset = CompanyUnit.objects.filter(company__name=company)
        return queryset

    def get_context_data(self):
        context = super().get_context_data()
        context['c_pk'] = Company.objects.get(pk=self.kwargs['pk'])
        return context


class CompanyUnitUpdateIndexView(LoginRequiredMixin, ListView):
    template_name = 'arm/company_unit_update_index.html'
    template_name_suffix = '_index'
    context_object_name = 'units'

    def get_queryset(self):
        pk = self.kwargs['pk']
        company = Company.objects.get(pk=pk)
        queryset = CompanyUnit.objects.filter(company__name=company)
        return queryset

    def get_context_data(self):
        context = super().get_context_data()
        context['c_pk'] = Company.objects.get(pk=self.kwargs['pk'])
        return context


class CompanyUnitUpdateView(LoginRequiredMixin, UpdateView):
    model = CompanyUnit
    template_name_suffix = '_update'
    template_name = 'arm/company_unit_update.html'
    success_url = reverse_lazy('company_index')
    fields = ['name']

    def get_context_data(self):
        context = super().get_context_data()
        context['unit'] = CompanyUnit.objects.get(pk=self.kwargs['pk'])
        return context

    def get_form(self):
        form = super().get_form()
        form.instance.company = Company.objects.get(pk=self.kwargs['pk'])
        return form


class CompanyUnitDeleteView(LoginRequiredMixin, DeleteView):
    model = CompanyUnit
    success_url = reverse_lazy('company_index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['unit_pk'] = CompanyUnit.objects.get(name=context['object']).pk
        return context


class PhoneNumberAddView(LoginRequiredMixin, CreateView):
    model = PhoneNumbers
    template_name = 'arm/phone_number_add.html'
    template_name_suffix = '_add'
    fields = ['name', 'position', 'work', 'mobile']
    success_url = reverse_lazy('phone_done')

    def get_form(self):
        form = super().get_form()
        form.instance.unit = CompanyUnit.objects.get(pk=self.kwargs['pk'])
        return form


class PhoneAddDoneView(LoginRequiredMixin, TemplateView):
    template_name = 'arm/phone_number_add_done.html'


class PhoneNumberUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'arm/phone_number_update.html'
    template_name_suffix = '_update'
    model = PhoneNumbers
    success_url = reverse_lazy('phone_update_done')
    fields = ['name', 'position', 'work', 'mobile']


class PhoneNumberUpdateSucces(LoginRequiredMixin, TemplateView):
    template_name = 'arm/number_update_succes.html'


class PhoneNumberDeleteView(LoginRequiredMixin, DeleteView):
    model = PhoneNumbers
    success_url = reverse_lazy('company_index')


class PhoneNumberUpdateIndex(LoginRequiredMixin, ListView):
    template_name = 'arm/phone_numbers_update_index.html'
    template_name_suffix = '_index'
    context_object_name = 'numbers'

    def get_queryset(self):
        pk = self.kwargs['pk']
        company_unit = CompanyUnit.objects.get(pk=pk)
        queryset = PhoneNumbers.objects.filter(unit__name=company_unit)
        return queryset

    def get_context_data(self):
        context = super().get_context_data()
        context['c_unit'] = CompanyUnit.objects.get(pk=self.kwargs['pk'])
        return context

