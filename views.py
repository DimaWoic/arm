from .models import Record, PhoneNumbers, Company, CompanyUnit
from django.views.generic import ListView, CreateView, UpdateView, TemplateView, DeleteView
from django.urls import reverse_lazy, reverse
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q


class UserLoginView(LoginView):
    """Контроллер формы входа в систему"""
    template_name = 'arm/login.html'
    redirect_authenticated_user = True

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['next'] = reverse_lazy('record_index')
        return context


class UserLogoutView(LoginRequiredMixin, LogoutView):
    """Контроллер формы выхода из системы"""
    next_page = 'login'


class RecordIndexView(LoginRequiredMixin, ListView):
    """Контроллер вывода всех записей в оперативном журнале"""
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
    """Контроллер создания записи в оперативном журнале"""
    model = Record
    template_name_suffix = '_create'
    template_name = 'arm/record_create.html'
    context_object_name = 'record'
    success_url = reverse_lazy('record_index')
    fields = '__all__'

    def get_queryset(self):
        return Record.objects.all()


class RecordUpdateView(LoginRequiredMixin, UpdateView, ListView):
    """Контроллер изменения записи в оперативном журнале"""
    model = Record
    template_name_suffix = '_update'
    success_url = reverse_lazy('record_index')
    fields = '__all__'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['record'] = Record.objects.all()
        return context


class RecordSearchResultView(LoginRequiredMixin, ListView):
    """Контроллер поиска записи в оперативном журнале"""
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
    """Контроллер вывода результата поиска записи в оперативном журнале"""
    model = Record
    template_name = 'arm/record_search_date.html'
    template_name_suffix = '_date'
    context_object_name = 'records'

    def get_queryset(self):
        search = self.request.GET.get('date')
        query = Record.objects.filter(date=search)
        return query


class PhoneNumbersIndexView(LoginRequiredMixin, ListView):
    """Контроллер вывода телефонных номеров определённого абонента"""
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
    """Контроллер создания организации телефонного справочника"""
    model = Company
    template_name = 'arm/company_add.html'
    template_name_suffix = '_add'
    success_url = reverse_lazy('company_edit_index')
    fields = '__all__'
    context_object_name = 'company'
    queryset = Company.objects.all()


class CompanyIndexView(LoginRequiredMixin, ListView):
    """Контроллер вывода списка организации телефонного справочника"""
    model = Company
    template_name = 'arm/company_index.html'
    template_name_suffix = '_index'
    context_object_name = 'companies'
    queryset = Company.objects.all()


class CompanyUpdateIndexView(LoginRequiredMixin, ListView):
    """Контроллер вывода списка для редактирования названий организаций и их удаление"""
    template_name = 'arm/company_update_index.html'
    template_name_suffix = '_index'
    context_object_name = 'companies'
    queryset = Company.objects.all()


class CompanyUpdateView(LoginRequiredMixin, UpdateView):
    """Контроллер изменения названия организации"""
    model = Company
    template_name_suffix = '_update'
    template_name = 'arm/company_update.html'
    success_url = reverse_lazy('company_update_done')
    fields = '__all__'


class CompanyUpdateSuccessfullyView(LoginRequiredMixin, TemplateView):
    """Контроллер вывода сообщения об успешном изменнии названия организации"""
    template_name = 'arm/company_update_done.html'


class CompanyDeleteView(LoginRequiredMixin, DeleteView):
    """Контроллер удаления организации"""
    model = Company
    success_url = reverse_lazy('company_delete_done')


class CompanyDeleteSuccessfullyView(LoginRequiredMixin, TemplateView):
    """Контроллер вывода сообщения об успешном удалении организации"""
    template_name = 'arm/company_delete_done.html'


class CompanyUnitIndexView(LoginRequiredMixin, ListView):
    """Контроллер вывода списка подразделений организации"""
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
    """Контроллер вывода списка для редактирования названий подразделений организации и их удаление"""
    template_name = 'arm/company_unit_update_index.html'
    template_name_suffix = '_index'
    context_object_name = 'units'

    def get_queryset(self):
        """Метод вывода подразделений компании"""
        pk = self.kwargs['pk']
        company = Company.objects.get(pk=pk)
        queryset = CompanyUnit.objects.filter(company__name=company)
        return queryset

    def get_context_data(self):
        context = super().get_context_data()
        context['c_pk'] = Company.objects.get(pk=self.kwargs['pk'])
        return context


class CompanyUnitUpdateView(LoginRequiredMixin, UpdateView):
    """Контроллер изменения названия подразделения организации"""
    model = CompanyUnit
    template_name_suffix = '_update'
    template_name = 'arm/company_unit_update.html'
    success_url = reverse_lazy('company_unit_update_done')
    fields = ['name']

    def get_context_data(self):
        context = super().get_context_data()
        company_unit = CompanyUnit.objects.get(pk=self.kwargs['pk'])
        context['unit'] = company_unit
        company = Company.objects.get(name=company_unit.company.name).pk
        context['company'] = company
        return context


class CompanyUnitUpdateSuccessfullyView(LoginRequiredMixin, TemplateView):
    """Контроллер вывода сообщения об успешном изменнии названия подразделения организации"""
    template_name = 'arm/company_unit_update_done.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        company_unit = CompanyUnit.objects.get(pk=self.kwargs['pk'])
        company = Company.objects.get(name=company_unit.company.name).pk
        context['company'] = company
        return context


class CompanyUnitDeleteView(LoginRequiredMixin, DeleteView):
    """Контроллер удаления подразделения организации"""
    model = CompanyUnit
    success_url = reverse_lazy('company_index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['unit_pk'] = CompanyUnit.objects.get(name=context['object']).pk
        return context


class CompanyUnitCreateView(LoginRequiredMixin, CreateView):
    """Контроллер создания подразделения организации телефонного справочника"""
    model = CompanyUnit
    template_name = 'arm/company_unit_add.html'
    template_name_suffix = '_add'
    success_url = reverse_lazy('company_index')
    fields = ['name']

    def get_form(self, form_class=None):
        form = super().get_form()
        form.instance.company = Company.objects.get(pk=self.kwargs['pk'])
        return form


class PhoneNumberAddView(LoginRequiredMixin, CreateView):
    """Форма добавления номера телефона подразделения организации"""
    model = PhoneNumbers
    template_name = 'arm/phone_number_add.html'
    template_name_suffix = '_add'
    fields = ['name', 'position', 'work', 'mobile']

    def get_form(self):
        """Метод сохраняющий (в форме) автоматически подразделение к которому пренадлежит номер"""
        form = super().get_form()
        form.instance.unit = CompanyUnit.objects.get(pk=self.kwargs['pk'])
        return form

    def get_success_url(self):
        return reverse('phone_done', args=[self.kwargs['pk']])


class PhoneAddDoneView(LoginRequiredMixin, TemplateView):
    """Контроллер выводит сообщение о успешном добавлении номера телефона"""
    template_name = 'arm/phone_number_add_done.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['c_unit_pk'] = CompanyUnit.objects.get(pk=self.kwargs['pk']).pk
        return context


class PhoneNumberUpdateView(LoginRequiredMixin, UpdateView):
    """Контроллер выводящий форму для изменения номера телефона"""
    template_name = 'arm/phone_number_update.html'
    template_name_suffix = '_update'
    model = PhoneNumbers
    fields = ['name', 'position', 'work', 'mobile']

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        phone_unit = PhoneNumbers.objects.get(pk=self.kwargs['pk'])
        context['c_unit_pk'] = CompanyUnit.objects.get(name=phone_unit.unit.name).pk
        return context

    def get_success_url(self):
        return reverse('phone_update_done', args=[self.kwargs['pk']])


class PhoneNumberUpdateSucces(LoginRequiredMixin, TemplateView):
    """Контроллер выводит сообщение о успешном изменении номера телефона"""
    template_name = 'arm/number_update_succes.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        phone_unit = PhoneNumbers.objects.get(pk=self.kwargs['pk'])
        context['c_unit_pk'] = CompanyUnit.objects.get(name=phone_unit.unit.name).pk
        return context


class PhoneNumberDeleteView(LoginRequiredMixin, DeleteView):
    """Контроллер удаления номера телефона"""
    model = PhoneNumbers
    success_url = reverse_lazy('company_index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        phone_unit = PhoneNumbers.objects.get(pk=self.kwargs['pk'])
        context['c_unit_pk'] = CompanyUnit.objects.get(name=phone_unit.unit.name).pk
        return context


class PhoneNumberUpdateIndex(LoginRequiredMixin, ListView):
    """Контроллер выводит список телефонных номеров для редактирования"""
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


class SchemaMainView(LoginRequiredMixin, TemplateView):
    template_name = 'arm/schema_main.html'


class CompanySearchResultView(LoginRequiredMixin, ListView):
    """Контроллер поиска организации в телефонном справочнике"""
    model = Company
    template_name_suffix = '_result'
    template_name = 'arm/company_search_result.html'
    context_object_name = 'companies'

    def get_queryset(self):
        search = self.request.GET.get('q')
        query = Q(name=search)
        result = Company.objects.filter(query)
        return result


class RecordPdfView(LoginRequiredMixin, ListView):
    """Контроллер вывода всех записей в оперативном журнале"""
    queryset = Record.objects.all()
    template_name = 'arm/pdf_index.html'
    template_name_suffix = '_index'
    context_object_name = 'records'
    login_url = reverse_lazy('login')

    def get_login_url(self, **kwargs):
        super().get_login_url(**kwargs)
        login_url = reverse_lazy('login')
        return login_url
