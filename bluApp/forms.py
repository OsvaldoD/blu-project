from django import forms
from django.forms import ModelForm
from bluApp.models import Credito, Message


class AplicaCreditoForm(ModelForm):
    class Meta:
        model = Credito
        fields = ['nome','apelido','contacto','email','nome_empresa','numero_conta'

        ]

class MessageForm(ModelForm):
    class Meta:
        model = Message
        fields = ['categoria', 'message']