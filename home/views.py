from django.shortcuts import render

from administracaodeparticipantes.models import Participante
from . import gerador_times


def jogador(request):

    if request.method == 'GET':
        participantes = Participante.objects.all().order_by('nome')
        context = {
            'participantes': participantes,
            'times': []
        }
        return render(request, 'home.html', context)

    players_ids = dict(request.POST)['players']
    participantes = Participante.objects.filter(id__in=players_ids).values('nome', 'sobrenome', 'habilidade')
    times = gerador_times.montar_time(participantes)

    context = {
        'participantes': participantes,
        'times': times
    }
    return render(request, 'home.html', context)

