from django.shortcuts import render
from .models import CadastrarParticipantes
from django.views.generic.list import ListView


def create(request):
    playerid = int()
    return render(request, 'administracao.html')
