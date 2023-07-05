from rest_framework.generics import ListCreateAPIView
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.pagination import PageNumberPagination
from shop.models import *
from .serializers import *

class ListPagination(PageNumberPagination):

    page_size = 2
    page_query_param = 'page_size'
    max_page_size = 500

class ProductViewSet(ModelViewSet):

    queryset = Products.objects.all()
    serializer_class = ProductSerializer
    pagination_class = ListPagination

class UserViewSet(ModelViewSet):
    
    queryset = Users.objects.all()
    serializer_class = UserSerializer
    pagination_class = ListPagination

class UserDetailView(RetrieveUpdateDestroyAPIView):

    queryset = Users.objects.all()
    serializer_class = UserSerializer
    pagination_class = ListPagination

class ProductDetailView(RetrieveUpdateDestroyAPIView):

    queryset = Products.objects.all()
    serializer_class = ProductSerializer
    pagination_class = ListPagination

class UserAddressView(ListCreateAPIView):

    queryset = UserAddresses.objects.all()
    serializer_class = UserAddressSerializer
    pagination_class = ListPagination

class UserAddressDetailView(RetrieveUpdateDestroyAPIView):

    queryset = UserAddresses.objects.all()
    serializer_class = UserAddressSerializer
    pagination_class = ListPagination

class CategoryView(ListCreateAPIView):

    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    pagination_class = ListPagination

class CategoryDetailView(RetrieveUpdateDestroyAPIView):

    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    pagination_class = ListPagination

class SubcategoryView(ListCreateAPIView):

    queryset = SubCategory.objects.all()
    serializer_class = SubcategorySerializer
    pagination_class = ListPagination

class SubcategoryDeatilView(RetrieveUpdateDestroyAPIView):

    queryset = SubCategory.objects.all()
    serializer_class = SubcategorySerializer
    pagination_class = ListPagination

class ProductCombView(ListCreateAPIView):

    queryset = ProductCombinamtions.objects.all()
    serializer_class = ProductCombinationSerializer
    pagination_class = ListPagination

class ProductCombDetailView(RetrieveUpdateDestroyAPIView):

    queryset = ProductCombinamtions.objects.all()
    serializer_class = ProductCombinationSerializer
    pagination_class = ListPagination

class ProductStockView(ListCreateAPIView):

    queryset = ProductStocks.objects.all()
    serializer_class = ProductStockSerializer
    pagination_class = ListPagination

class ProductStockDetailView(RetrieveUpdateDestroyAPIView):

    queryset = ProductStocks.objects.all()
    serializer_class = ProductStockSerializer
    pagination_class = ListPagination

class ProductVarOptView(ListCreateAPIView):

    queryset = ProductsVariationsOptions.objects.all()
    serializer_class = ProductVarOpSerializer
    pagination_class = ListPagination

class ProductVarOptDetailView(RetrieveUpdateDestroyAPIView):

    queryset = ProductsVariationsOptions.objects.all()
    serializer_class = ProductVarOpSerializer
    pagination_class = ListPagination

class ProdVarOptValView(ListCreateAPIView):

    queryset = ProductsVariationsOptionsValue.objects.all()
    serializer_class = ProductVarOpValSerializer
    pagination_class = ListPagination

class ProdVarOptValDetailView(RetrieveUpdateDestroyAPIView):

    queryset = ProductsVariationsOptionsValue.objects.all()
    serializer_class = ProductVarOpValSerializer
    pagination_class = ListPagination

class VariationView(ListCreateAPIView):

    queryset = Variations.objects.all()
    serializer_class = VariationSerializer
    pagination_class = ListPagination

class VariationDetailView(RetrieveUpdateDestroyAPIView):

    queryset = Variations.objects.all()
    serializer_class = VariationSerializer
    pagination_class = ListPagination

class VariationOptionView(ListCreateAPIView):

    queryset = VariationOptions.objects.all()
    serializer_class = VariationsOptSerializer
    pagination_class = ListPagination

class VariationOptionDetailView(RetrieveUpdateDestroyAPIView):

    queryset = VariationOptions.objects.all()
    serializer_class = VariationsOptSerializer
    pagination_class = ListPagination
