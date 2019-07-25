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



class RegistrarVagaForm(forms.Form):

    def __init__(self,  *args, **kwargs):
        super(RegistrarVagaForm, self).__init__(*args, **kwargs)
        self.sem_erro = True

    def is_valid(self):
        if not super(RegistrarVagaForm, self).is_valid():
            self.adiciona_erro('Por favor, verifique os dados informados')

        return self.sem_erro

    def adiciona_erro(self, message):
        errors = self._errors.setdefault(forms.forms.NON_FIELD_ERRORS, forms.utils.ErrorList())
        errors.append(message)
        self.sem_erro = False
