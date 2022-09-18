from django.db import models

class Catalogo(models.Model):
    filme = models.CharField(max_length=60)
    ano = models.BigIntegerField(max_length=8)
    diretor = models.CharField(max_length=40)
    comentarios = models.TextField()
    data_publicacao = models.DateField(auto_now_add=True)

