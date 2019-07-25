from django.urls import path, include
from cadastro_edital.views import RegistrarEditalView,RegistrarVagaView
from rest_framework.routers import DefaultRouter
from .services import EditalService, VagaService
from django.contrib import admin


router = DefaultRouter()
router.register('edital', EditalService)

urlpatterns = [
    # path('', views.admin_dashboard, name='dashboard'),
    path('edital/', RegistrarEditalView.as_view(), name='novoEdital'),
    path('confirmaredital/', RegistrarEditalView.confirmarEdital, name='confirmar'), # interno do sistema. Não deve ser um caminho para o usuário final
    path('confirmarvaga/', RegistrarVagaView.as_view(), name='vaga'), # interno do sistema. Não deve ser um caminho para o usuário final
    path('confirmarvaga/', RegistrarVagaView.confirmarVaga, name='confirmarvaga'), # interno do sistema. Não deve ser um caminho para o usuário final
    path('listar/', RegistrarEditalView.lista_editais, name='listareditais'),
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls)),

]