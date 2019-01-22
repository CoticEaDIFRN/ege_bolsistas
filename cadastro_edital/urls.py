from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
from .services import EditalService, VagaService
from django.contrib import admin


router = DefaultRouter()
router.register('edital', EditalService)
#router.register('vaga', VagaService)

app_name = 'ege_cadastro_edital'
urlpatterns = [
    # path('', views.admin_dashboard, name='dashboard'),
    path('', views.novoEdital, name='novoEdital'),
    # path('i/', views.list_Edital, name='list_Edital'),
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls))

]