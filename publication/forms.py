from django import forms
from .models import Etudiant, Note

class EtudiantForm(forms.ModelForm):
    class Meta:
        model = Etudiant
        fields = ['matricule', 'nom', 'niveau', 'filiere', 'formation']

class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['ec', 'cc1', 'cc2', 'cc3', 'session_normale', 'session_avant']


class UploadFileForm(forms.Form):
    fichier = forms.FileField()