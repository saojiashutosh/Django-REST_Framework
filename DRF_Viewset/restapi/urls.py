from django.urls import path,include
from rest_framework import routers
from .views import CustomerViewSet

router = routers.DefaultRouter()

router.register("customer",CustomerViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    # path('', views.home, name='home')
]