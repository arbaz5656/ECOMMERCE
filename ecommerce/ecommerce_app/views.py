from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Product, CartItem
from .serializers import ProductSerializer, CartItemSerializer
from django.shortcuts import render

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class CartItemViewSet(viewsets.ModelViewSet):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer

    @action(detail=True, methods=['post'])
    def add_to_cart(self, request, pk=None):
        product = Product.objects.get(pk=pk)
        cart_item, created = CartItem.objects.get_or_create(product=product)
        if not created:
            cart_item.quantity += 1
            cart_item.save()
        return Response({'status': 'added to cart'})
def index(request):
    return render(request, "index.html")