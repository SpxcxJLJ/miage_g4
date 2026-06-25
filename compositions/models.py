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

    enseignant_api_id = models.IntegerField()
    matiere_api_id = models.IntegerField()
    heures_enseignement = models.FloatField(default=0)
    heures_greta = models.FloatField(default=0)
    heures_service = models.FloatField(default=0)

    ordre = models.IntegerField(default=0)

    class Meta:
        ordering = ['ordre']


    def __str__(self):
        return f"Détail {self.id} - {self.composition}"
