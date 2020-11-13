from django.urls import path
from . import views

urlpatterns = [
    path('record_index/', views.RecordIndexView.as_view(), name='record_index'),
    path('add_record/', views.RecordCreateView.as_view(), name='add_record'),
    path('', views.UserLoginView.as_view(), name='login'),
    path('logout/', views.UserLogoutView.as_view(), name='logout'),
]
