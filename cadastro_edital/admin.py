from django.contrib import admin
from .models import Edital, Vaga, Fase, Coordenador, Usuario, Avaliador, Documento, Cronograma, CriterioAvaliacao, MotivoNotaZero


class VagaInline(admin.TabularInline):
    model = Vaga
    extra = 1

class CoordenadorInline(admin.TabularInline):
    model = Coordenador
    extra = 1

class EditalAdmin(admin.ModelAdmin):
    inlines = [
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

admin.site.register(Edital, EditalAdmin)
admin.site.register(Usuario)
admin.site.register(Fase, FaseAdmin)
