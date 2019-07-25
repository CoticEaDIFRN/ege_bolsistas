from django.shortcuts import render, redirect, render_to_response
from django.views.generic.base import View
from .forms import RegistrarEditalForm, RegistrarVagaForm
from .models import Edital,Vaga
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required



class RegistrarEditalView(View):
    template_name = 'cadastro_edital/edital.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        form = RegistrarEditalForm(request.POST)

        if form.is_valid():
            dados_form = form.data

            edital = Edital.objects.create(tipo=dados_form['tipo'],
                                           programa=dados_form['programa'],
                                           numero=dados_form['numero'],
                                           siglaUO=dados_form['siglaUO'],
                                           linkEdital=dados_form['linkEdital'],
                                           grupo=dados_form['grupo'],
                                           descricao=dados_form['descricao'],
                                           ano=dados_form['ano'],
                                           periodo=dados_form['periodo'],
                                           data_publicacao=dados_form['data_publicacao'])
                                           # existe_taxa=dados_form['existe_taxa'])
                                           # valor_taxa=dados_form['valor_taxa'],
                                           # vencimento_boleto=dados_form['vencimento_boleto'])




            return redirect('vaga')


        return render(request, self.template_name, {'form': form})



    def confirmarEdital(request):
        return render(request, 'cadastro_edital/confirmardados.html',
                      {'edital': Edital.objects.last()})

    def lista_editais(request):
        return render(request, 'cadastro_edital/listagem.html',
                      {'edital': Edital.objects.all()})




class RegistrarVagaView(View):
    template_name = 'cadastro_edital/vaga.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        form = RegistrarVagaForm(request.POST)

        if form.is_valid():
            dados_form = form.data

            vaga = Vaga.objects.create(curso=dados_form['curso'],
                                       vaga =dados_form['vaga'],
                                       numero_vagas = dados_form['numero_vagas'],
                                       edital = Edital.objects.last())


            return redirect('confirmar')


        return render(request, self.template_name, {'form': form})



    def confirmarVaga(request):
        return render(request, 'cadastro_edital/confirmardados.html', {'edital':Edital.objects.last(), 'vaga': Vaga.objects.last()})

    def lista_editais(request):
        return render(request, 'cadastro_edital/listagem.html',
                      {'edital': Edital.objects.all()})
