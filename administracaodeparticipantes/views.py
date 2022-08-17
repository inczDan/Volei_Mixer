from multiprocessing import context
from django.shortcuts import render

from .forms import CadastrarPartipantesForms
from .service import lista_participantes

def create(request):
    context = {}
    if request.method == 'POST':
        form = CadastrarPartipantesForms(request.POST)
        if not form.is_valid():
            raise RuntimeError("Dados inválidos!")
        form.save()

    context['participantes'] = lista_participantes()
    context['form'] = CadastrarPartipantesForms()
    return render(request, 'administracao.html', context)
