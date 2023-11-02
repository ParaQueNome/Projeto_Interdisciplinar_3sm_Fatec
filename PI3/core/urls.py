from django.contrib import admin
from django.urls import path
from django.urls import include
from .import views

urlpatterns = [
    path('cadastro', views.cadastro, name='cadastro'),
    path('cadastro_juridico', views.cadastro_juridico, name='cadastro_juridico'),
    path('cadastro_fisico', views.cadastro_fisico, name = 'cadastro_fisico')



]