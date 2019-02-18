from django.shortcuts import render, redirect, render_to_response
from django.utils import timezone
from .forms import EditalForm, VagaForm, CoordenadorForm
from .models import Edital,Vaga
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required


@staff_member_required
def admin_dashboard(request):
    return render(request, 'cadastro_edital/dashboard.html')


def novoEdital(request):


    if request.method == "POST":
        form1 = EditalForm(request.POST)
        form2 = VagaForm(request.POST)
        form3 = CoordenadorForm(request.POST)
        if form1.is_valid() and form2.is_valid() and form3.is_valid():
            form1.save()
            form2.save()
            form3.save()
            return redirect('edital_detail')

    else:
        form1 = EditalForm()
        form2 = VagaForm()
        form3 = CoordenadorForm()

    return render(request, 'cadastroEdital/edital.html', {'form1': form1, 'form2': form2, 'form3': form3})


def list_Edital(request):
    #posts = Edital.objects.filter(published_date__lte=timezone.now()).order_by('data_publicacao')
    posts = Edital.objects.filter()
    return render(request, 'cadastroEdital/index.html', {'posts': posts})

def new_edital(request):
    if request.method == "POST":
        form = EditalForm(request.POST)
        if form.is_valid():
            edital = form.save(commit=False)
            edital.save()
            return redirect('edital_detail', pk=edital.pk)
    else:
        form = EditalForm()
    return render(request, 'blog/post_edit.html', {'form': form})