from rest_framework import viewsets
from .models import Composition, CompositionDetail
from .serializers import CompositionDetailSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from backend.api_clients import get_enseignants
from django.shortcuts import render
from .models import Composition
from .forms import CompositionDetailForm, CompositionForm
from django.shortcuts import redirect
from django.urls import path

from .serializers import CompositionSerializer

class CompositionViewSet(viewsets.ModelViewSet):
    queryset = Composition.objects.all()
    serializer_class = CompositionSerializer


class CompositionDetailViewSet(viewsets.ModelViewSet):
    queryset = CompositionDetail.objects.all().order_by('ordre')
    serializer_class = CompositionDetailSerializer


def compositions_list(request):
    compositions = Composition.objects.all()
    return render(request, 'compositions/list.html', {'compositions': compositions})    

def composition_detail(request, pk):
    compo = Composition.objects.get(pk=pk)
    return render(request, 'compositions/detail.html', {'compo': compo})



def composition_create(request):
    if request.method == 'POST':
        form = CompositionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('compositions_list')
    else:
        form = CompositionForm()

    return render(request, 'compositions/create.html', {'form': form})

def composition_update(request, pk):
    compo = Composition.objects.get(pk=pk)
    if request.method == 'POST':
        form = CompositionForm(request.POST, instance=compo)
        if form.is_valid():
            form.save()
            return redirect('compositions_list')
    else:
        form = CompositionForm(instance=compo)

    return render(request, 'compositions/update.html', {'form': form})

def composition_detail_create(request):
    if request.method == 'POST':
        form = CompositionDetailForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('compositions_list')
    else:
        form = CompositionDetailForm()

    return render(request, 'compositions/detail_form.html', {'form': form})


import requests

def enseignants_list(request):
    response = requests.get("http://10.3.17.208:5000/enseignants")  #api de prisca
    enseignants = response.json()
    return render(request, 'compositions/enseignants.html', {'enseignants': enseignants})





