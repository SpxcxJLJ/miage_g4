from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404

from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Composition
from .models import CompositionDetail

from .forms import CompositionForm
from .forms import CompositionDetailForm

from .serializers import CompositionSerializer
from .serializers import CompositionDetailSerializer

from backend.api_clients import (
    get_enseignants,
)
class CompositionViewSet(viewsets.ModelViewSet):
    queryset = Composition.objects.all()
    serializer_class = CompositionSerializer


class CompositionDetailViewSet(viewsets.ModelViewSet):
    queryset = CompositionDetail.objects.all().order_by('ordre')
    serializer_class = CompositionDetailSerializer


def compositions_list(request):
    compositions = Composition.objects.all()
    return render(request, 'compositions/list.html', {'compositions': compositions})    

def composition_detail(request, pk):
    compo = Composition.objects.get(pk=pk)
    return render(request, 'compositions/detail.html', {'compo': compo})


def composition_detail_list(request, composition_id):
    details = CompositionDetail.objects.filter(composition_id=composition_id)

    return render(
        request,
        "compositions/detail_tables.html",
        {"details": details},
    )


def composition_create(request):
    if request.method == "POST":
        form = CompositionForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("compositions_list")

    else:
        form = CompositionForm()

    return render(
        request,
        "compositions/create.html",
        {
            "form": form
        }
    )
    
    
def composition_detail_create(request):

    if request.method == "POST":

        form = CompositionDetailForm(request.POST)

        if form.is_valid():

            detail = form.save(commit=False)

            enseignant = get_enseignant(detail.enseignant_id)

            detail.enseignant_nom = enseignant["nom"]
            detail.enseignant_prenom = enseignant["prenom"]
            detail.statut = enseignant.get("statut", "")
            detail.raison_sociale = enseignant.get("raison_sociale", "")
            detail.ministere_collectivite = enseignant.get("ministere_collectivite", "")

            matieres = get_matieres()

            matiere = next(
                (
                    m
                    for m in matieres
                    if m["id"] == detail.matiere_id
                ),
                None,
            )

            if matiere:
                detail.code_matiere = matiere["code_matiere"]
                detail.intitule_matiere = matiere["intitule"]
                detail.volume_horaire = matiere["volume_horaire"]

            detail.save()

            return redirect("compositions_list")

    else:

        form = CompositionDetailForm()

    return render(
        request,
        "compositions/detail_form.html",
        {
            "form": form,
            "enseignants": get_enseignants(),
            "matieres": get_matieres(),
        },
    )

def composition_update(request, pk):
    compo = Composition.objects.get(pk=pk)
    if request.method == 'POST':
        form = CompositionForm(request.POST, instance=compo)
        if form.is_valid():
            form.save()
            return redirect('compositions_list')
    else:
        form = CompositionForm(instance=compo)

    return render(request, 'compositions/update.html', {'form': form})

import requests







