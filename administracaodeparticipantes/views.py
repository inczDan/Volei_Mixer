from multiprocessing import context
from django.shortcuts import render
from models import Participante
from .forms import CadastrarPartipantesForms

def create(request):
    context = {}
    if request.method == 'POST':
        form = CadastrarPartipantesForms(request.POST)
        if not form.is_valid():
            raise RuntimeError("Dados inválidos!")
        form.save()

    context['participantes'] = [p for p in Participante.objects.all()]
    context['form'] = CadastrarPartipantesForms()
    return render(request, 'administracao.html', context)
