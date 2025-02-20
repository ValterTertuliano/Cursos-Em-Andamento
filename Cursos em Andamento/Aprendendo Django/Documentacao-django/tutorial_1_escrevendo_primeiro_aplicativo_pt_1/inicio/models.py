from django.db import models  # type: ignore
from django.utils import timezone  # type: ignore
import datetime


class Pergunta(models.Model):
    texto_pergunta = models.CharField(max_length=200)
    data_publicacao = models.DateTimeField("data de publicação")

    def __str__(self):
        return self.texto_pergunta

    def foi_publicada_recentemente(self):
        return self.data_publicacao >= timezone.now() - datetime.timedelta(days=1)


class Escolha(models.Model):
    pergunta = models.ForeignKey(Pergunta, on_delete=models.CASCADE)
    texto_escolha = models.CharField(max_length=200)
    votos = models.IntegerField(default=0)

    def __str__(self):
        return self.texto_escolha
