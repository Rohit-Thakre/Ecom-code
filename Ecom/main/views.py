from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, logout, authenticate
# Create your views here.
from .models import User, Order, Review, Address, Category, Product, Cart_item, Banner

from .forms import RegisterForm
from .forms import LoginForm


def user_login(request):

    if request.method == 'POST':
        email = request.POST.get('email', '')
        password = request.POST.get('password', '')

        email_check = User.objects.filter(email=email)
        if email_check:
            instance = authenticate(email=email, password=password)
            if instance:
                login(request, instance)
                return redirect('home')
            else:
                return render(request, 'login.html', {'val': True,  'msg': "Password Incorrect !"})

        else:
            return render(request, 'login.html', {'val': True,  'msg': "No account with this email"})

    return render(request, 'login.html', {'val': False})


def user_logout(request):
    logout(request)
    return redirect('home')


def register(request):
    if request.method == 'POST':
        full_name = request.POST.get('full_name', '')
        email = request.POST.get('email', '')
        pass1 = request.POST.get('pass1', '')
        pass2 = request.POST.get('pass2', '')

        if full_name != '' and email != '' and pass1 != pass2:
            return render(request, 'register.html', {'val': True, 'msg': 'Fill all fields !'})

        if pass1 != pass2:
            return render(request, 'register.html', {'val': True, 'msg': 'passwords are different !'})

        else:
            user_obj = User(full_name=full_name, email=email)
            user_obj.set_password(pass1)
            user_obj.save()
            login(request, user_obj)
            return redirect('home')

    return render(request, 'register.html')


def home(request):

    banners = Banner.objects.all()
    products = Product.objects.all()
    context = {'products': products, 'banners': banners}
    return render(request, 'home.html', context)


def add_product(request):
    category_list = Category.objects.all()
    if request.method == 'POST':
        product_name = request.POST.get('product_name', '')
        category = request.POST.get('category', '')
        obj, craeted = Category.objects.get_or_create(type=category)
        stock = request.POST.get('stock', '')
        mrp = request.POST.get('mrp', '')
        selling_price = request.POST.get('selling_price', '')
        img = request.POST.get('img', '')
        description = request.POST.get('description', '')

        # print(product_name, category, stock, mrp,
        #       selling_price, img, description)
        product_obj = Product(name=product_name, category=obj, stock=stock,
                              max_price=mrp, current_price=selling_price, image=img, description=description, merchant=request.user)
        product_obj.save()

        return HttpResponse('data saved.')

    return render(request, 'add_product.html', {'category_list': category_list})


def be_merchant(request):
    print(request.user.email)
    if request.method == 'POST':
        avatar = request.POST.get('avatar', '')

        # print(avatar)
        merchant = request.POST.get('merchant', '')
        merchant = True if merchant == 'True' else False

        age = request.POST.get('age', '')
        number = request.POST.get('phone', '')

        street = request.POST.get('street', '')
        area = request.POST.get('area', '')
        city = request.POST.get('city', '')

        pin = request.POST.get('pin', '')
        state = request.POST.get('state', '')
        country = request.POST.get('country', '')

        address_instance = Address(
            user=request.user, street=street, area=area, city=city, country=country, pin=pin, state=state)
        address_instance.save()

        user_instance = User.objects.get(email=request.user.email)
        user_instance.age = age
        # print(avatar)
        # if avatar:
        #     user_instance.avatar = avatar
        #     print('img set')
        user_instance.merchant = merchant
        user_instance.number = number
        user_instance.save()
        print('set all.')

    return render(request, 'be_merchant_form.html')


def cart(request):
    total = 0
    current_price = 0
    off = 0

    cart = Cart_item.objects.filter(user=request.user)
    for x in cart:
        total += int(x.product.max_price)
        current_price += int(x.product.current_price)

    context = {'cart': cart, 'total': total,
               'current_price': current_price, 'off': total - current_price}
    return render(request, 'cart.html', context)


def add_to_cart(request, key):
    product = Product.objects.get(id=key)
    try:
        cart_obj = Cart_item(product=product, count=1, user=request.user)
        cart_obj.save()
    except:
        pass
    return redirect('cart')


def remove_from_cart(request, key):
    item = Cart_item.objects.get(product__id=key)
    if item:
        item.delete()
        # return HttpResponse('product removed')
    return redirect('cart')


def product(request, key):

    product = Product.objects.get(id=key)
    products = Product.objects.all()
    off = int(product.max_price) - int(product.current_price)
    reviews = Review.objects.filter(product=product)
    context = {'product': product, 'reviews': reviews,
               'off': off, 'products': products}
    return render(request, 'product-view.html', context)


def category_list(request, type):

    products = Product.objects.filter(category__type=type)
    context = {'products': products}
    return render(request, 'product-list.html', context)


def account(request):
    user = User.objects.get(full_name=request.user)
    address = None
    try:
        address = Address.objects.get(user=user)
    except:
        pass
    orders = Order.objects.filter(user=request.user)

    context = {'user': user, 'address': address, 'orders': orders}

    return render(request, 'account.html', context)


def edit_profile(request):

    user = User.objects.get(email=request.user.email)
    address = Address.objects.filter(user=request.user)

    msg = ''
    show = 0

    if request.method == 'POST':
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')

        # print(name, email, phone)
        if name and email and phone:
            user.full_name = name
            user.email = email
            user.number = phone
            user.save()
            msg = 'User data saved'
            show = 1

        street = request.POST.get('street', '')
        area = request.POST.get('area', '')
        city = request.POST.get('city', '')
        state = request.POST.get('state', '')
        country = request.POST.get('country', '')
        pin = request.POST.get('pin', '')

        if street and area and city and state and country and pin:
            adrs_obj = Address.objects.create(
                street=street, area=area, city=city, state=state, country=country, pin=pin, user=request.user)
            adrs_obj.save()
            msg += 'Address saved'
            show = 1

    context = {'user': user, 'address': address, 'msg': msg, 'show': show}
    return render(request, 'edit_profile.html', context)


def remove_address(request, key):

    pass
