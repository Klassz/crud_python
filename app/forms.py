from django.forms import ModelForm
from app.models import Membros

class MembrosForm(ModelForm):
    class Meta:
        model = Membros
        fields =['nome','cargo','linguagem']