from django.forms import ModelForm
from .models import Participante


class CadastrarPartipantesForms(ModelForm):
    class Meta:
        model = Participante
        fields = ['nome', 'sobrenome', 'habilidade']
