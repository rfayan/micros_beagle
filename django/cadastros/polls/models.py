from django.db import models

# Create your models here.
class Morador(models.Model):
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=11)
    endereco = models.CharField(max_length=100)
    telefone = models.CharField(max_length=15)

    def __str__(self):
        return self.cpf
