from rest_framework import serializers
from .models import Product, CartItem

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class CartItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)  # Make it read-only
    product_id = serializers.PrimaryKeyRelatedField(
        queryset=Product.objects.all(), write_only=True
    )  # Use product_id for writable input

    class Meta:
        model = CartItem
        fields = ['id', 'cart', 'product', 'product_id', 'quantity']

    def create(self, validated_data):
        product = validated_data.pop('product_id')  # Extract product ID
        cart_item = CartItem.objects.create(product=product, **validated_data)
        return cart_item
