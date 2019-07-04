from django import forms
from .models import Edital, Vaga, Coordenador



class RegistrarEditalForm(forms.Form):

    def __init__(self,  *args, **kwargs):
        super(RegistrarEditalForm, self).__init__(*args, **kwargs)
        self.sem_erro = True

    def is_valid(self):
        if not super(RegistrarEditalForm, self).is_valid():
            self.adiciona_erro('Por favor, verifique os dados informados')


        # if not Usuario.objects.filter(cpf=self.data['cpf']).exists():
        #     self.adiciona_erro("Não existe cadastro com o CPF informado.")

        return self.sem_erro

    def adiciona_erro(self, message):
        errors = self._errors.setdefault(forms.forms.NON_FIELD_ERRORS, forms.utils.ErrorList())
        errors.append(message)
        self.sem_erro = False



# class EditalForm(forms.ModelForm):
#
#     class Meta:
#         model = Edital
#         fields = ['tipo', 'programa', 'numero', 'siglaUO','linkEdital','grupo', 'descricao', 'ano', 'periodo', 'data_publicacao', 'existe_taxa', 'valor_taxa', 'vencimento_boleto']
#
#
# # class PagamentoForm(forms.ModelForm):
# #     class Meta:
# #         model = Pagamento
# #         fields = ['existe_taxa', 'valor_taxa', 'vencimento_boleto']
#
# class VagaForm(forms.ModelForm):
#     class Meta:
#         model = Vaga
#         fields = '__all__'
#
# class CoordenadorForm(forms.ModelForm):
#     class Meta:
#         model = Coordenador
#         fields = ['usuario']