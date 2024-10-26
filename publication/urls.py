from django.urls import path
from . import views

"""urlpatterns = [
    path('etudiants/', views.liste_etudiants, name='liste_etudiants'),
    path('etudiants/<int:etudiant_id>/', views.detail_notes, name='detail_notes'),
    path('etudiants/ajouter/', views.ajouter_etudiant, name='ajouter_etudiant'),
    path('etudiants/<int:etudiant_id>/modifier/', views.modifier_etudiant, name='modifier_etudiant'),
    path('etudiants/<int:etudiant_id>/supprimer/', views.supprimer_etudiant, name='supprimer_etudiant'),
    path('etudiants/<int:etudiant_id>/ajouter_note/', views.ajouter_note, name='ajouter_note'),
    path('notes/<int:note_id>/modifier/', views.modifier_note, name='modifier_note'),
    path('notes/<int:note_id>/supprimer/', views.supprimer_note, name='supprimer_note'),
    
]"""

urlpatterns = [
    path('etudiants/', views.liste_etudiants, name='liste_etudiants'),
    path('etudiants/<int:etudiant_id>/', views.detail_notes, name='detail_notes'),
    path('etudiants/ajouter/', views.ajouter_etudiant, name='ajouter_etudiant'),
    path('etudiants/<int:etudiant_id>/modifier/', views.modifier_etudiant, name='modifier_etudiant'),
    path('etudiants/<int:etudiant_id>/supprimer/', views.supprimer_etudiant, name='supprimer_etudiant'),
    path('etudiants/<int:etudiant_id>/ajouter_note/', views.ajouter_note, name='ajouter_note'),
    path('notes/notes/<int:note_id>/modifier/', views.modifier_note, name='modifier_note'),
    path('notes/<int:note_id>/supprimer/', views.supprimer_note, name='supprimer_note'),
    path('importer/', views.importer_etudiants, name='importer_etudiants'),
    path('exporter/', views.exporter_etudiants, name='exporter_etudiants'),
]