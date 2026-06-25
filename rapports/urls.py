from rest_framework.routers import DefaultRouter
from .views import RapportEtudiantViewSet, RapportEnseignantViewSet
from django.urls import path
from .views import rapports_presence, rapports_matieres, rapports_enseignants

router = DefaultRouter()
router.register(r'rapports-etudiants', RapportEtudiantViewSet, basename='rapports-etudiants')
router.register(r'rapports-enseignants', RapportEnseignantViewSet, basename='rapports-enseignants')

urlpatterns = [
    path("presences/", rapports_presence, name="rapports_presence"),
    path("matieres/", rapports_matieres, name="rapports_matieres"),
    path("enseignants/", rapports_enseignants, name="rapports_enseignants"),
]
