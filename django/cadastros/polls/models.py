from django.db import models

# Create your models here.
class Morador(models.Model):
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=11)
    endereco = models.CharField(max_length=100)
    telefone = models.CharField(max_length=15)

    def __str__(self):
        return self.cpf


class Usuario(models.Model):
    login = models.CharField(max_length=30)
    senha = models.CharField(max_length=30)
    morador = models.ForeignKey(Morador, on_delete=models.CASCADE)

    def __str__(self):
        return self.login

class Evento(models.Model):
    titulo = models.CharField(max_length=40)
    horario_inicio = models.DateTimeField('Horario de Inicio')
    horario_final = models.DateTimeField('Horario de Termino')
    horario_entrada = models.DateTimeField('Horario Máximo de Entrada')
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo


class Convidado(models.Model):
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=11)
    endereco = models.CharField(max_length=100)
    eventos = models.ManyToManyField(Evento)

    def __str__(self):
        return self.nome


class Veiculo(models.Model):
    placa = models.CharField(max_length=8)
    modelo = models.CharField(max_length=30)
    marca = models.CharField(max_length=30)
    cor_principal = models.CharField(max_length=30)
    cor_secundaria = models.CharField(max_length=30)
    convidado = models.ForeignKey(Convidado, on_delete=models.CASCADE)

    def __str__(self):
        return self.placa


