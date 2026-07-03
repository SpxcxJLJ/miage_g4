from django import forms

from .models import Composition
from .models import CompositionDetail


class CompositionForm(forms.ModelForm):

    class Meta:

        model = Composition

        fields = [
            "intitule_action",
            "lieu",
            "niveau",
            "public",
            "effectif",
            "date_debut",
            "date_fin",
        ]


class CompositionDetailForm(forms.ModelForm):

    class Meta:

        model = CompositionDetail

        fields = [
            "enseignant_id",
            "code_matiere",
            "semestre",
            "volume_horaire",
            "heures_enseignement",
            "heures_greta",
            "heures_service",
            "ordre",
        ]