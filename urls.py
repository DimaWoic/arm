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
    path('phone_number_delete/<int:pk>', views.PhoneNumberDeleteView.as_view(), name='phone_delete')
]
