from django import forms
from .models import Composition, CompositionDetail

class CompositionForm(forms.ModelForm):
    class Meta:
        model = Composition
        fields = '__all__'
        
    
class CompositionDetailForm(forms.ModelForm):
    class Meta:
        model = CompositionDetail
        fields = '__all__'
