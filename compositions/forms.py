from django import forms
from .models import Composition, CompositionDetail
from .external_api.enseignants import get_enseignants
from .external_api.matieres import get_matieres

class CompositionForm(forms.ModelForm):
    class Meta:
        model = Composition
        fields = '__all__'
        
    
class CompositionDetailForm(forms.ModelForm):
    enseignant_id = forms.ChoiceField(choices=[])
    matiere_id = forms.ChoiceField(choices=[])

    class Meta:
        model = CompositionDetail
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        enseignants = get_enseignants()
        self.fields["enseignant_id"].choices = [
            (e["id"], f"{e['nom']} {e['prenom']}") for e in enseignants
        ]
        matieres = get_matieres()
        self.fields["matiere_id"].choices = [
            (m["id"], f"{m['code_matiere']} - {m['intitule']}") for m in matieres
        ]
