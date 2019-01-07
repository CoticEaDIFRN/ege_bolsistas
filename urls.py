from django.contrib import admin
from django.urls import include, path
from django.conf.urls import url


urlpatterns = [

    path('cadastro_edital/', include('cadastro_edital.urls')),
    url('admin/', admin.site.urls),
]
