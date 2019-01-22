from django.utils.translation import gettext_lazy as _
from django.db.models import Model, ForeignKey, OneToOneField, CASCADE
from django.db.models import CharField, BooleanField, URLField, PositiveIntegerField, DateTimeField, DateField, DecimalField, FloatField
from django.contrib.auth.models import AbstractUser


class Edital(Model):
    PERIODO = (
        (1, '1º Período'),
        (2, '2º Período'),
    )

    tipo = CharField('Tipo', max_length=100, help_text='Discente/Bolsista')
    programa = CharField('Programa', max_length=100)
    numero = CharField('Número', max_length=50, null=True, blank=True)
    siglaUO = CharField('Unidade organizacional', max_length=100, help_text='Ex.: DG-EAD/IFRN')
    linkEdital = URLField('URL', max_length=300, help_text='Informe o LINK onde está o edital')
    grupo = CharField('Grupo', max_length=200, null=True)
    descricao = CharField('Descrição', max_length=300)
    ano = PositiveIntegerField('Ano', help_text='Digite o ano')
    periodo = PositiveIntegerField('Período letivo', choices=PERIODO)
    data_publicacao = DateTimeField('Data de publicação')

    def __str__(self):
        return self.tipo


class Pagamento(Model):
    existe_taxa = BooleanField(default=False)
    valor_taxa = DecimalField(max_digits=7, decimal_places=2)
    vencimento_boleto = DateField()
    edital = OneToOneField(Edital,on_delete=CASCADE)

    def __str__(self):
        return "Pagamento"


class Vaga(Model):
    curso = CharField('Curso', max_length=200)
    vaga = CharField('Vaga', max_length=100)
    numero_vagas = PositiveIntegerField('Número de vagas')
    edital = ForeignKey(Edital, on_delete=CASCADE)

    def __str__(self):
        return self.curso


class Usuario(AbstractUser):
    username = CharField(_('username'), max_length=150, primary_key=True)
    is_active = BooleanField(_('is active'), default=True)
    is_staff = BooleanField(_('staff status'), default=True)
    is_superuser = BooleanField(_('superuser status'), default=False)

    class Meta:
        verbose_name = _('User')
        verbose_name_plural = _('Users')

    def __str__(self):
        return self.username


class Coordenador(Model):
    usuario = ForeignKey(Usuario, on_delete=CASCADE)
    edital = ForeignKey(Edital, on_delete=CASCADE)

    def __str__(self):
        return "coordenador"


class Fase(Model):
    CLASSIFICACAO = (
        (1, 'Eliminatória'),
        (2, 'Classificatória'),
    )

    nome =CharField('Nome', max_length=200)
    tipo_classificacao = PositiveIntegerField('Tipo de classificação', choices=CLASSIFICACAO)
    aproveitamento_min = PositiveIntegerField('Aproveitamento mínimo', help_text='Nota necessária para passar')
    fator_habilitacao = PositiveIntegerField('Fator habilitação', help_text='Quantidade máxima de cadidatos que serão selecionados')
    edital = ForeignKey(Edital, on_delete=CASCADE)

    def __str__(self):
        return self.nome


class Cronograma(Model):
    etapa = CharField('Etapa', max_length=200)
    marco = CharField('Marco', max_length=200)
    inicio = DateField('Data Inicial')
    fim = DateField('Data Final')
    fase = OneToOneField(
        Fase,
        on_delete=CASCADE,
    )

    def __str__(self):
        return self.etapa


class Documento(Model):
    nome = CharField('Nome', max_length=200)
    fase = ForeignKey(Fase, on_delete=CASCADE)

    def __str__(self):
        return self.nome


class Avaliador(Model):
    usuario = ForeignKey(Usuario, on_delete=CASCADE)
    fase = ForeignKey(Fase, on_delete=CASCADE)

    def __str__(self):
        return "Avaliador"


class CriterioAvaliacao(Model):
    descricao = CharField('Nome', max_length=200)
    nota_minima = FloatField('Nota Mínima')
    nota_maxima = FloatField('Nota Maxima')
    ajuda_avaliador = CharField('Nome', max_length=500)
    incremento_nota = PositiveIntegerField('Incremento da Nota')
    fase = ForeignKey(Fase, on_delete=CASCADE)

    def __str__(self):
        return self.descricao


class MotivoNotaZero(Model):
    descriaco = CharField('Descrição', max_length=200, help_text='Exemplo: Inscrição sem anexos')
    fase = ForeignKey(Fase, on_delete=CASCADE)

    def __str__(self):
        return self.descricao


# por enquanto vai ficar internamente, pois essa classe não está nas telas
class EstrategiaClassificacao(Model):
    descriaco = CharField('Descrição', max_length=200, help_text='Exemplo: Inscrição sem anexos')
    fase = ForeignKey(Fase, on_delete=CASCADE)

    def __str__(self):
        return self.descricao
