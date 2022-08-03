from django import forms
from django.db import models
from django.forms import ModelForm

class CadastrarParticipantes(models.Model):
    nome = models.CharField(max_length=20)
    sobrenome = models.CharField(max_length=20)
    habilidade = models.IntegerField()

class CadastrarPartipantesForms(ModelForm):
    class Meta:
        model = CadastrarParticipantes
        fields = ['nome', 'sobrenome', 'habilidade']