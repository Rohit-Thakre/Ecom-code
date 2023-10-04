from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class User(AbstractUser):
    name = models.CharField(max_length=150)
    email = models.EmailField(unique=True)

    number = models.CharField(max_length=15, null=True)
    verified = models.BooleanField(default=False)
    age = models.PositiveIntegerField(null=True)
    merchant = models.BooleanField(default=False)
    avatar = models.ImageField(
        null=True, default="avatar.svg", upload_to='user/')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self) -> str:
        return str(self.name)


class Address(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=20)
    country = models.CharField(max_length=10)
    pin = models.CharField(max_length=6)
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
    max_price = models.CharField(max_length=10)
    last_price = models.CharField(max_length=10)
    current_price = models.CharField(max_length=10)

    description = models.TextField()
    image = models.ImageField(upload_to='product/')

    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.name) + str(self.current_price)


class Cart_item(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE)
    count = models.PositiveIntegerField(default=1)
    current_price = models.CharField(max_length=10)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.product)


class Cart(models.Model):
    items = models.ForeignKey(Cart_item, on_delete=models.CASCADE)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.user)


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

    def __str__(self):
        return str(self.user)


class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    text = models.TextField()
    img = models.ImageField(upload_to='review/', null=True, blank=True)
    rating = models.PositiveIntegerField()
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.user) + str(self.product)
