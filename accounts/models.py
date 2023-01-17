from django.db import models

# Create your models here.

class Customer(models.Model):
    name = models.CharField(max_length=255, null= True)
    phone = models.CharField(max_length=255, null= True)
    email = models.EmailField(max_length=255, null= True)
    date_created = models.DateTimeField(auto_now_add= True, null= True)

    def __str__(self) -> str:
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=255, null=True)

    def __str__(self) -> str:
        return self.name


class Product(models.Model):
    CATEGORY=(
        ('Indoor', 'Indoor'),
        ('Out door','Out door'),
    )
    name = models.CharField(max_length=255, null= True)
    price = models.FloatField(null= True)
    category = models.CharField(max_length=255, null= True, choices=CATEGORY)
    description = models.CharField(max_length=255, null= True)
    date_created = models.DateTimeField(auto_now_add= True, null= True, blank=True)
    tag = models.ManyToManyField(Tag)

    def __str__(self) -> str:
        return self.name

class Order(models.Model):
    STATUS=(
        ('Pending', 'Pending'),
        ('Out of delivery', 'Out of delivery'),
        ('Delivered', 'Delivered'),
    )
    customer = models.ForeignKey(Customer, on_delete= models.CASCADE, null=True,  related_name="orders")
    product = models.ForeignKey(Product, on_delete= models.CASCADE, null=True)
    date_created = models.DateTimeField(auto_now_add= True, null= True)
    status = models.CharField(max_length=255,null =True, choices=STATUS)

    def __str__(self) -> str:
        return self.product.name
