from rest_framework import viewsets
from .models import RapportEtudiant, RapportEnseignant
from .serializers import RapportEtudiantSerializer, RapportEnseignantSerializer

class RapportEtudiantViewSet(viewsets.ModelViewSet):
    queryset = RapportEtudiant.objects.all()
    serializer_class = RapportEtudiantSerializer


class RapportEnseignantViewSet(viewsets.ModelViewSet):
    queryset = RapportEnseignant.objects.all()
    serializer_class = RapportEnseignantSerializer
