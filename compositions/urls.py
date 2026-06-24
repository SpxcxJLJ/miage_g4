from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import CompositionViewSet, CompositionDetailViewSet, enseignants_list
from django.urls import path
from .views import compositions_list

router = DefaultRouter()
router.register(r'compositions', CompositionViewSet, basename='compositions')
router.register(r'composition-details', CompositionDetailViewSet, basename='composition-details')

urlpatterns = [
    path('enseignants/', enseignants_list),
    path('compositions/', compositions_list, name='compositions_list'),
]

urlpatterns += router.urls
