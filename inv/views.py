from rest_framework import viewsets
from .serializers import ProductSerializer
from .models import Product

class ProducView(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()

