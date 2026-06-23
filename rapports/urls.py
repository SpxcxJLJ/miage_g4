from rest_framework.routers import DefaultRouter
from .views import RapportEtudiantViewSet, RapportEnseignantViewSet

router = DefaultRouter()
router.register(r'rapports-etudiants', RapportEtudiantViewSet, basename='rapports-etudiants')
router.register(r'rapports-enseignants', RapportEnseignantViewSet, basename='rapports-enseignants')

urlpatterns = router.urls
