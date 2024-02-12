

from rest_framework import serializers
from .models import Product, Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id','category_name', 'category_description')

class ProductSerializer(serializers.ModelSerializer):
    # category = CategorySerializer()  
    class Meta:
        model = Product
        fields = ('id','product_code', 'product_description', 'price', 'quantity', 'category')



# from rest_framework import serializers
# from .models import Category, Product

# class CategorySerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Category
#         fields = ('category_name', 'category_description')  

# class ProductSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Product
#         fields = ('product_code', 'product_description', 'price', 'quantity', 'category')  

