# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.conf import settings


class Edital(models.Model):
    PERIODO = (
        (1, '1º Período'),
        (2, '2º Período'),
    )

    tipo = models.CharField('Tipo', max_length=100, help_text='Discente/Bolsista')
    programa = models.CharField('Programa', max_length=100)
    numero = models.CharField('Número', max_length=50, null=True, blank=True)
    siglaUO = models.CharField('Unidade organizacional', max_length=100, help_text='Ex.: DG-EAD/IFRN')
    linkEdital = models.URLField('URL', max_length=300, help_text='Informe o LINK onde está o edital')
    grupo = models.CharField('Grupo', max_length=200, null=True)
    descricao = models.CharField('Descrição', max_length=300)
    ano = models.PositiveIntegerField('Ano', help_text='Digite o ano')
    periodo = models.PositiveIntegerField('Período letivo', choices=PERIODO)
    data_publicacao = models.DateField()

    def __str__(self):
        return self.tipo


class Pagamento(models.Model):
    existe_taxa = models.BooleanField(default=False)
    valor_taxa = models.DecimalField(max_digits=7, decimal_places=2)
    vencimento_boleto = models.DateField()
    edital = models.OneToOneField(
        Edital,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return "Pagamento"


class Vaga(models.Model):
    curso = models.CharField('Curso', max_length=200)
    vaga = models.CharField('Vaga', max_length=100)
    numero_vagas = models.IntegerField('Número de vagas')
    edital = models.ForeignKey(Edital, on_delete=models.CASCADE)

    def __str__(self):
        return self.curso


class Usuario(models.Model):
    ifrn_id = models.CharField('Ifrn ID', max_length=100, help_text='Matrícula suap ou CPF')
    nome = models.CharField('Nome', max_length=100)


class Coordenador(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    edital = models.ForeignKey(Edital, on_delete=models.CASCADE)

    def __str__(self):
        return self.usuario


class Fase(models.Model):
    CLASSIFICACAO = (
        (1, 'Eliminatória'),
        (2, 'Classificatória'),
    )

    nome =models.CharField('Nome', max_length=200)
    tipo_classificacao = models.PositiveIntegerField('Tipo de Classificação', choices=CLASSIFICACAO)
    aproveitamento_min = models.PositiveIntegerField('Aproveitamento Mínimo', help_text='Nota necessária para passar')
    fator_habilitacao = models.PositiveIntegerField('Fator Habilitação', help_text='Quantidade máxima de cadidatos que serão selecionados')
    edital = models.ForeignKey(Edital, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome


class Cronograma(models.Model):
    etapa = models.CharField('Etapa', max_length=200)
    marco = models.CharField('Marco', max_length=200)
    inicio = models.DateField('Data Inicial')
    fim = models.DateField('Data Final')
    fase = models.OneToOneField(
        Fase,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.etapa


class Documento(models.Model):
    nome = models.CharField('Nome', max_length=200)
    fase = models.ForeignKey(Fase, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome


class Avaliador(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    fase = models.ForeignKey(Fase, on_delete=models.CASCADE)

    def __str__(self):
        return self.usuario


class CriterioAvaliacao(models.Model):
    descricao = models.CharField('Nome', max_length=200)
    nota_minima = models.FloatField('Nota Mínima')
    nota_maxima = models.FloatField('Nota Maxima')
    ajuda_avaliador = models.CharField('Nome', max_length=500)
    incremento_nota =models.IntegerField('Incremento da Nota')
    fase = models.ForeignKey(Fase, on_delete=models.CASCADE)

    def __str__(self):
        return self.descricao


class MotivoNotaZero(models.Model):
    descriaco = models.CharField('Descrição', max_length=200, help_text='Exemplo: Inscrição sem anexos')
    fase = models.ForeignKey(Fase, on_delete=models.CASCADE)

    def __str__(self):
        return self.descricao

#por enquanto vai ficar internamente, pois essa classe não está nas telas
class EstrategiaClassificacao(models.Model):
    descriaco = models.CharField('Descrição', max_length=200, help_text='Exemplo: Inscrição sem anexos')
    fase = models.ForeignKey(Fase, on_delete=models.CASCADE)

    def __str__(self):
        return self.descricao