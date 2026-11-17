from django.db import models

class filme(models.Model):
    titulo = models.CharField(max_length=200)
    ano = models.IntegerField()
    genero = models.CharField(max_length=100)
    nota = models.FloatField()
    autor = models.CharField(max_length=100)
    
    def __str__(self):
        return self.titulo

class projeto(models.Model):
    nome = models.CharField(max_length=200)
    descricao = models.TextField()
    data_criacao = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.nome