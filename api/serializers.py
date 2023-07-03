from rest_framework import serializers
from shop.models import (
    Users, UserAddresses,
    Products, Category,
    SubCategory, ProductCombinamtions,
    ProductStocks, ProductsVariationsOptions,
    ProductsVariationsOptionsValue, 
    VariationOptions, Variations
)

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = Users
        fields = '__all__'

class UserAddressSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserAddresses
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Products
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'

class SubcategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = SubCategory
        fields = '__all__'

class ProductCombinationSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductCombinamtions
        fields = '__all__'

class ProductStockSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ProductStocks
        fields = '__all__'

class ProductVarOpSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductsVariationsOptions
        fields = '__all__'

class ProductVarOpValSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductsVariationsOptionsValue
        fields = '__all__'

class VariationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Variations
        fields = '__all__'

class VariationsOptSerializer(serializers.ModelSerializer):

    class Meta:
        model = VariationOptions
        fields = '__all__'
