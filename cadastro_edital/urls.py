from django.urls import path

from . import views

urlpatterns = [
    path('', views.novoEdital, name='novoEdital'),
    path('i/', views.list_Edital, name='list_Edital'),
    path('v/', views.list_vaga, name='list_Vaga')

]