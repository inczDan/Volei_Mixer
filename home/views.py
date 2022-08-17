from cgitb import reset
from django.shortcuts import render
from administracaodeparticipantes.models import Participante
import random
import string

# Create your views here.
def home(request):
    return render(request, 'home.html')


def jogador(request):
    participantes = Participante.objects.all().values('nome', 'sobrenome', 'habilidade')
    dicionario = {}
    for p in participantes:
        dicionario[p['nome']] = p['habilidade']
    
    times = [[], [], [], []]
    jogadores_ordenados = sorted(
        list(dicionario.items()),
        key=lambda item: item[1]
    )
    for t in range(4):
        jogador = jogadores_ordenados.pop(0)
        times[t].append(jogador)

    pudim = [0, 1, 2, 3]
    while not all(len(time) == 6 for time in times):
        random.shuffle(pudim)
        for t in pudim:
            jogador = jogadores_ordenados.pop(0)
            times[t].append(jogador)

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



# EM_APRENDIZADO = 4
# RAZOVEL = 3
# BOM = 2
# MUITO_BOM = 1

# jogadores = {'Ana/Gu':2,'Aninha':1,'Daniel':1,'Erle':3,'Gi Rosa':2,'Ingrid':4,'Laura':2,'Lorrana':4,'Lu del Grande':2,'Mi Torres':3,'Nath':1,'Prata':3,'Vital':1,'Vitor': 1,'Edson': 1,'Iuri': 2,'Bia': 3,'Clara (irmã Bia)': 4,'Hiago': 1,'Vinicius Girotto (Bia)': 2,'Davi (Bia)':4,'aa':4, 'bb':4, 'cc':4}


