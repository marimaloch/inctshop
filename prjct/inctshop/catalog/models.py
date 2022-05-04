from django.db import models
from django.contrib.auth.models import User


class Catalog(models.Model):
    catalog_name = models.CharField(max_length=100, primary_key=True)


class Material(models.Model):
    material_name = models.CharField(max_length=100, primary_key=True)


class Brand(models.Model):
    brand_name = models.CharField(max_length=100, primary_key=True)


class Color(models.Model):
    color_name = models.CharField(max_length=100, primary_key=True)


class Size(models.Model):
    size_name = models.CharField(max_length=100, primary_key=True)


class ProductIdentificate(models.Model):
    product_number = models.IntegerField(default=404, primary_key=True)


class Product(models.Model):
    product_number = models.ForeignKey(ProductIdentificate, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=100)
    product_price = models.IntegerField()
    product_detail = models.TextField()
    product_short_detail = models.TextField(max_length=65)
    product_brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    product_material = models.ForeignKey(Material, on_delete=models.CASCADE)
    product_color = models.ForeignKey(Color, on_delete=models.CASCADE)
    product_size = models.ForeignKey(Size, on_delete=models.CASCADE)
    product_catalog = models.ForeignKey(Catalog, on_delete=models.CASCADE)
    product_photo = models.ImageField()
    product_photo1 = models.ImageField(null=True, blank=True)
    product_photo2 = models.ImageField(null=True, blank=True)
    product_photo3 = models.ImageField(null=True, blank=True)
    product_photo4 = models.ImageField(null=True, blank=True)
    product_photo5 = models.ImageField(null=True, blank=True)
    product_photo6 = models.ImageField(null=True, blank=True)
    product_photo7 = models.ImageField(null=True, blank=True)
    product_photo8 = models.ImageField(null=True, blank=True)
    product_photo9 = models.ImageField(null=True, blank=True)


class Reviews(models.Model):
    reviews_username = models.ForeignKey(User, on_delete=models.CASCADE)
    reviews_rating = models.IntegerField()
    reviews_text = models.CharField(max_length=1000)
    reviews_product = models.ForeignKey(ProductIdentificate, on_delete=models.CASCADE)


class Cart(models.Model):
    codes = models.IntegerField()
    user = models.OneToOneField(User, on_delete=models.CASCADE)


class OrderList(models.Model):
    account = models.ForeignKey(User, default=-1, on_delete=models.SET_DEFAULT)
    product_code = models.IntegerField()
    product_count = models.IntegerField()
    client_name = models.CharField(max_length=20)
    client_surename = models.CharField(max_length=20)
    client_email = models.EmailField()
    client_city = models.CharField(max_length=40)
    client_address = models.CharField(max_length=100)
