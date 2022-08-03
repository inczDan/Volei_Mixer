from django.shortcuts import render
from .models import CadastrarParticipantes


def crud(request):
    return render(request, 'administracao.html')
