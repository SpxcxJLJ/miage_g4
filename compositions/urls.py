from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import *

router = DefaultRouter()

router.register(
    r"compositions",
    CompositionViewSet,
)

router.register(
    r"composition-details",
    CompositionDetailViewSet,
)

urlpatterns = [

    path(
        "compositions/",
        compositions_list,
        name="compositions_list",
    ),

    path(
        "compositions/create/",
        composition_create,
        name="composition_create",
    ),

    path(
        "compositions/detail/create/",
        composition_detail_create,
        name="composition_detail_create",
    ),

    path(
        "compositions/<int:pk>/",
        composition_detail,
        name="composition_detail",
    ),

    path(
        "compositions/<int:pk>/update/",
        composition_update,
        name="composition_update",
    ),

    path(
        "enseignants/",
        enseignants_list,
        name="enseignants_list",
    ),

]

urlpatterns += router.urls