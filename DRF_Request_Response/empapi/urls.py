from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.getcreate, name='getcreate'),
    path('<int:pk>/', views.getputdelete, name='getputdelete'),
]