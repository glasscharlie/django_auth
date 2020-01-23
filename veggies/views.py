from rest_framework import generics
from veggies.models import Veggies
from .serializers import VeggieSerializer
from .permissions import IsAuthorOrReadOnly

class VeggieList(generics.ListCreateAPIView):
    queryset = Veggies.objects.all()
    serializer_class = VeggieSerializer

class VeggieDetail(generics.RetrieveUpdateAPIView):
    queryset = Veggies.objects.all()
    serializer_class = VeggieSerializer
    permissions_classes = (
        IsAuthorOrReadOnly,
    )