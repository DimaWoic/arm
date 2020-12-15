from django.urls import path
from . import views

urlpatterns = [
    path('record_index/', views.RecordIndexView.as_view(), name='record_index'),
    path('add_record/', views.RecordCreateView.as_view(), name='add_record'),
    path('', views.UserLoginView.as_view(), name='login'),
    path('logout/', views.UserLogoutView.as_view(), name='logout'),
    path('record_update/<int:pk>', views.RecordUpdateView.as_view(), name='record_update'),
    path('record_search/', views.RecordSearchResultView.as_view(), name='search'),
    path('record_search_date/', views.RecordSearchDateResultView.as_view(), name='search_date'),
    path('phone_numbers/<int:pk>', views.PhoneNumbersIndexView.as_view(), name='phone_numbers'),
    path('company_add/', views.CompanyCreateView.as_view(), name='company_add'),
    path('companies/', views.CompanyIndexView.as_view(), name='company_index'),
    path('company_units/<int:pk>', views.CompanyUnitIndexView.as_view(), name='company_units'),
    path('phonenumber_add/<int:pk>', views.PhoneNumberAddView.as_view(), name='phonenumber_add'),
    path('phone_number_add_done/', views.PhoneAddDoneView.as_view(), name='phone_done'),
    path('phone_number_update/<int:pk>', views.PhoneNumberUpdateView.as_view(), name='phone_update'),
    path('phone_number_delete/<int:pk>', views.PhoneNumberDeleteView.as_view(), name='phone_delete'),
    path('phone_number_update_index/<int:pk>', views.PhoneNumberUpdateIndex.as_view(), name='phone_update_index'),
    path('phone_number_update_done/<int:pk>', views.PhoneNumberUpdateSucces.as_view(), name='phone_update_done'),
    path('company_edit_index/', views.CompanyUpdateIndexView.as_view(), name='company_edit_index'),
    path('company_edit/<int:pk>', views.CompanyUpdateView.as_view(), name='company_edit'),
    path('company_delete/<int:pk>', views.CompanyDeleteView.as_view(), name='company_delete'),
    path('company_unit_edit_index/<int:pk>', views.CompanyUnitUpdateIndexView.as_view(), name='company_unit_edit_index'),
    path('company_unit_edit/<int:pk>', views.CompanyUnitUpdateView.as_view(), name='company_unit_edit'),
    path('company_unit_delete/<int:pk>', views.CompanyUnitDeleteView.as_view(), name='company_unit_delete'),
    path('company_update_done/', views.CompanyUpdateSuccessfullyView.as_view(), name='company_update_done'),
    path('company_delete_done/', views.CompanyDeleteSuccessfullyView.as_view(), name='company_delete_done'),
    path('company_unit_delete_done/<int:pk>', views.CompanyUnitUpdateSuccessfullyView.as_view(),
         name='company_unit_update_done'),
    path('company_unit_create/<int:pk>', views.CompanyUnitCreateView.as_view(), name='company_unit_create'),

]
