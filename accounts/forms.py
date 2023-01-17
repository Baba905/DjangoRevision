from django.forms import ModelForm
from .models import Order,Customer, Product
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
#***********************
class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields= ['customer','product', 'status']

class RegistrationForm(UserCreationForm):
    class Meta:
        model= User
        fields=['username','email', 'password1','password2']


class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields=['name','phone', 'email']

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'category', 'price']