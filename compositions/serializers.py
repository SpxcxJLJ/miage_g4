from rest_framework import serializers
from .models import Composition, CompositionDetail
from backend.api_clients import get_enseignant

from rest_framework import serializers
from .models import CompositionDetail

class CompositionDetailSerializer(serializers.ModelSerializer):
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
