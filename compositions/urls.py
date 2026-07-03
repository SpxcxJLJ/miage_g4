from django.urls import path

from .views import (
    composition_create,
    compositions_list,
    composition_detail,
    composition_detail_create,
    composition_pdf,
)

urlpatterns = [

    path(
        "",
        compositions_list,
        name="compositions_list",
    ),


    path(
        "<int:pk>/",
        composition_detail,
        name="composition_detail",
    ),

    path(
    "create/",
    composition_create,
    name="composition_create"
    ),

    
    
    path(
        "<int:pk>/ajouter/",
        composition_detail_create,
        name="composition_detail_create",
    ),

    path(
        "<int:pk>/pdf/",
        composition_pdf,
        name="composition_pdf",
    ),

]