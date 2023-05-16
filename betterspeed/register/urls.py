from django.urls import path
from . import views

urlpatterns = [
    path('', views.register_home, name="register-home"),
]