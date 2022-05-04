from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.views.generic import DetailView
from .models import Product, Cart, OrderList, Material, Brand, Color, Size, Reviews, ProductIdentificate


class ProductDetail(DetailView):
    model = Product
    template_name = 'product.html'
   # context_object_name = 'product'

    def post(self, request, *args, **kwargs):
        if request.POST.get('review'):
            review = request.POST.get("review", "")
            review_text = request.POST.get('review_text')
            if review_text:
                review_product = ProductIdentificate.objects.get(product_number=review)
                review = Reviews(reviews_username=request.user, reviews_rating=0, reviews_text=review_text, reviews_product=review_product)
                review.save()
        if request.POST.get('mybtn'):
            product = request.POST.get("mybtn", "")
            j = ""
            for n, y in enumerate(product):
                if y == "0" or y == "1" or y == "2" or y == "3" or y == "4" or y == "5" or y == "6" or y == "7" or y == "8" or y == "9":
                    j += y
            number = int(j)
            if request.user.is_authenticated:
                obj, created = Cart.objects.get_or_create(codes=number, user=request.user)
                if created:
                    pass
                else:
                    return redirect('cart/')
            else:
                return redirect('authorization/')
        return redirect('main')

    def get_context_data(self, *args, **kwargs):
        context = super(ProductDetail, self).get_context_data(**kwargs)
        context['reviews'] = Reviews.objects.all()
        return context


def main(request):
    numbering = request.session.get('count', 1)
    request.session['count'] = numbering + 1
    products = Product.objects.all()
    materials = Material.objects.all()
    brands = Brand.objects.all()
    sizes = Size.objects.all()
    colors = Color.objects.all()
    if request.GET.get('search'):
        search_words = request.GET.get('search')
        products = Product.objects.filter(product_name__contains=search_words)
        return render(request, 'index_non.html', context={'numbering': numbering, 'products': products, 'brands': brands,
                                                      'colors': colors, 'materials': materials, 'sizes': sizes}, )
    if request.POST.get('filter'):
        mat = request.POST.get('mat')
        brn = request.POST.get('brn')
        col = request.POST.get('col')
        siz = request.POST.get('siz')
        if mat and brn and col and siz:
            products = Product.objects.filter(product_brand=brn, product_material=mat, product_color=col, product_size=siz)
        elif mat and brn and col:
            products = Product.objects.filter(product_brand=brn, product_material=mat, product_color=col)
        elif mat and brn and siz:
            products = Product.objects.filter(product_brand=brn, product_material=mat, product_size=siz)
        elif brn and col and siz:
            products = Product.objects.filter(product_brand=brn, product_color=col, product_size=siz)
        elif mat and brn:
            products = Product.objects.filter(product_brand=brn, product_material=mat)
        elif mat and col:
            products = Product.objects.filter(product_material=mat, product_color=col)
        elif mat and siz:
            products = Product.objects.filter(product_material=mat, product_size=siz)
        elif brn and siz:
            products = Product.objects.filter(product_brand=brn, product_size=siz)
        elif brn and col:
            products = Product.objects.filter(product_brand=brn, product_color=col)
        elif siz and col:
            products = Product.objects.filter(product_color=col, product_size=siz)
        elif mat:
            products = Product.objects.filter(product_material=mat)
        elif brn:
            products = Product.objects.filter(product_brand=brn)
        elif col:
            products = Product.objects.filter(product_color=col)
        elif siz:
            products = Product.objects.filter(product_size=siz)
        return render(request, 'index.html',
                      context={'numbering': numbering, 'products': products, 'brands': brands, 'colors': colors,
                               'materials': materials, 'sizes': sizes, }, )
    if request.POST.get('mybtn'):
        product = request.POST.get("mybtn", "")
        j = ""
        for n, y in enumerate(product):
            if y == "0" or y == "1" or y == "2" or y == "3" or y == "4" or y == "5" or y == "6" or y == "7" or y == "8" or y == "9":
                j += y
        number = int(j)
        if request.user.is_authenticated:
            obj, created = Cart.objects.get_or_create(codes=number, user=request.user)
            if created:
                pass
            else:
                return redirect('cart/')
        else:
            return redirect('authorization/')
    return render(request, 'index.html', context={'numbering': numbering, 'products': products, 'brands': brands,
                                                  'colors': colors, 'materials': materials, 'sizes': sizes},)


def authorization(request):
    if request.user.is_authenticated:
        cart_obj = OrderList.objects.filter(account=request.user)
        x = []
        for n, c in enumerate(cart_obj):
            code = c.product_code
            x.append(Product.objects.get(product_number=code))
        products = x
        return render(request, 'profile.html', context={'carts': cart_obj, 'products': products})
    else:
        return render(request, 'authorization.html')


def exit(request):
    logout(request)
    return redirect('/')


def cart(request):
    if request.user.is_authenticated:
        if request.POST.get('order'):
            codes = request.POST.get('order', '')
            j = ""
            for n, y in enumerate(codes):
                if y == "0" or y == "1" or y == "2" or y == "3" or y == "4" or y == "5" or y == "6" or y == "7" or y == "8" or y == "9":
                    j += y
            code = int(j)
            count = request.POST.get('count')
            name = request.POST.get('name')
            surename = request.POST.get('surename')
            email = request.POST.get('email')
            city = request.POST.get('city')
            address = request.POST.get('address')
            order = OrderList(account=request.user, product_code=code, product_count=count, client_name=name,
                              client_surename=surename, client_email=email, client_city=city, client_address=address)
            order.save()
            item = Cart.objects.get(user=request.user, codes=code)
            item.delete()
            return redirect('main')
        if request.POST.get('buy'):
            codes = request.POST.get('buy', '')
            j = ""
            for n, y in enumerate(codes):
                if y == "0" or y == "1" or y == "2" or y == "3" or y == "4" or y == "5" or y == "6" or y == "7" or y == "8" or y == "9":
                    j += y
            code = int(j)
            product = Product.objects.get(product_number=code)
            return render(request, 'order.html', context={'product': product})
        if request.POST.get('cancel'):
            codes = request.POST.get('cancel', '')
            j = ""
            for n, y in enumerate(codes):
                if y == "0" or y == "1" or y == "2" or y == "3" or y == "4" or y == "5" or y == "6" or y == "7" or y == "8" or y == "9":
                    j += y
            code = int(j)
            item = Cart.objects.get(user=request.user, codes=code)
            item.delete()
            return redirect('cart')
        carts_objects = Cart.objects.filter(user=request.user)
        x = []
        for n, c in enumerate(carts_objects):
            code = c.codes
            x.append(Product.objects.filter(product_number=code))
        products = x
        return render(request, 'cart.html', context={'carts': carts_objects, 'products': products})
    else:
        return render(request, 'authorization.html')


def singup(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        userCreate = User.objects.create_user(username, email, password)
        userCreate.save()
        return redirect("main")
    else:
        return render(request, 'singup.html')


def singin(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("main")
        else:
            return render(request, "404")
    return render(request, 'singin.html')


def ff(request):
    return render(request, "404.html")
