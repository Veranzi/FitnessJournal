# planning/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('plans/', views.training_plans, name='training_plans'),
    path('plans/create/', views.create_training_plan, name='create_training_plan'),  # New path
    path('plans/<int:plan_id>/sessions/', views.training_plan_sessions, name='training_plan_sessions'),
    path('plans/<int:plan_id>/sessions/create/', views.create_training_session, name='create_training_session'),
    path('plans/<int:plan_id>/sessions/<int:session_id>/complete/', views.mark_session_complete, name='mark_session_complete'),

]
