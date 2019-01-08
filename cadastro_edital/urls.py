from django.urls import path

from . import views

app_name = 'ege_cadastro_edital'
urlpatterns = [
    path('', views.admin_dashboard, name='dashboard'),
    # path('', views.novoEdital, name='novoEdital'),
    # path('i/', views.list_Edital, name='list_Edital'),
    # path('v/', views.list_vaga, name='list_Vaga')

]