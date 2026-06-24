from rest_framework import serializers
from .models import Composition, CompositionDetail
from backend.api_clients import get_enseignant

class CompositionDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompositionDetail
        fields = [
            'id',
            'composition',
            'enseignant_id',
            'enseignant_nom',
            'enseignant_prenom',
            'statut',
            'raison_sociale',
            'module',
            'semestre',
            'heures_enseignement',
            'heures_greta',
            'heures_service',
            'ordre'
        ]

    class Meta:
        model = CompositionDetail
        fields = '__all__'

    def get_enseignant_details(self, obj):
        try:
            return get_enseignant(obj.id_enseignant)
        except Exception:
            return {"error": "Impossible de récupérer l'enseignant"}

class CompositionSerializer(serializers.ModelSerializer):
    details = CompositionDetailSerializer(many=True, read_only=True)

    class Meta:
        model = Composition
        fields = '__all__'
