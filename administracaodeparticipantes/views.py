from django.shortcuts import render
from .models import CadastrarParticipantes
from django.views.generic.list import ListView


class Crud(ListView):
    model: CadastrarParticipantes
    template_name = 'administracao.html'


    def get_queryset(self):
        participantes = CadastrarParticipantes.objects.all()
        context = {
            'participantes': participantes
        }
        return context
