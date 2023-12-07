from django.contrib import admin
from django.urls import path
from django.urls import include
from .import views

urlpatterns = [
    path('', views.cadastro,name= 'cadastro'),
    path('cadastro_juridico', views.cadastro_juridico, name='cadastro_juridico'),
    path('cadastro_fisico', views.cadastro_fisico, name = 'cadastro_fisico'),
    path('doacao',views.doacao, name='doacao'),
    path('login', views.login,name='login'),
    path('doacao_alimento',views.doar_alimento, name = 'alimento'),
    path('relatorios',views.relatorio, name='relatorio'),
    path('remover_alimento/<str:alimento_id>',views.remover_alimento, name='remover_alimento'),
    path('editarDoacao/<str:alimento_id>',views.editarDoacao, name='editarDoacao'),
    path('processar_atualizacao/<str:alimento_id>',views.processar_atualizacao, name='processar_atualizacao'),
    path('registroDoacao', views.registrarDoacao, name='registroDoacao'),
]