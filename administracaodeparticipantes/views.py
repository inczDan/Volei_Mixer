from multiprocessing import context
from django.shortcuts import render
from .models import CadastrarParticipantes, CadastrarPartipantesForms


def create(request):

    context = {}
    if request.method == 'POST':
        form = CadastrarPartipantesForms(request.POST)
        if not form.is_valid():
            raise RuntimeError("algo errado, arruma esta resposta aqui")
        form.save()
        context['participantes'] = [p for p in CadastrarParticipantes.objects.all()]

    context['form'] = CadastrarPartipantesForms()
    return render(request, 'administracao.html', context)
