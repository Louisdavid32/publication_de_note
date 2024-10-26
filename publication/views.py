from django.shortcuts import render, redirect, get_object_or_404
from .models import Etudiant, Note, UE, EC,Niveau, Filiere
from .forms import EtudiantForm, NoteForm,UploadFileForm
from django.http import HttpResponse
import pandas as pd




def liste_etudiants(request):
    if request.method == 'POST':
        form = EtudiantForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('liste_etudiants')
    else:
        form = EtudiantForm()
    etudiants = Etudiant.objects.all()
    return render(request, 'notes/liste_etudiants.html', {'etudiants': etudiants, 'form': form})

def detail_notes(request, etudiant_id):
    etudiant = get_object_or_404(Etudiant, pk=etudiant_id)
    notes = Note.objects.filter(etudiant=etudiant).select_related('ec', 'ec__ue')
    return render(request, 'notes/detail_notes.html', {'etudiant': etudiant, 'notes': notes})

def ajouter_etudiant(request):
    if request.method == 'POST':
        form = EtudiantForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('liste_etudiants')
    else:
        form = EtudiantForm()
    return render(request, 'notes/ajouter_etudiant.html', {'form': form})

def modifier_etudiant(request, etudiant_id):
    etudiant = get_object_or_404(Etudiant, pk=etudiant_id)
    if request.method == 'POST':
        form = EtudiantForm(request.POST, instance=etudiant)
        if form.is_valid():
            form.save()
            return redirect('liste_etudiants')
    else:
        form = EtudiantForm(instance=etudiant)
    return render(request, 'notes/modifier_etudiant.html', {'form': form})

def supprimer_etudiant(request, etudiant_id):
    etudiant = get_object_or_404(Etudiant, pk=etudiant_id)
    if request.method == 'POST':
        etudiant.delete()
        return redirect('liste_etudiants')
    return render(request, 'notes/supprimer_etudiant.html', {'etudiant': etudiant})

def ajouter_note(request, etudiant_id):
    etudiant = get_object_or_404(Etudiant, pk=etudiant_id)
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            note.etudiant = etudiant
            note.save()
            return redirect('detail_notes', etudiant_id=etudiant_id)
    else:
        form = NoteForm()
    return render(request, 'notes/ajouter_note.html', {'form': form, 'etudiant_id': etudiant_id})

def modifier_note(request, note_id):
    note = get_object_or_404(Note, pk=note_id)
    if request.method == 'POST':
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect('detail_notes', etudiant_id=note.etudiant.id)
    else:
        form = NoteForm(instance=note)
    return render(request, 'notes/modifier_note.html', {'form': form})

def supprimer_note(request, note_id):
    note = get_object_or_404(Note, pk=note_id)
    if request.method == 'POST':
        note.delete()
        return redirect('detail_notes', etudiant_id=note.etudiant.id)
    return render(request, 'notes/supprimer_note.html', {'note': note})



def importer_etudiants(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            fichier_excel = request.FILES['fichier']
            df = pd.read_excel(fichier_excel)

            # Vérifier si les colonnes nécessaires sont présentes dans le fichier Excel
            colonnes_requises = ['matricule', 'nom_etudi', 'password', 'FILIERE', 'type_cours']
            if not all(colonne in df.columns for colonne in colonnes_requises):
                return HttpResponse("Le fichier Excel ne contient pas toutes les colonnes nécessaires.")

            for index, row in df.iterrows():
                # Créer ou mettre à jour l'étudiant
                niveau, created = Niveau.objects.get_or_create(nom=row['FILIERE'])
                filiere, created = Filiere.objects.get_or_create(nom=row['FILIERE'])
                etudiant, created = Etudiant.objects.update_or_create(
                    matricule=row['matricule'],
                    defaults={
                        'nom': row['nom_etudi'],
                        'niveau': niveau,
                        'filiere': filiere,
                        'formation': row['type_cours'],
                    }
                )

            return redirect('liste_etudiants')
    else:
        form = UploadFileForm()
    return render(request, 'notes/importer_etudiants.html', {'form': form})

def exporter_etudiants(request):
    # Récupérer les données des étudiants
    etudiants = Etudiant.objects.all().select_related('niveau', 'filiere')

    # Créer un DataFrame pandas
    data = []
    for etudiant in etudiants:
        data.append({
            'Matricule': etudiant.matricule,
            'Nom': etudiant.nom,
            'Nom etudi': etudiant.nom_etudi,
            'Mot de passe': etudiant.password,
            'Niveau': etudiant.niveau.nom,
            'Filière': etudiant.filiere.nom,
            'Type de cours': etudiant.type_cours,
            'Moyenne': etudiant.obtenir_moyenne(),
        })
    df = pd.DataFrame(data)

    # Générer le fichier Excel
    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename="etudiants.xlsx"'
    df.to_excel(response, index=False, engine='openpyxl')
    return response