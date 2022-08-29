import random

# EM_APRENDIZADO = 4
# RAZOVEL = 3
# BOM = 2
# MUITO_BOM = 1
# jogadores = {'Ana/Gu':2,'Aninha':1,'Daniel':1,'Erle':3,'Gi Rosa':2,'Ingrid':4,'Laura':2,'Lorrana':4,'Lu del Grande':2,'Mi Torres':3,'Nath':1,'Prata':3,'Vital':1,'Vitor': 1,'Edson': 1,'Iuri': 2,'Bia': 3,'Clara (irmã Bia)': 4,'Hiago': 1,'Vinicius Girotto (Bia)': 2,'Davi (Bia)':4,'aa':4, 'bb':4, 'cc':4}


def montar_time(participantes, aleatoriedade=None, numero_times:int = 4):

    if len(participantes) != 24:
        numero_times = 2
    if aleatoriedade:
        random.seed(aleatoriedade)

    dicionario = {}
    for p in participantes:
        dicionario[p['nome']] = p['habilidade']
    
    times = []
    for i in range (numero_times):
        times.append([])

    jogadores_ordenados = sorted(
        list(dicionario.items()),
        key=lambda item: item[1]
    )
    for t in range(0, numero_times):
        jogador = jogadores_ordenados.pop(0)
        times[t].append(jogador)

    numero_participante = [item for item in range(0, numero_times)]

    while not all(len(time) == 6 for time in times):
        random.shuffle(numero_participante)
        for t in numero_participante:
            jogador = jogadores_ordenados.pop(0)
            times[t].append(jogador)

    return times
