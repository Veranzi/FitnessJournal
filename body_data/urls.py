from django.urls import path
from . import views

urlpatterns = [
    path('addbody/', views.add_body_data, name='add_body_data'),
    path('bodyrecords', views.body_data, name='body_data'),
]
