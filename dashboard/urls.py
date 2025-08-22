from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),  # Dashboard view
    path('api/chart-data/', views.get_chart_data, name='chart_data'),  # API endpoint for chart data
]
