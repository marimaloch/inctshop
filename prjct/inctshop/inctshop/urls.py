from django.contrib import admin
from django.urls import path
from catalog import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.main, name="main"),
    path('authorization/', views.authorization, name="authorization"),
    path('singin/', views.singin, name="singin"),
    path('singup/', views.singup, name="singup"),
    path('404', views.ff, name="404"),
    path('cart/', views.cart, name="cart"),
    path('profile/', views.authorization, name="authorization"),
    path('logout/', views.exit, name="logout"),
    path('<int:pk>', views.ProductDetail.as_view(), name="product"),
]
