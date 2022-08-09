from tkinter import CASCADE
from django import forms
from django.db import models
from django.forms import ModelForm

hability_value = (
    (1, 'Excelente(1)'),
    (2, 'Bom(2)'),
    (3, 'Intermediário(3)'),
    (4, 'Em desenvolvimento(4)'),
)

# renomear para Participante
class CadastrarParticipantes(models.Model):
    nome = models.CharField(max_length=20)
    sobrenome = models.CharField(max_length=20)
    habilidade = models.IntegerField(choices=hability_value)

    def __str__(self):
        return self.nome
    
    @property
    def habilidade_str(self):
        h = [text for (idx, text) in hability_value if idx == self.habilidade]
        return h[0]


# isto deveria estar no forms.py TIRAR DAQUI
class CadastrarPartipantesForms(ModelForm):
    class Meta:
        model = CadastrarParticipantes
        fields = ['nome', 'sobrenome', 'habilidade']
