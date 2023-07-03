from django.contrib import admin
from .models import (
    Users, UserAddresses,
    Products, Category,
    SubCategory, ProductCombinamtions,
    ProductStocks, ProductsVariationsOptions,
    ProductsVariationsOptionsValue,
    Variations, VariationOptions
)
@admin.register(Users)
class UserAdmin(admin.ModelAdmin):

    list_display = ['id', 'first_name', 'last_name', 'email', 'status']
    list_display_links = ['id', 'first_name', 'last_name', 'email']
    list_filter = ['first_name', 'last_name', 'status', 'forgotCodeSentTime']
    search_fields = ['id', 'first_name', 'last_name', 'status']
    date_hierarchy = 'forgotCodeSentTime'
    ordering = ['status', 'forgotCodeSentTime']

@admin.register(UserAddresses)
class UserAddressAdmin(admin.ModelAdmin):

    list_display = ['id', 'user', 'completeAddress', 'phoneNumber']
    list_display_links = ['id', 'user']

@admin.register(Products)
class ProductAdmin(admin.ModelAdmin):

    list_display = ['id', 'product_name', 'category', 'sub_category']
    list_display_links = ['id', 'product_name']
    list_filter = ['product_name', 'category', 'sub_category']
    search_fields = ['product_name', 'category', 'sub_category']
    prepopulated_fields = {'slug': ('product_name',)}
    raw_id_fields = ['category', 'sub_category']

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):

    list_display = ['id', 'category_name']
    list_display_links = ['id', 'category_name']
    list_filter = ['category_name']
    prepopulated_fields = {'slug': ('category_name',)}
    search_fields = ['category_name', 'categoryIcon']

@admin.register(SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):
    
    list_display = ['id', 'subcategory_name']
    list_display_links = ['id', 'subcategory_name']
    list_filter = ['subcategory_name']
    search_fields = ['subcategory_name']
    raw_id_fields = ['category']

@admin.register(ProductCombinamtions)
class ProductCombinationsAdmin(admin.ModelAdmin):

    list_display = ['id', 'combination', 'sku', 'price', 'available_stock']
    list_display_links = ['id', 'combination']
    list_filter = ['combination', 'sku', 'available_stock']
    search_fields = ['combination', 'sku', 'unique']
    raw_id_fields = ['products']

@admin.register(ProductStocks)
class ProductStocksAdmin(admin.ModelAdmin):

    list_display = ['id', 'totalstock', 'unit_price', 'total_price']
    list_display_links = ['id', 'totalstock', 'unit_price', 'total_price']
    list_filter = ['totalstock', 'unit_price', 'total_price']
    raw_id_fields = ['product_combination']

@admin.register(ProductsVariationsOptions)
class ProductVariationsOptionsAdmin(admin.ModelAdmin):

    list_display = ['id', 'variation_name']
    list_display_links = ['id', 'variation_name']
    list_filter = ['variation_name']
    search_fields = ['variation_name']
    raw_id_fields = ['product']
    ordering = ['variation_name']

@admin.register(ProductsVariationsOptionsValue)
class ProductVariationsOptionsValueAdmin(admin.ModelAdmin):

    list_display = ['id', 'product_variation']
    list_display_links = ['id', 'product_variation']
    search_fields = ['product_variation']
    raw_id_fields = ['product_variation']
    ordering = ['product_variation']

@admin.register(Variations)
class VariationsAdmin(admin.ModelAdmin):

    list_display = ['id', 'variation_name']
    list_display_links = ['id', 'variation_name']
    search_fields = ['variation_name']
    ordering = ['variation_name']

@admin.register(VariationOptions)
class VariationOptionsAdmin(admin.ModelAdmin):

    list_display = ['id', 'variations']
    list_display_links = ['id', 'variations']
    search_fields = ['variations']
    raw_id_fields = ['variations']
    ordering = ['variations']