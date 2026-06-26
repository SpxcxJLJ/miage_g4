from django.db import models

class Composition(models.Model):
    promotion = models.CharField(max_length=50)
    date_creation = models.DateField(auto_now_add=True)
    status = models.BooleanField(default=True)
    date_fin = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"Composition {self.promotion}"


class CompositionDetail(models.Model):
    composition = models.ForeignKey(
        Composition,
        on_delete=models.CASCADE,
        related_name="details"
    )

    # Données venant de l’API enseignants
    enseignant_id = models.IntegerField(
    null=True,
    blank=True
    )

    enseignant_nom = models.CharField(
    max_length=100,
    blank=True,
    null=True
    )
    enseignant_prenom = models.CharField(
    max_length=100,
    blank=True,
    null=True
    )
    statut = models.CharField(max_length=100, null=True, blank=True)
    raison_sociale = models.CharField(max_length=150, null=True, blank=True)
    ministere_collectivite = models.CharField(max_length=150, null=True, blank=True)

    # Données venant de l’API matières
    matiere_id = models.IntegerField(
    null=True,
    blank=True
    )

    code_matiere = models.CharField(
    max_length=20,
    null=True,
    blank=True
    )
    intitule_matiere = models.CharField(
    max_length=150,
    blank=True,
    null=True
    )
    volume_horaire = models.FloatField(default=0)

    # Données GRETA
    semestre = models.CharField(max_length=10, null=True, blank=True)
    heures_enseignement = models.FloatField(default=0)
    heures_greta = models.FloatField(default=0)
    heures_service = models.FloatField(default=0)

    ordre = models.IntegerField(default=0)

    class Meta:
        ordering = ["ordre"]


    def __str__(self):
        return f"Détail {self.id} - {self.composition}"
