from django import forms

class PasswordForm(forms.Form):
    majuscules = forms.BooleanField(required=False,initial=False)
    minuscules = forms.BooleanField(required=False,initial=False)
    chiffres = forms.BooleanField(required=False,initial=False)
    speciaux = forms.BooleanField(required=False,initial=False)
    nbreCaractere = forms.IntegerField(max_value = 30) 