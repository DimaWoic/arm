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
    path('phone_numbers/', views.PhoneNumbersIndexView.as_view(), name='phone_numbers'),
    path('units_add/', views.CompanyCreateView.as_view(), name='company_add'),
]
