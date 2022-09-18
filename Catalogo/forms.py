from django.forms import ModelForm
from .models import Catalogo

class Formulariocatalogo(ModelForm):
    
    class Meta:
        model = Catalogo
        fields = ['filme', 'ano', 'diretor', 'comentarios']