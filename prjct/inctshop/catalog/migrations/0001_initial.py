# Generated by Django 3.2.9 on 2022-03-31 21:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('brand_name', models.CharField(max_length=100, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Catalog',
            fields=[
                ('catalog_name', models.CharField(max_length=100, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Color',
            fields=[
                ('color_name', models.CharField(max_length=100, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Material',
            fields=[
                ('material_name', models.CharField(max_length=100, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='ProductIdentificate',
            fields=[
                ('product_number', models.IntegerField(default=404, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Size',
            fields=[
                ('size_name', models.CharField(max_length=100, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Reviews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reviews_rating', models.IntegerField()),
                ('reviews_text', models.CharField(max_length=1000)),
                ('reviews_product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.productidentificate')),
                ('reviews_username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=100)),
                ('product_price', models.IntegerField()),
                ('product_detail', models.TextField()),
                ('product_short_detail', models.TextField(max_length=65)),
                ('product_photo', models.ImageField(upload_to='')),
                ('product_photo1', models.ImageField(blank=True, null=True, upload_to='')),
                ('product_photo2', models.ImageField(blank=True, null=True, upload_to='')),
                ('product_photo3', models.ImageField(blank=True, null=True, upload_to='')),
                ('product_photo4', models.ImageField(blank=True, null=True, upload_to='')),
                ('product_photo5', models.ImageField(blank=True, null=True, upload_to='')),
                ('product_photo6', models.ImageField(blank=True, null=True, upload_to='')),
                ('product_photo7', models.ImageField(blank=True, null=True, upload_to='')),
                ('product_photo8', models.ImageField(blank=True, null=True, upload_to='')),
                ('product_photo9', models.ImageField(blank=True, null=True, upload_to='')),
                ('product_brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.brand')),
                ('product_catalog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.catalog')),
                ('product_color', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.color')),
                ('product_material', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.material')),
                ('product_number', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.productidentificate')),
                ('product_size', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.size')),
            ],
        ),
    ]
