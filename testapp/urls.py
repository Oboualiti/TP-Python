from django.urls import path
from . import views # Importe depuis le dossier testapp

urlpatterns = [
    path('', views.index, name='index'),
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('counter', views.counter, name='counter'),
]