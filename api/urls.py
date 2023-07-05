from django.urls import path
from rest_framework.routers import SimpleRouter
from api.views import *


router = SimpleRouter()
router.register('', ProductViewSet, basename='products')
router.register('users', UserViewSet, basename='users')

urlpatterns = [
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product-detail'),
    path('users/<int:pk>/', UserDetailView.as_view(), name='user-detail'),
    path('useraddress/', UserAddressView.as_view(), name='useraddress'),
    path('useraddress/<int:pk>/', UserAddressDetailView.as_view(), name='address-detail'),
    path('category/', CategoryView.as_view(), name='category'),
    path('category/<int:pk>/', CategoryDetailView.as_view(), name='category-detail'),
    path('subcategory/', SubcategoryView.as_view(), name='ssubcategory'),
    path('subcategory/<int:pk>/', SubcategoryDeatilView.as_view(), name='subcategory-detail'),
    path('productcombin/', ProductCombView.as_view(), name='productcombin'),
    path('productcombin/<int:pk>/', ProductCombDetailView.as_view(), name='combin-detail'),
    path('productstock/', ProductStockView.as_view(), name='stock'),
    path('productstock/<int:pk>/', ProductStockDetailView.as_view(), name='stock-detail'),
    path('productvar/', ProductVarOptView.as_view(), name='variatoptions'),
    path('productvar/<int:pk>/', ProductVarOptDetailView.as_view(), name='variation_detail'),
    path('productvarval/', ProdVarOptValView.as_view(), name='variation-value'),
    path('productvarval/<int:pk>/', ProdVarOptValDetailView.as_view(), name='variation-value-detail'),
    path('variations/', VariationView.as_view(), name='variations'),
    path('variations/<int:pk>/', VariationDetailView.as_view(), name='variation-detail'),
    path('variationopt/', VariationOptionView.as_view(), name='variation-option'),
    path('variationopt/<int:pk>/', VariationOptionDetailView.as_view(), name='varoption-detail'),
]
urlpatterns += router.urls