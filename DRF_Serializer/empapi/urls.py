from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('<int:pk>/', views.getemp, name='getemp'),
    path('create/', views.create_data, name='create'),
    path('update/', views.create_data, name='update')
]