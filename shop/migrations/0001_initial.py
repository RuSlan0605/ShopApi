# Generated by Django 4.2 on 2023-06-26 13:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=300)),
                ('categoryIcon', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='ProductCombinamtions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('combination', models.CharField(max_length=100)),
                ('sku', models.CharField(max_length=100)),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('unique', models.CharField(max_length=100)),
                ('available_stock', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=300)),
                ('slug', models.SlugField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='shop.category')),
            ],
        ),
        migrations.CreateModel(
            name='ProductsVariationsOptions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('variation_name', models.CharField(max_length=100)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.products')),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('ip', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=100)),
                ('status', models.CharField(max_length=10)),
                ('sactivation_Code', models.CharField(max_length=200)),
                ('forgot_Code', models.CharField(max_length=200)),
                ('forgotCodeSentTime', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Пользователь',
                'verbose_name_plural': 'Пользователи',
            },
        ),
        migrations.CreateModel(
            name='Variations',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('variation_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='VariationOptions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('variations', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.variations')),
            ],
        ),
        migrations.CreateModel(
            name='UserAddresses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('completeAddress', models.CharField(max_length=300)),
                ('phoneNumber', models.CharField(max_length=15)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.users')),
            ],
            options={
                'verbose_name': 'Адресы Пользователей',
                'verbose_name_plural': 'Адресы Пользователей',
            },
        ),
        migrations.CreateModel(
            name='SubCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subcategory_name', models.CharField(max_length=100)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='shop.category')),
            ],
        ),
        migrations.CreateModel(
            name='ProductsVariationsOptionsValue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_variation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.productsvariationsoptions')),
            ],
        ),
        migrations.CreateModel(
            name='ProductStocks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('totalstock', models.IntegerField(default=0)),
                ('unit_price', models.FloatField(default=0)),
                ('total_price', models.FloatField(default=0)),
                ('product_combination', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.productcombinamtions')),
            ],
        ),
        migrations.AddField(
            model_name='products',
            name='sub_category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='shop.subcategory'),
        ),
        migrations.AddField(
            model_name='productcombinamtions',
            name='products',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.products'),
        ),
    ]