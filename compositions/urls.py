from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import CompositionViewSet, CompositionDetailViewSet, enseignants_list

router = DefaultRouter()
router.register(r'compositions', CompositionViewSet, basename='compositions')
router.register(r'composition-details', CompositionDetailViewSet, basename='composition-details')

urlpatterns = [
    path('enseignants/', enseignants_list),
]

urlpatterns += router.urls
