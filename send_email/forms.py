from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    """Форма підписки по e-mail"""

    class Meta:
        model = Contact
        labels = {
            'name': "Ім'я користувача",
            'email': "Електронна адреса"
        }
        fields = '__all__'
