from rest_framework import viewsets
from django.http import HttpResponse
from .models import RapportEtudiant, RapportEnseignant
from .serializers import RapportEtudiantSerializer, RapportEnseignantSerializer
from django.shortcuts import render 
from .presence_api import get_presences
from .matieres_api import get_matieres
from .pdf_utils import generate_table_pdf
from .cours_api import get_cours
from .students_api import get_students
from .classes_api import get_classes


from backend.api_clients import (
    get_enseignants,
    get_matieres,
)


#plus très utilse--------------------------------------
class RapportEtudiantViewSet(viewsets.ModelViewSet):
    queryset = RapportEtudiant.objects.all()
    serializer_class = RapportEtudiantSerializer

class RapportEnseignantViewSet(viewsets.ModelViewSet):
    queryset = RapportEnseignant.objects.all()
    serializer_class = RapportEnseignantSerializer
    
#------------------------------------------------------------
    
def rapports_index(request):
    return render(request, "rapports/index.html")

    
#Les presences         
def rapports_presence(request):
    cours = request.GET.get("cours")
    etudiant = request.GET.get("etudiant")
    statut = request.GET.get("statut")

    data = get_presences(cours=cours, etudiant=etudiant, statut=statut)
    presences = data.get("results", [])

    return render(request, "rapports/presences.html", {"presences": presences})


def rapport_presences_pdf(request):
    cours = request.GET.get("cours")
    etudiant = request.GET.get("etudiant")
    statut = request.GET.get("statut")

    data = get_presences(cours=cours, etudiant=etudiant, statut=statut)
    presences = data.get("results", [])

    headers = ["ID", "Cours", "Étudiant", "Heure", "Statut", "Saisi par", "Date saisie"]
    rows = [
        [
            p["id"],
            p["cours"],
            p["etudiant_id"],
            p["heure_creneau"],
            p["statut"],
            p["saisi_par"],
            p["date_saisie"]
        ]
        for p in presences
    ]

    response = HttpResponse(content_type="application/pdf")
    response["Content-Disposition"] = "attachment; filename=rapport_presences.pdf"

    generate_table_pdf(response, "Rapport des présences", headers, rows)
    return response
#------------------------------------------------------------------------------------------------

#Les cours-----------------perfect--------------------------
def rapports_cours(request):
    date = request.GET.get("date")
    enseignant = request.GET.get("enseignant")
    classe = request.GET.get("classe")

    data = get_cours(date=date, enseignant=enseignant, classe=classe)
    cours = data.get("results", [])

    return render(request, "rapports/cours.html", {"cours": cours})


def rapport_cours_pdf(request):
    date = request.GET.get("date")
    enseignant = request.GET.get("enseignant")
    classe = request.GET.get("classe")

    data = get_cours(date=date, enseignant=enseignant, classe=classe)
    cours = data.get("results", [])

    headers = ["ID", "Date", "Début", "Fin", "Matière", "Enseignant", "Classe", "Salle"]
    rows = [
        [
            c["id"],
            c["date"],
            c["heure_debut"],
            c["heure_fin"],
            c["matiere"],
            c["enseignant"],
            c["classe"],
            c["salle"]
        ]
        for c in cours
    ]

    response = HttpResponse(content_type="application/pdf")
    response["Content-Disposition"] = "attachment; filename=rapport_cours.pdf"

    generate_table_pdf(response, "Rapport des cours", headers, rows)
    return response




#--------------------------------------------------------------
    

#Enseignants------------------------perfect--------------------------------
def rapports_enseignants(request):
    enseignants = get_enseignants()
    return render(request, "rapports/enseignants.html", {"enseignants": enseignants})

def rapport_enseignants_pdf(request):
    enseignants = get_enseignants()

    headers = ["Nom", "Prénom", "Email", "Statut", "Raison sociale", "Ministère"]
    rows = [
        [
            e["nom"], e["prenom"], e["email"],
            e["statut"], e["raison_sociale"], e["ministere_collectivite"]
        ]
        for e in enseignants
    ]

    response = HttpResponse(content_type="application/pdf")
    response["Content-Disposition"] = "attachment; filename=rapport_enseignants.pdf"

    generate_table_pdf(response, "Rapport des enseignants", headers, rows)
    return response

#-----------------------------------------------------------------------------


# Matières------------------------perfect--------------------------------
def rapports_matieres(request):
    matieres = get_matieres()
    return render(request, "rapports/matieres.html", {"matieres": matieres})

def rapport_matieres_pdf(request):
    matieres = get_matieres()

    headers = ["Code", "Intitulé", "Année", "Volume"]
    rows = [
        [m["code_matiere"], m["intitule"], m["annee_universitaire"], m["volume_horaire"]]
        for m in matieres
    ]

    response = HttpResponse(content_type="application/pdf")
    response["Content-Disposition"] = "attachment; filename=rapport_matieres.pdf"

    generate_table_pdf(response, "Rapport des matières", headers, rows)
    return response

#------------------------------------------------------------------------------


#etudiants------------------------perfect--------------------------------
def rapports_etudiants(request):
    etudiants = get_students()

    return render(request, "rapports/students.html", {
        "etudiants": etudiants
    })


def rapport_etudiants_pdf(request):
    etudiants = get_students()

    headers = ["INE", "Nom", "Prénom", "Sexe", "Email Univ.", "Téléphone", "Naissance"]
    rows = [
        [
            e["INE"],
            e["Lname"],
            e["Fname"],
            e["Sexe"],
            e["univ_email"],
            e["PhoneNumber"],
            e["Birthdate"]
        ]
        for e in etudiants
    ]

    response = HttpResponse(content_type="application/pdf")
    response["Content-Disposition"] = "attachment; filename=rapport_etudiants.pdf"

    generate_table_pdf(response, "Rapport des étudiants", headers, rows)
    return response
#------------------------------------------------------------------------------


#classes------------------------perfect--------------------------------

def rapports_classes(request):
    classes = get_classes()

    return render(request, "rapports/classes.html", {
        "classes": classes
    })


def rapport_classes_pdf(request):
    classes = get_classes()

    headers = ["ID Classe", "Nom", "Programme", "Niveau", "Début", "Fin", "Archive"]
    rows = [
        [
            c["idClass"],
            c["ClassName"],
            c["Curriculum"],
            c["idLevel"],
            c["StartYear"],
            c["EndYear"],
            c["Archive"]
        ]
        for c in classes
    ]

    response = HttpResponse(content_type="application/pdf")
    response["Content-Disposition"] = "attachment; filename=rapport_classes.pdf"

    generate_table_pdf(response, "Rapport des classes", headers, rows)
    return response
#------------------------------------------------------------------------------





