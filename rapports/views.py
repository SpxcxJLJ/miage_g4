from rest_framework import viewsets
from .models import RapportEtudiant, RapportEnseignant
from .serializers import RapportEtudiantSerializer, RapportEnseignantSerializer
from django.shortcuts import render
from .presence_api import get_cours
from .matieres_api import get_matieres
from backend.api_clients import get_enseignants
class RapportEtudiantViewSet(viewsets.ModelViewSet):
    queryset = RapportEtudiant.objects.all()
    serializer_class = RapportEtudiantSerializer


class RapportEnseignantViewSet(viewsets.ModelViewSet):
    queryset = RapportEnseignant.objects.all()
    serializer_class = RapportEnseignantSerializer
    
    
def rapports_presence(request):
    date = request.GET.get("date")
    classe = request.GET.get("classe")
    enseignant = request.GET.get("enseignant")

    data = get_cours(date=date, classe=classe, enseignant=enseignant)

    return render(request, "rapports/presences.html", {
        "cours": data.get("results", []),
    })
    
def rapports_matieres(request):
    matieres = get_matieres()
    return render(request, "rapports/matieres.html", {"matieres": matieres})

def rapports_enseignants(request):
    enseignants = get_enseignants()
    return render(request, "rapports/enseignants.html", {"enseignants": enseignants})
