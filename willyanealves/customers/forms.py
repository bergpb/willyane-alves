from django import forms
from django.forms.widgets import ClearableFileInput

class CustomersForm(forms.Form):
    SEX = [("Feminino", "Feminino"), ("Masculino", "Masculino")]
    CITIES = [("Natal", "Natal"), ("Parnamirim", "Parnamirim"), ("São Gonçalo do Amarante", "São Gonçalo do Amarante"), ("Extremoz", "Extremoz"), ("Ceará-Mirim", "Ceará-Mirim"),
              ("São José de Mipibu", "São José de Mipibu"), ("Outra", "Outra")]
    name = forms.CharField(label="Nome")
    last_name = forms.CharField(label="Sobrenome")
    cpf = forms.CharField(label="CPF", required=False)
    email = forms.EmailField(label="Email")
    phone = forms.CharField(label="Telefone")
    sex = forms.CharField(label="Sexo", widget=forms.Select(choices=SEX))
    address = forms.CharField(label="Endereço", required=False)
    city = forms.CharField(label="Cidade", widget=forms.Select(choices=CITIES))
    district =forms.CharField(label="Bairro", required=False)
    birth = forms.DateField(label="Data de nascimento", required=False)
    picture = forms.ImageField(label="Foto", required=False, widget=ClearableFileInput)
