from .models import Product
from .serializers import ProductDetailSerialiser
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter,OrderingFilter
from rest_framework.response import Response
class ProductDetailView(generics.RetrieveAPIView):
    serializer_class = ProductDetailSerialiser
    def get_queryset(self):
        return Product.objects.all()
    def retrieve(self, request, *args, **kwargs):
        params = kwargs
        product = Product.objects.filter(id = params['pk'])
        serializer = ProductDetailSerialiser(product,many=True)
        return Response(serializer.data)

class ProductsListView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductDetailSerialiser
    filter_backends = [DjangoFilterBackend,SearchFilter,OrderingFilter]
    search_fields = ['title','sku']
    ordering_fields = ['status']



