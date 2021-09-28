from django import forms
from django.contrib.auth.forms import  UserCreationForm
from .models import UserOver


class User_ProfilesForm(UserCreationForm):
    """
        Esta clase permite crear un usuario a partir del modelo UserOver
    """
    class Meta:
        """
            Esta clase es un contenedor de los datos adjuntos al modelo UserOver
        """
        model = UserOver
        fields = [
            'first_name',
            'last_name',
            'email',
            'username',
            'password1',
            'password2',
            'formation',
        ]
    
    def __init__(self, *args):
        """
            Esta función permite crear un campo para elejir una formacion específica
        """
        super(User_ProfilesForm, self).__init__(*args)
        self.fields['formation'].empty_label = "select your formation"
        #self.fields['email'].required = False #in this way we can make unrequired certain field


class LoginForm(forms.Form):
    """
        Esta clase es un formulario para el inicio de sesión de los usuarios
    """
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class SearchForm(forms.Form):
    """
        Esta clase es un formulario para la busqueda de archivos
    """
    query = forms.CharField()