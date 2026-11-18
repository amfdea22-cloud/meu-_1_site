from django.contrib import admin
from .models import Filme, Categoria, Projeto

class FilmeAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'ano', 'genero', 'nota', 'autor')
    list_filter = ('genero', 'ano')
    search_fields = ('titulo', 'autor', 'genero')

admin.site.register(Filme, FilmeAdmin)


class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ('nome',)

admin.site.register(Categoria, CategoriaAdmin)


class ProjetoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'data_criacao', 'categoria')
    list_filter = ('categoria', 'data_criacao')
    search_fields = ('nome', 'descricao')

admin.site.register(Projeto, ProjetoAdmin)