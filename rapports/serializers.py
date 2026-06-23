from rest_framework import serializers
from .models import RapportEtudiant, RapportEnseignant

class RapportEtudiantSerializer(serializers.ModelSerializer):
    class Meta:
        model = RapportEtudiant
        fields = '__all__'


class RapportEnseignantSerializer(serializers.ModelSerializer):
    class Meta:
        model = RapportEnseignant
        fields = '__all__'
