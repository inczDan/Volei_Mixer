from .models import Participante

def lista_participantes():
    return [{
        'nome': p.nome,
        'sobrenome': p.sobrenome,
        'habilidade': p.habilidade,
    } for p in Participante.objects.all()]
