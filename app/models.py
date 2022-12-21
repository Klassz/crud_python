from django.db import models

class Membros(models.Model):
    nome = models.CharField(max_length=100)
    cargo = models.CharField(max_length=100)
    linguagem = models.CharField(max_length=100)

