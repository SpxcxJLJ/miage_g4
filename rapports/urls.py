from rest_framework.routers import DefaultRouter
from .views import RapportEtudiantViewSet, RapportEnseignantViewSet
from django.urls import path
from .views import (
    RapportEtudiantViewSet,
    RapportEnseignantViewSet,
    rapports_presence,
    rapports_matieres,
    rapports_enseignants,
    rapports_cours,
    rapport_enseignants_pdf,
    rapport_matieres_pdf,
    rapport_presences_pdf,
    rapport_cours_pdf,
    rapports_index,
    rapports_etudiants, rapport_etudiants_pdf,
    rapports_classes, rapport_classes_pdf
)


router = DefaultRouter()
router.register(r'rapports-etudiants', RapportEtudiantViewSet, basename='rapports-etudiants')
router.register(r'rapports-enseignants', RapportEnseignantViewSet, basename='rapports-enseignants')

urlpatterns = [
    path("enseignants/", rapports_enseignants, name="rapports_enseignants"),
    path("enseignants/pdf/", rapport_enseignants_pdf, name="rapport_enseignants_pdf"),

    path("matieres/", rapports_matieres, name="rapports_matieres"),
    path("matieres/pdf/", rapport_matieres_pdf, name="rapport_matieres_pdf"),

    path("presences/", rapports_presence, name="rapports_presence"),
    path("presences/pdf/", rapport_presences_pdf, name="rapport_presences_pdf"),
    
    path("cours/", rapports_cours, name="rapports_cours"),
    path("cours/pdf/", rapport_cours_pdf, name="rapport_cours_pdf"),
    
    path("", rapports_index, name="rapports"),
    
    path("etudiants/", rapports_etudiants, name="rapports_etudiants"),
    path("etudiants/pdf/", rapport_etudiants_pdf, name="rapport_etudiants_pdf"),

    path("classes/", rapports_classes, name="rapports_classes"),
    path("classes/pdf/", rapport_classes_pdf, name="rapport_classes_pdf"),
  
]