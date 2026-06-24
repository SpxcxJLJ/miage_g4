from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import CompositionViewSet, CompositionDetailViewSet, composition_detail, composition_update, enseignants_list
from django.urls import path
from .views import compositions_list
from .views import composition_create

router = DefaultRouter()
router.register(r'compositions', CompositionViewSet, basename='compositions')
router.register(r'composition-details', CompositionDetailViewSet, basename='composition-details')

urlpatterns = [
    path('enseignants/', enseignants_list),
    path('compositions/', compositions_list, name='compositions_list'),
    path('compositions/create/', composition_create, name='composition_create'),
    path('compositions/<int:pk>/', composition_detail, name='composition_detail'),
    path('enseignants/', enseignants_list, name='enseignants_list'),
    path('compositions/<int:pk>/update/', composition_update, name='composition_update'),


]

urlpatterns += router.urls
