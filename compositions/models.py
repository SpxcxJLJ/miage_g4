from django.db import models

class Composition(models.Model):
    intitule_action = models.CharField(max_length=150)
    lieu = models.CharField(max_length=150)
    niveau = models.CharField(max_length=100)
    public = models.CharField(max_length=200)
    effectif = models.PositiveIntegerField(default=0)

    date_debut = models.DateField()
    date_fin = models.DateField()

    date_creation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.intitule_action


class CompositionDetail(models.Model):

    composition = models.ForeignKey(
        Composition,
        on_delete=models.CASCADE,
        related_name="details"
    )

    # API enseignants
    enseignant_id = models.IntegerField()
    enseignant_nom = models.CharField(max_length=100)
    enseignant_prenom = models.CharField(max_length=100)
    enseignant_email = models.CharField(max_length=150, blank=True, null=True)
    enseignant_telephone = models.CharField(max_length=50, blank=True, null=True)
    statut = models.CharField(max_length=100, blank=True, null=True)
    raison_sociale = models.CharField(max_length=150, blank=True, null=True)
    ministere_collectivite = models.CharField(max_length=150, blank=True, null=True)

    # API matières
    code_matiere = models.CharField(max_length=40)
    intitule_matiere = models.CharField(max_length=150, blank=True, null=True)
    volume_horaire = models.DecimalField(max_digits=5, decimal_places=1, default=0)

    # GRETA
    semestre = models.CharField(max_length=10, blank=True)
    heures_enseignement = models.DecimalField(max_digits=5, decimal_places=1, default=0)
    heures_greta = models.DecimalField(max_digits=5, decimal_places=1, default=0)
    heures_service = models.DecimalField(max_digits=5, decimal_places=1, default=0)

    ordre = models.PositiveIntegerField(default=1)

    class Meta:
        ordering = ["ordre"]

    def __str__(self):
        return f"{self.enseignant_nom} {self.enseignant_prenom} - {self.intitule_matiere}"

  