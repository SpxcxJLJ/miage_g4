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

    return render(request, "rapports/presences.html", {
        "presences": presences,
        "cours_filter": cours,
        "etudiant_filter": etudiant,
        "statut_filter": statut,
    })



def rapport_presences_pdf(request):
    cours = request.GET.get("cours")
    etudiant = request.GET.get("etudiant")
    statut = request.GET.get("statut")

    data = get_presences(cours=cours, etudiant=etudiant, statut=statut)
    presences = data.get("results", [])

    headers = ["ID", "Cours", "Étudiant", "Heure", "Statut", "Saisi par", "Date saisie"]
    rows = [
        [
            p.get("id"),
            p.get("cours"),
            p.get("etudiant_id"),
            p.get("heure_creneau"),
            p.get("statut"),
            p.get("saisi_par"),
            p.get("date_saisie")
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

    return render(request, "rapports/cours.html", {
        "cours": cours,
        "date_filter": date,
        "enseignant_filter": enseignant,
        "classe_filter": classe,
    })


def rapport_cours_pdf(request):
    date = request.GET.get("date")
    enseignant = request.GET.get("enseignant")
    classe = request.GET.get("classe")

    data = get_cours(date=date, enseignant=enseignant, classe=classe)
    cours = data.get("results", [])

    headers = ["ID", "Date", "Début", "Fin", "Matière", "Enseignant", "Classe", "Salle"]
    rows = [
        [
            c.get("id"),
            c.get("date"),
            c.get("heure_debut"),
            c.get("heure_fin"),
            c.get("matiere", c.get("matiere_id", "")),
            c.get("enseignant", c.get("enseignant_id", "")),
            c.get("classe", c.get("classe_id", "")),
            c.get("salle", "")
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
    nom = request.GET.get("nom")
    statut = request.GET.get("statut")

    enseignants = get_enseignants()

    if nom:
        enseignants = [e for e in enseignants if nom.lower() in e["nom"].lower()]

    if statut:
        enseignants = [e for e in enseignants if statut.lower() in e["statut"].lower()]

    return render(request, "rapports/enseignants.html", {
        "enseignants": enseignants,
        "nom_filter": nom,
        "statut_filter": statut,
    })

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
    code = request.GET.get("code")
    annee = request.GET.get("annee")

    matieres = get_matieres()

    if code:
        matieres = [m for m in matieres if code.lower() in m["code_matiere"].lower()]

    if annee:
        matieres = [m for m in matieres if annee == m["annee_universitaire"]]

    return render(request, "rapports/matieres.html", {
        "matieres": matieres,
        "code_filter": code,
        "annee_filter": annee,
    })


def rapport_matieres_pdf(request):
    code = request.GET.get("code")
    annee = request.GET.get("annee")

    matieres = get_matieres()

    if code:
        matieres = [m for m in matieres if code.lower() in m["code_matiere"].lower()]

    if annee:
        matieres = [m for m in matieres if str(m["annee_universitaire"]) == annee]

    headers = ["ID", "Code", "Intitulé", "Année", "Volume"]
    rows = [
        [
            m.get("id"),
            m.get("code_matiere"),
            m.get("intitule"),
            m.get("annee_universitaire"),
            m.get("volume_horaire")
        ]
        for m in matieres
    ]

    response = HttpResponse(content_type="application/pdf")
    response["Content-Disposition"] = "attachment; filename=rapport_matieres.pdf"

    generate_table_pdf(response, "Rapport des matières", headers, rows)
    return response


#------------------------------------------------------------------------------


#etudiants------------------------perfect--------------------------------
def rapports_etudiants(request):
    ine = request.GET.get("ine")
    sexe = request.GET.get("sexe")

    etudiants = get_students()

    if ine:
        etudiants = [e for e in etudiants if ine in e["INE"]]

    if sexe:
        etudiants = [e for e in etudiants if sexe == e["Sexe"]]

    return render(request, "rapports/students.html", {
        "etudiants": etudiants,
        "ine_filter": ine,
        "sexe_filter": sexe,
    })



def rapport_etudiants_pdf(request):
    ine = request.GET.get("ine")
    sexe = request.GET.get("sexe")

    etudiants = get_students()

    if ine:
        etudiants = [e for e in etudiants if ine in e["INE"]]

    if sexe:
        etudiants = [e for e in etudiants if sexe == e["Sexe"]]

    headers = ["INE", "Nom", "Prénom", "Sexe", "Email Univ.", "Téléphone", "Naissance"]
    rows = [
        [
            e.get("INE"),
            e.get("Lname"),
            e.get("Fname"),
            e.get("Sexe"),
            e.get("univ_email"),
            e.get("PhoneNumber"),
            e.get("Birthdate")
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
    niveau = request.GET.get("niveau")
    programme = request.GET.get("programme")

    classes = get_classes()

    if niveau:
        classes = [c for c in classes if str(c["idLevel"]) == niveau]

    if programme:
        classes = [c for c in classes if programme.lower() in c["Curriculum"].lower()]

    return render(request, "rapports/classes.html", {
        "classes": classes,
        "niveau_filter": niveau,
        "programme_filter": programme,
    })


def rapport_classes_pdf(request):
    programme = request.GET.get("programme")
    niveau = request.GET.get("niveau")
    annee = request.GET.get("annee")

    classes = get_classes()

    if programme:
        classes = [c for c in classes if programme.lower() in c["Curriculum"].lower()]

    if niveau:
        classes = [c for c in classes if str(c["idLevel"]) == niveau]

    if annee:
        classes = [c for c in classes if str(c["StartYear"]) == annee]

    headers = ["ID Classe", "Nom", "Programme", "Niveau", "Début", "Fin", "Archive"]
    rows = [
        [
            c.get("idClass"),
            c.get("ClassName"),
            c.get("Curriculum"),
            c.get("idLevel"),
            c.get("StartYear"),
            c.get("EndYear"),
            c.get("Archive")
        ]
        for c in classes
    ]

    response = HttpResponse(content_type="application/pdf")
    response["Content-Disposition"] = "attachment; filename=rapport_classes.pdf"

    generate_table_pdf(response, "Rapport des classes", headers, rows)
    return response

#------------------------------------------------------------------------------





