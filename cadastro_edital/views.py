from django.shortcuts import render, redirect, render_to_response
from django.views.generic.base import View
from .forms import RegistrarEditalForm
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
            # edital = Edital.objects.get(cpf=dados_form['cpf'])
            edital = Edital.objects.create(tipo=dados_form['tipo'],
                                           programa=dados_form['programa'],
                                           numero=dados_form['numero'],
                                           siglaUO=dados_form['siglaUO'],
                                           linkEdital=dados_form['linkEdital'],
                                           grupo=dados_form['grupo'],
                                           descricao=dados_form['descricao'],
                                           ano=dados_form['ano'],
                                           periodo=dados_form['periodo'],
                                           data_publicacao=dados_form['data_publicacao'],
                                           existe_taxa=dados_form['existe_taxa'],
                                           valor_taxa=dados_form['valor_taxa'],
                                           vencimento_boleto=dados_form['vencimento_boleto'],)

            return redirect('confirmar')


        return render(request, self.template_name, {'form': form})


    def confirmarEdital(request):
        return render(request, 'cadastro_edital/confirmardados.html',
                      {'edital': Edital.objects.last()})

    def lista_editais(request):
        return render(request, 'cadastro_edital/listagem.html',
                      {'edital': Edital.objects.all()})



# def admin_dashboard(request):
#     return render(request, 'cadastro_edital/dashboard.html')
#
#
# def novoEdital(request):
#
#
#     if request.method == "POST":
#         form1 = EditalForm(request.POST)
#         form2 = VagaForm(request.POST)
#         form3 = CoordenadorForm(request.POST)
#         if form1.is_valid() and form2.is_valid() and form3.is_valid():
#             form1.save()
#             form2.save()
#             form3.save()
#             return redirect('edital_detail')
#
#     else:
#         form1 = EditalForm()
#         form2 = VagaForm()
#         form3 = CoordenadorForm()
#
#     return render(request, 'cadastro_edital/edital.html', {'form1': form1, 'form2': form2, 'form3': form3})
#
#
# def list_Edital(request):
#     #posts = Edital.objects.filter(published_date__lte=timezone.now()).order_by('data_publicacao')
#     posts = Edital.objects.filter()
#     return render(request, 'cadastro_edital/index.html', {'posts': posts})
#
# def new_edital(request):
#     if request.method == "POST":
#         form = EditalForm(request.POST)
#         if form.is_valid():
#             edital = form.save(commit=False)
#             edital.save()
#             return redirect('edital_detail', pk=edital.pk)
#     else:
#         form = EditalForm()
#     return render(request, 'blog/post_edit.html', {'form': form})