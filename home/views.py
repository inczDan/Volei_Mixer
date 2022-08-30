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


    """
                Niveis de habilidade:
(1 = muito bom | 2 = bom | 3 = razoavel  | 4 = em aprendizado)
------------------------------------------------------------------------"""
"""
{'nath': 1, 'bernardo': 1, 'denis': 2, 'aninha': 2,
                     'gi rosa': 2, 'vital': 1, 'marcelo': 1, 'math': 2,
                     'lu': 3, 'ana/gu': 2, 'mi': 3, 'gu gondim': 2, 'caue': 2,
                     'lari rizzo': 4, 'erle': 3, 'prata': 3, 'daniel': 2,
                     'marilia': 3, 'eliel': 2, 'lorrana': 4, 'amanda': 2,
                     'ingrid': 4, 'laura': 3, 'felipe': 2}
                     'Nicolle': 1 , 'Bernardo': 1,'Bia':2,'Denis':2,'Vital': 1,'Marcelo':1,'Math':2, 'lu': 3,
            'Mi Torres': 3,'Erle':3 ,'Prata':3 ,'Daniel':2,'Marilia':2,'Ingrid':4 ,'Gabriela':3 ,'Laura': 3,'Natan':3 ,
            'Eliel':2 ,'Lorrana':4 ,'Fabricio':1 ,'Gi Michelato':4 ,'Feza':2 ,'Edson':2
"""
