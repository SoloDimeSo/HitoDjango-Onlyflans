from django import forms
from .models import Contacto




class TextInputWidget(forms.TextInput):
    def __init__(self, *args, **kwargs):
        kwargs['attrs'] = {'type': 'text'}
        super().__init__(*args, **kwargs)

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contacto
        fields = ['customer_name','customer_email','message']
        widgets = {
            'customer_email': TextInputWidget(),  # Usa el widget personalizado
        }
        labels = {
            'customer_name' : 'Nombre del cliente: ',
            'customer_email' : 'Correo del cliente: ',
            'message' : 'Motivo de su mensaje: '
        }