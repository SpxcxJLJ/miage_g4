from rest_framework import viewsets
from .models import Composition, CompositionDetail
from .serializers import CompositionSerializer, CompositionDetailSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from backend.api_clients import get_enseignants


class CompositionViewSet(viewsets.ModelViewSet):
    queryset = Composition.objects.all()
    serializer_class = CompositionSerializer


class CompositionDetailViewSet(viewsets.ModelViewSet):
    queryset = CompositionDetail.objects.all()
    serializer_class = CompositionDetailSerializer
    


@api_view(['GET'])
def enseignants_list(request):
    try:
        data = get_enseignants()
        return Response(data)
    except:
        return Response({"error": "Impossible de récupérer les enseignants"}, status=500)

