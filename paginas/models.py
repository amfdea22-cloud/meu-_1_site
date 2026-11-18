from django.db import models

class Filme(models.Model):
    titulo = models.CharField(max_length=200)
    ano = models.IntegerField()
    genero = models.CharField(max_length=100)
    nota = models.FloatField()
    autor = models.CharField(max_length=100)
    
    def __str__(self):
        return self.titulo


class Categoria(models.Model):
    nome = models.CharField(max_length=100)
    
    def __str__(self):
        return self.nome


class Projeto(models.Model):
    nome = models.CharField(max_length=200)
    descricao = models.TextField()
    data_criacao = models.DateField(auto_now_add=True)
    categoria = models.ForeignKey(
        Categoria, 
        on_delete=models.SET_NULL,
        null=True, blank=True
    )
    
    def __str__(self):
        return self.nome