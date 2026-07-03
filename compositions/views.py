from django.shortcuts import render, redirect, get_object_or_404
from .models import Composition, CompositionDetail
from .forms import CompositionForm, CompositionDetailForm
from backend.api_clients import get_enseignants, get_enseignant, get_matieres
from django.http import HttpResponse
from rapports.pdf_utils import generate_table_pdf
def compositions_list(request):
    compositions = Composition.objects.all()
    return render(request, "compositions/list.html", {"compositions": compositions})

def composition_create(request):
    if request.method == "POST":
        form = CompositionForm(request.POST)

        if form.is_valid():
            composition = form.save()
            return redirect("composition_detail", pk=composition.pk)

    else:
        form = CompositionForm()

    return render(
        request,
        "compositions/create.html",
        {
            "form": form
        }
    )


def composition_detail(request, pk):
    compo = Composition.objects.get(pk=pk)
    details = compo.details.all()
    return render(request, "compositions/detail.html", {
        "compo": compo,
        "details": details,
        "enseignants": get_enseignants(),
        "matieres": get_matieres(),
    })


def composition_detail_create(request, pk):
    compo = Composition.objects.get(pk=pk)

    if request.method == "POST":
        form = CompositionDetailForm(request.POST)
        if form.is_valid():
            detail = form.save(commit=False)
            detail.composition = compo

            # API enseignants
            enseignant = get_enseignant(detail.enseignant_id)
            detail.enseignant_nom = enseignant["nom"]
            detail.enseignant_prenom = enseignant["prenom"]
            detail.enseignant_email = enseignant.get("email", "")
            detail.enseignant_telephone = enseignant.get("telephone", "")    
            detail.statut = enseignant.get("statut", "")
            detail.raison_sociale = enseignant.get("raison_sociale", "")
            detail.ministere_collectivite = enseignant.get("ministere_collectivite", "")

            # API matières
            matieres = get_matieres()
            matiere = next((m for m in matieres if m["code_matiere"] == detail.code_matiere), None)

            if matiere:
                detail.intitule_matiere = matiere["intitule"]
                # L'utilisateur saisit lui-même le volume horaire

            detail.save()
            return redirect("composition_detail", pk=pk)

    form = CompositionDetailForm()
    return render(request, "compositions/detail_form.html", {
        "form": form,
        "compo": compo,
        "enseignants": get_enseignants(),
        "matieres": get_matieres(),
    })


def composition_pdf(request, pk):
    compo = Composition.objects.get(pk=pk)
    details = compo.details.all()

    headers = [
        "Enseignant", "Matière", "Volume", "Semestre",
        "Heures enseign.", "GRETA", "Service", "Ordre"
    ]

    rows = [
        [
            f"{d.enseignant_nom} {d.enseignant_prenom}",
            d.intitule_matiere,
            d.volume_horaire,
            d.semestre,
            d.heures_enseignement,
            d.heures_greta,
            d.heures_service,
            d.ordre
        ]
        for d in details
    ]

    response = HttpResponse(content_type="application/pdf")
    response["Content-Disposition"] = f"attachment; filename=composition_{pk}.pdf"

    generate_table_pdf(response, f"Composition {compo.intitule_action}", headers, rows)
    return response

