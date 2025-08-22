

from django.urls import path
from . import views

urlpatterns = [
    path('addsleep/', views.add_sleep_record, name='add_sleep_record'),
    path('sleeprecords', views.sleep_records, name='sleep_records'),
]
