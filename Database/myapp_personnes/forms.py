from django import forms

class UploadFileForm(forms.Form):
    fichier = forms.FileField(label='Sélectionnez un fichier Excel ou CSV')
class RecherchePersonneForm(forms.Form):
    terme_recherche = forms.CharField(label='Recherche', max_length=100)