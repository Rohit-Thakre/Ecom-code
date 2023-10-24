from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class User(AbstractUser):
    full_name = models.CharField(max_length=150, null=True, blank=True)
    email = models.EmailField(unique=True)

    number = models.CharField(max_length=15, null=True, blank=True)
    verified = models.BooleanField(default=False)
    age = models.PositiveIntegerField(null=True, blank=True)
    merchant = models.BooleanField(default=False, null=True, blank=True)
    avatar = models.ImageField(
        null=True, default="user/avatar.jpg", upload_to='user/')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'full_name']

    def __str__(self) -> str:
        return str(self.full_name)


class Address(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    street = models.CharField(max_length=50)
    area = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=20)
    country = models.CharField(max_length=10, default='india')
    pin = models.IntegerField()
    selected = models.BooleanField(default=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.city)


class Category(models.Model):
    type = models.CharField(max_length=50)
    by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.type)


class Product(models.Model):
    name = models.CharField(max_length=50)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    max_price = models.CharField(max_length=10)
    last_price = models.CharField(max_length=10, null=True)
    current_price = models.CharField(max_length=10)

    description = models.TextField()
    image = models.ImageField(upload_to='product/')

    merchant = models.ForeignKey(User, on_delete=models.CASCADE)

    stock = models.PositiveBigIntegerField()
    likes = models.PositiveBigIntegerField(null=True)
    dislikes = models.PositiveBigIntegerField(null=True)
    # rating = models.PositiveIntegerField()

    total_orders = models.PositiveIntegerField(null=True)

    def __str__(self):
        return str(self.name) + str(self.current_price)


class Cart_item(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE)
    count = models.PositiveIntegerField(default=1)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.product)


class Order(models.Model):
    payment_CHOICES = (
        ('upi', 'upi'),
        ('cod', 'cash on delivery'),
    )
    payment_method = models.CharField(max_length=10, choices=payment_CHOICES)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    CHOICES_status = (
        ('processing', 'Processing'),
        ('shipped', 'shipped'),
        ('delivered', 'delivered'),
        ('cancelled', 'cancelled'),
    )
    status = models.CharField(max_length=10, choices=CHOICES_status)
    product = models.ForeignKey(Cart_item, on_delete=models.CASCADE)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.user) + str(Product)


class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    text = models.TextField()
    img = models.ImageField(upload_to='review/', null=True, blank=True)
    rating = models.PositiveIntegerField()
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    likes = models.PositiveIntegerField()
    dislikes = models.PositiveIntegerField()

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.user) + str(self.product)
