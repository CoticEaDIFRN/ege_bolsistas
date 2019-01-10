from django.contrib import admin
from ege_auth_jwt.sites import ege_admin_site
from .models import Edital, Pagamento, Vaga, Fase, Coordenador, Usuario, Avaliador, Documento, Cronograma, CriterioAvaliacao, MotivoNotaZero


class PagamentoInline(admin.TabularInline):
    model = Pagamento
    extra = 1


class VagaInline(admin.TabularInline):
    model = Vaga
    extra = 1

class CoordenadorInline(admin.TabularInline):
    model = Coordenador
    extra = 1

class EditalAdmin(admin.ModelAdmin):
    inlines = [
        PagamentoInline,
        VagaInline,
        CoordenadorInline
    ]

class CronogramaInline(admin.TabularInline):
    model = Cronograma
    extra = 1

class DocumentoInline(admin.TabularInline):
    model = Documento
    extra = 1

class AvaliadorInline(admin.TabularInline):
    model = Avaliador
    extra = 1

class CriterioAvaliacaoInline(admin.TabularInline):
    model = CriterioAvaliacao
    extra = 1

class MotivoNotaZeroInline(admin.TabularInline):
    model = MotivoNotaZero
    extra = 1


class FaseAdmin(admin.ModelAdmin):
    inlines = [
        CronogramaInline,
        DocumentoInline,
        AvaliadorInline,
        CriterioAvaliacaoInline,
        MotivoNotaZeroInline
    ]

ege_admin_site.register(Edital, EditalAdmin)
ege_admin_site.register(Usuario)
ege_admin_site.register(Fase, FaseAdmin)
