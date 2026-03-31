from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('add-blood-pressure/', views.add_blood_pressure, name='add_blood_pressure'),
    path('add-sugar-level/', views.add_sugar_level, name='add_sugar_level'),
    path('add-weight/', views.add_weight, name='add_weight'),
]
