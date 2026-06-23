from django.db import models

class RapportEtudiant(models.Model):
    numero_etudiant = models.IntegerField()
    periode_debut = models.DateField()
    periode_fin = models.DateField()
    heures_totales = models.FloatField(default=0)

    def __str__(self):
        return f"Rapport étudiant {self.numero_etudiant}"


class RapportEnseignant(models.Model):
    id_enseignant = models.IntegerField()
    periode_debut = models.DateField()
    periode_fin = models.DateField()
    heures_totales = models.FloatField(default=0)

    def __str__(self):
        return f"Rapport enseignant {self.id_enseignant}"
