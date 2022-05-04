from django.contrib import admin
from .models import Catalog, Material, Brand, Color, Size, ProductIdentificate, Product, Reviews, User, Cart, OrderList

admin.site.register(Catalog)
admin.site.register(Material)
admin.site.register(Brand)
admin.site.register(Color)
admin.site.register(Size)
admin.site.register(Product)
admin.site.register(ProductIdentificate)
admin.site.register(Reviews)
admin.site.register(Cart)
admin.site.register(OrderList)




