from django.db import models
from django.db.models.query import QuerySet
from django.utils import timezone


#-----------------------------------------------------------------------------


class UserManager(models.Manager):
    def get_queryset(self) -> QuerySet:
        return super().get_queryset()\
            .filter(status=Users.Status.REGISTERED)

class Users(models.Model):

    class Status(models.TextChoices):
        DRAFT = 'DF', 'Draft'
        REGISTERED = 'RG', 'Registered'
        SENT = 'SN', 'Sent'

    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    ip = models.CharField(max_length=30)
    email = models.EmailField()
    password = models.CharField(max_length=100)
    status = models.CharField(max_length=10, choices=Status.choices, default=Status.DRAFT)
    sactivation_Code = models.CharField(max_length=200)
    forgot_Code = models.CharField(max_length=200)
    forgotCodeSentTime = models.DateTimeField(default=timezone.now)

    objects = models.Manager()
    registered = UserManager()

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ['-first_name', '-last_name']

    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'
    

class UserAddresses(models.Model):

    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    completeAddress = models.CharField(max_length=300)
    phoneNumber = models.CharField(max_length=15)

    class Meta:
        verbose_name = 'Адресы Пользователей'
        verbose_name_plural = 'Адресы Пользователей'

    def __str__(self) -> str:
        return self.completeAddress


#------------------------------------------------------------------------------


class ProductManager(models.Manager):
    def get_queryset(self) -> QuerySet:
        return super().get_queryset()\
            .filter(status=Products.Status.PUBLISHED)

class Products(models.Model):

    class Status(models.TextChoices):
        DRAFT = 'DF', 'Draft'
        PUBLISHED = 'PB', 'Published'

    product_name = models.CharField(max_length=300)
    slug = models.SlugField()
    publish = models.DateTimeField(default=timezone.now)
    category = models.ForeignKey('Category', on_delete=models.PROTECT, related_name='products')
    sub_category = models.ForeignKey('SubCategory', on_delete=models.PROTECT)
    image = models.ImageField(upload_to='images/')
    status = models.CharField(max_length=10, choices=Status.choices, default=Status.DRAFT)

    objects = models.Manager()
    published = ProductManager()

    class Meta:
        verbose_name_plural = 'Продукты'
        verbose_name = 'Продукты'
        ordering = ['-publish']
        indexes = [
            models.Index(fields=['-publish'])
        ]

    def __str__(self) -> str:
        return self.product_name

class Category(models.Model):

    category_name = models.CharField(max_length=300)
    categoryIcon = models.CharField(max_length=255)
    slug = models.SlugField(max_length=200, unique=True)

    class Meta:
        ordering = ['category_name']
        indexes = [
            models.Index(fields=['category_name'])
        ]

        verbose_name_plural = 'Категории'
        verbose_name = 'Категория'

    def __str__(self) -> str:
        return self.category_name

class SubCategory(models.Model):

    subcategory_name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)

    class Meta:
        ordering = ['subcategory_name']
        indexes = [
            models.Index(fields=['subcategory_name'])
        ]
        
        verbose_name_plural = 'Субкатегории'
        verbose_name = 'Субкатегория'

    def __str__(self) -> str:
        return self.subcategory_name
    

#----------------------------------------------------------------------------


class ProdCombinationsManager(models.Manager):
    def get_queryset(self) -> QuerySet:
        return super().get_queryset()\
            .filter(status=ProductCombinamtions.Status.AVAILABLE)
    
class ProductCombinamtions(models.Model):

    class Status(models.TextChoices):
        AVAILABLE = 'AVBL', 'Available'
        NOT_AVAILABLE = 'NAVBL', 'Not_Available'

    combination = models.CharField(max_length=100)
    sku = models.CharField(max_length=100)
    price = models.DecimalField(default=0, decimal_places=3, max_digits=10)
    unique = models.CharField(max_length=100)
    products = models.ForeignKey(Products, on_delete=models.CASCADE)
    available_stock = models.IntegerField(default=0)
    status = models.CharField(max_length=10, choices=Status.choices, default=Status.NOT_AVAILABLE)

    objects = models.Manager()
    available = ProdCombinationsManager()

    class Meta:
        verbose_name_plural = 'Комбинации продуктов'
        verbose_name = 'Комбинация продуктов'

    def __str__(self) -> str:
        return self.combination

class ProductStocks(models.Model):
    
    totalstock = models.IntegerField(default=0)
    unit_price = models.FloatField(default=0)
    total_price = models.FloatField(default=0)
    product_combination = models.ForeignKey(ProductCombinamtions, on_delete=models.CASCADE)


#----------------------------------------------------------------------------------


class ProductsVariationsOptions(models.Model):

    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    variation_name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.variation_name
    
class ProductsVariationsOptionsValue(models.Model):

    product_variation = models.ForeignKey(ProductsVariationsOptions, on_delete=models.CASCADE)


#----------------------------------------------------------------------------------

class Variations(models.Model):

    variation_name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.variation_name
    
class VariationOptions(models.Model):

    variations = models.ForeignKey(Variations, on_delete=models.CASCADE)