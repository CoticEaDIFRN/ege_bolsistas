from django import forms
from .models import Edital, Vaga, Coordenador

class EditalForm(forms.ModelForm):

    class Meta:
        model = Edital
        fields = ['tipo', 'programa', 'numero', 'siglaUO','linkEdital','grupo', 'descricao', 'ano', 'periodo', 'data_publicacao', 'existe_taxa', 'valor_taxa', 'vencimento_boleto']


# class PagamentoForm(forms.ModelForm):
#     class Meta:
#         model = Pagamento
#         fields = ['existe_taxa', 'valor_taxa', 'vencimento_boleto']

class VagaForm(forms.ModelForm):
    class Meta:
        model = Vaga
        fields = '__all__'

class CoordenadorForm(forms.ModelForm):
    class Meta:
        model = Coordenador
        fields = ['usuario']