from django.db.models import Q
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, logout, authenticate
# Create your views here.
from .models import Review_image, User, Order, Review, Address, Category, Product, Cart_item, Banner
from django.contrib.auth.decorators import login_required


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
        try:
            usr_obj = User.objects.get(email = email)
            if usr_obj: 
                return render(request, 'register.html', {'val': True, 'msg': 'Email Taken !'})
        except:
            pass


        if full_name != '' and email != '' and pass1 != pass2:
            return render(request, 'register.html', {'val': True, 'msg': 'Fill all fields !'})

        if pass1 != pass2:
            return render(request, 'register.html', {'val': True, 'msg': 'passwords are different !'})

        else:
            print(full_name, email, pass1)
            user_obj = User.objects.create(full_name=full_name, email=email, username = full_name+'+'+email)
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

from .forms import ProductForm
@login_required(login_url='login')
def add_product(request):
    category_list = Category.objects.all()
    show = 0
    msg = ''
    # form = ProductForm()
            
    if request.method == 'POST':

        

        product_name = request.POST.get('product_name', '')
        category = request.POST.get('category', '')
        obj, craeted = Category.objects.get_or_create(type=category)
        stock = request.POST.get('stock', '')
        mrp = request.POST.get('mrp', '')
        selling_price = request.POST.get('selling_price', '')
        # img = request.POST.get('img', '')
        img = request.FILES.get('img')
        description = request.POST.get('description', '')

        product_obj = Product(name=product_name, category=obj, stock=stock,
                              max_price=mrp, current_price=selling_price, image=img, 
                              description=description, merchant=request.user)
        product_obj.save()

        # form = ProductForm(request.POST, request.FILES, instance=product_obj)
        # if form.is_valid():
        #     form.save()

        msg = 'product added.'
        show = 1

    return render(request, 'add_product.html', {'category_list': category_list, 'msg': msg, 'show': show})

from .forms import UserForm
@login_required(login_url='login')
def be_merchant(request):
    address = Address.objects.filter(user=request.user).first()
    show = 0
    msg = ''

    user = User.objects.get(email = request.user.email)
    form = UserForm(instance=user)
    
    if request.method == 'POST':
        form = UserForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()

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

        address_instance = Address.objects.create(
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
        msg = 'Data Saved !'
        show = 1

        # return redirect('merchant_details')

    context = {'address': address, 'msg': msg, 'show': show, 'form':form}
    return render(request, 'be_merchant_form.html', context)

@login_required(login_url='login')
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

@login_required(login_url='login')
def add_to_cart(request, key):
    product = Product.objects.get(id=key)
    try:
        cart_obj = Cart_item(product=product, count=1, user=request.user)
        cart_obj.save()
    except:
        pass
    return redirect('cart')

@login_required(login_url='login')
def remove_from_cart(request, key):
    item = Cart_item.objects.filter(product__id=key).first()
    if item:
        item.delete()
        # return HttpResponse('product removed')
    return redirect('cart')


def product(request, key):

    product = Product.objects.get(id=key)
    products = Product.objects.all()
    off = int(product.max_price) - int(product.current_price)
    reviews = Review.objects.filter(product=product)

    for review in reviews: 
        review.image = Review_image.objects.filter(review= review)
    

    context = {'product': product, 'reviews': reviews,
               'off': off, 'products': products}
    
    return render(request, 'product-view.html', context)

def category_list(request, type):
    # q = request.GET.get('q')
    # q = q if q != None else ''
    # print(q)

    products = Product.objects.filter(category__type__icontains=type)
    context = {'products': products}
    return render(request, 'product-list.html', context)

@login_required(login_url='login')
def account(request):
    user = User.objects.get(email=request.user.email)
    address = None
    try:
        address = Address.objects.filter(user=user).first()
    except:
        pass
    orders = Order.objects.filter(user=request.user)

    context = {'user': user, 'address': address, 'orders': orders}

    return render(request, 'account.html', context)

@login_required(login_url='login')
def edit_profile(request):

    address = Address.objects.filter(user=request.user)
    msg = ''
    show = 0

    user = User.objects.get(email = request.user.email)
    form = UserForm(instance=user)
    
    if request.method == 'POST':

        form = UserForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()

        name = request.POST.get('name', None)
      
        phone = request.POST.get('phone', None)

 
        if name and phone:
            print(name,phone)
            user.full_name = name
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
        
        # return redirect('edit_profile')

    context = {'user': user, 'address': address, 'msg': msg, 'show': show,'form':form}
    return render(request, 'edit_profile.html', context)

@login_required(login_url='login')
def remove_address(request, key):

    address = Address.objects.get(id=key)
    address.delete()

    return redirect('edit_profile')


def new_category_list(request):
    q = request.GET.get('q')
    q = q if q != None else ''

    products = Product.objects.filter(
        Q(category__type__icontains=q) |
        Q(name__icontains=q)
    )
    context = {'products': products}
    return render(request, 'product-list.html', context)

# from .forms import ReviewForm
@login_required(login_url='login')
def review(request, key):

    show = 0
    msg = ''
    # form = ReviewForm()
    product = Product.objects.get(id=key)


    if request.method == 'POST':
        images = request.FILES.getlist('image')
        text = request.POST.get('text', '')
        rate = request.POST.get('rate', 0)

        review_obj = Review.objects.create(text=text, rating=rate, product = product,user= request.user)
        review_obj.save()

        for image in images:
            review_image = Review_image.objects.create(image = image, user = request.user, review = review_obj)
            review_image.save()



            



        # form = ReviewForm(request.POST, request.FILES, instance=review_obj)

        # if form.is_valid():
        #     form.save()

        show = 1
        msg = 'Review Added.'

    context = {'show': show, 'msg': msg}
    return render(request, 'reviewForm.html', context)



def like_product(request, key):
    
    product = Product.objects.get(id=key)
    product.likes  += 1 
    product.save()

    return redirect('product', key)

def dislike_product(request, key):
    
    product = Product.objects.get(id=key)
    product.dislikes  += 1 
    product.save()

    return redirect('product', key)


def order_address(request, key):
    address = Address.objects.filter(user__email = request.user.email)

    q = request.GET.get('q')
    q = q if q != None else ''
    selected_address = None
    adrs_obj = None
 
    if q != '': 
        selected_address = Address.objects.get(id =int(q))
    else:
        selected_address = address.first()

    if request.method =='POST':
        street = request.POST.get('street' )
        area = request.POST.get('area')
        city = request.POST.get('city')
        state = request.POST.get('state')
        country = request.POST.get('country')
        pin = request.POST.get('pin')

        if street and area and city and state and country and pin:
            adrs_obj,created  = Address.objects.get_or_create(
                street=street, area=area, city=city, state=state, country=country, pin=pin, user=request.user)
            adrs_obj.save()
            return redirect('payment_method', key, adrs_obj.id)

    context = {'address':address, 'selected_address':selected_address, 'key':key}    
    return render(request, 'order_address.html',context)


def cod(request, product_id, address_id):
    product = Product.objects.get(id=product_id)
    address = Address.objects.get(id=address_id)

    order = Order.objects.create(address = address, 
                                 payment_method='cod', user=request.user, 
                                 status ='processing', product=product)
    order.save()
    return redirect('home')


import razorpay
from django.conf import settings
client = razorpay.Client(auth=(settings.RAZOR_KEY, settings.RAZOR_SECRET))
def payment_method(request, product_id, address_id):

    product = Product.objects.get(id=product_id)
    address = Address.objects.get(id=address_id)
    
    payment_id = request.GET.get('payment_id')
    order_id = request.GET.get('order_id')
    signature = request.GET.get('signature')

    if payment_id and order_id: 
        order = Order.objects.create(payment_id = payment_id, order_id=order_id, 
                                        signature=signature,address = address, 
                                            payment_method = 'upi', user = request.user, status = 'processing', product = product)
        order.payment_method = 'upi'
        order.save()
        return redirect('home')
  
    data = { "amount": int(product.current_price)*100, "currency": "INR", "receipt": "order_rcptid_11" , 'payment_capture':1}
    payment = client.order.create(data=data)
    # context = {'payment' : payment, 'order_id': payment['id']}  

    conetxt = {'payment' : payment, 'order_id': payment['id'],'product_id': product_id, 'address_id':address_id}
    return render(request,'payment_method.html', conetxt)
    
