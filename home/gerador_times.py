import random

# EM_APRENDIZADO = 4
# RAZOVEL = 3
# BOM = 2
# MUITO_BOM = 1


def montar_time(participantes, aleatoriedade=None):

    numero_times = round(len(participantes)/6)
    print('--------->1', numero_times)
    # travas:
    # - menos que 8 gera mensagem de erro
    # - teste com 11, auto completar até chegar em multiplo de 6

    # faz cópia para nao ter queryset (GAMBI BRABA), remover
    participantes = [
        {
            'nome': item['nome'],
            'sobrenome': item['sobrenome'],
            'habilidade': item['habilidade']
        } for item in participantes]


    if len(participantes) != 24:
        numero_times = 2
    if aleatoriedade:
        random.seed(aleatoriedade)

    total_esperado = numero_times * 6
    if len(participantes) < total_esperado:
        for item in range(total_esperado-len(participantes)):
            participantes.append({'nome': '👻', 'sobrenome': '👻', 'habilidade': 5})

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
