from django.db import models

class Niveau(models.Model):
    nom = models.CharField(max_length=255)

    def __str__(self):
        return self.nom

class Filiere(models.Model):
    nom = models.CharField(max_length=255)

    def __str__(self):
        return self.nom

class UE(models.Model):
    code_ue = models.CharField(max_length=255)
    nom_ue = models.CharField(max_length=255)
    niveau = models.ForeignKey(Niveau, on_delete=models.CASCADE)
    filiere = models.ForeignKey(Filiere, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.code_ue} - {self.nom_ue}"
    
    

class Etudiant(models.Model):
    matricule = models.CharField(max_length=255, unique=True)
    nom = models.CharField(max_length=255)
    niveau = models.ForeignKey(Niveau, on_delete=models.CASCADE)
    filiere = models.ForeignKey(Filiere, on_delete=models.CASCADE)
    formation = models.IntegerField(choices=[(1, 'Cours du jour'), (2, 'Cours du soir')])

    def __str__(self):
        return f"{self.matricule} - {self.nom}"

    def obtenir_moyenne(self):
        notes = self.note_set.all()
        if not notes:
            return 0
        total_notes = 0
        total_coefficients = 0
        for note in notes:
            notes_ec = [note.cc1, note.cc2, note.cc3, note.session_normale, note.session_avant]
            notes_ec = [n for n in notes_ec if n is not None]
            if notes_ec:
                moyenne_ec = sum(notes_ec) / len(notes_ec)
                total_notes += moyenne_ec
                total_coefficients += 1
        return total_notes / total_coefficients if total_coefficients else 0
    


class EC(models.Model):
    code_ec = models.CharField(max_length=255)
    nom_ec = models.CharField(max_length=255)
    ue = models.ForeignKey(UE, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.code_ec} - {self.nom_ec}"

class Note(models.Model):
    etudiant = models.ForeignKey(Etudiant, on_delete=models.CASCADE)
    ec = models.ForeignKey(EC, on_delete=models.CASCADE)
    cc1 = models.FloatField(null=True, blank=True)
    cc2 = models.FloatField(null=True, blank=True)
    cc3 = models.FloatField(null=True, blank=True)
    session_normale = models.FloatField(null=True, blank=True)
    session_avant = models.FloatField(null=True, blank=True)

    def __str__(self):
        return f"Note de {self.etudiant} pour {self.ec}"