from django.shortcuts import render
from .models import ProjetoDjango
from .forms import UserForm
# Create your views here.


def homepage(request):
    return render(
        request=request,
        template_name="home.html",
        context={"Filmes": ProjetoDjango.objects.all}

    )

def formulario(request):
    submibutton = request.POST.get("submit")

    conteudo = str
    observacao = str

    form = UserForm(request.POST or None)
    if form.is_valid():
        conteudo = form.cleaned_data.get("conteudo")
        observacao = form.cleaned_data.get("observacao")

    context = {'form': form, 'conteudo': conteudo, 'observacao': observacao,
               'submitbutton': submibutton}

    return render(
        request=request,
        template_name="observacaoFilme.html",
        context=context
    )