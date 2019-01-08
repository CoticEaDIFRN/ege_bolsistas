from django.shortcuts import render, redirect, render_to_response
from django.utils import timezone
from .forms import EditalForm, PagamentoForm, VagaForm, CoordenadorForm
from .models import Edital,Vaga
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required


@staff_member_required
def admin_dashboard(request):
    return render(request, 'cadastro_edital/dashboard.html')


def novoEdital(request):
    form1 = EditalForm()
    form2 = PagamentoForm()
    form3 = VagaForm()
    form4 = CoordenadorForm()
    return render(request, 'cadastroEdital/edital.html', {'form1': form1, 'form2': form2, 'form3': form3, 'form4': form4})


def list_Edital(request):
    #posts = Edital.objects.filter(published_date__lte=timezone.now()).order_by('data_publicacao')
    posts = Edital.objects.filter()
    return render(request, 'cadastroEdital/index.html', {'posts': posts})
