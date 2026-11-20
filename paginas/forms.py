from django import forms
from .models import Projeto, Categoria

class ProjetoForm(forms.ModelForm):
    class Meta:
        model = Projeto
        fields = ['nome','descricao', 'categoria']
        
class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nome']