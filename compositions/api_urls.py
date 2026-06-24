from rest_framework.routers import DefaultRouter
from .views import CompositionDetailViewSet

router = DefaultRouter()
router.register(r'composition-details', CompositionDetailViewSet)

urlpatterns = router.urls
