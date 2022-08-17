from django.shortcuts import render
from administracaodeparticipantes.models import Participante

# Create your views here.
def home(request):
    return render(request, 'home.html')


def jogador(request):
    nome = [n for n in Participante.objects.all().only("nome")]
    sobrenome = [s for s in Participante.objects.all().only("sobrenome")]
    habilidade = [h for h in Participante.objects.all().only("habilidade")]
    context = {
        'nome': nome,
        'sobrenome': sobrenome,
        'habilidade':  habilidade,
    }
    return render(request, context)