from django.db import models


hability_value = (
    (1, 'Excelente(1)'),
    (2, 'Bom(2)'),
    (3, 'Intermediário(3)'),
    (4, 'Em desenvolvimento(4)'),
)


class Participante(models.Model):
    nome = models.CharField(max_length=20)
    sobrenome = models.CharField(max_length=20)
    habilidade = models.IntegerField(choices=hability_value)

    def __str__(self):
        return self.nome
    
    @property
    def habilidade_str(self):
        h = [text for (idx, text) in hability_value if idx == self.habilidade]
        return h[0]
