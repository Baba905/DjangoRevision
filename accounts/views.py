from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import *
# Create your views here.

def home(request):
    total_order= Order.objects.count()
    delivred_order = Order.objects.filter(status="Delivered").count()
    pending_order = Order.objects.filter(status='Pending').count()
    customers= Customer.objects.all()
    orders = Order.objects.all().order_by('-date_created')
    context={
        "total_order":total_order, 
        "delivered_order": delivred_order,
        "pending_order" : pending_order,
        "customers": customers,
        "orders":orders,
    }
    return render(request, 'accounts/dashboard.html', context)

def customer(request,customer_id):
    customer = Customer.objects.get(id=customer_id)
    context={'customer':customer}
    return render(request,'accounts/customer.html', context)

def products(request):
    products = Product.objects.all()
    context ={'products':products}
    return render(request,'accounts/products.html',context)

#CRUD Order
def create_order(request):
    if request.method=='POST':
        form=OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form=OrderForm()
    context= {'form':form}
    return render(request, 'accounts/order.html',context)

def update_order(request, pk):
    order = Order.objects.get(id= pk)
    
    if request.method=='POST':
        form=OrderForm(request.POST, instance=order)
        form.save()
        return redirect('/')
    else:
        form=OrderForm(instance=order)
    context ={'form':form}
    return render(request, 'accounts/order.html', context)


def delete_order(request, pk):
    order= Order.objects.get(id=pk)
    if request.method=='POST':
        order.delete()
        return redirect('/')
    context= {'item':order}
    return render(request, 'accounts/delete.html', context)


#CRUD Customer

def create_customer(request):
    if request.method=='POST':
        form=CustomerForm(request.POST)
        if form.is_valid():
                form.save()
                return redirect('/')
    else:
        form=CustomerForm()
    context= {'form':form}
    return render(request, 'accounts/order.html',context)


def update_customer(request,pk):
    customer = Customer.objects.get(id= pk)
    
    if request.method=='POST':
        form=CustomerForm(request.POST, instance=customer)
        form.save()
        return redirect('/')
    else:
        form=CustomerForm(instance=customer)
    context ={'form':form}
    return render(request, 'accounts/order.html', context)

def delete_customer(request, pk):
    customer = Customer.objects.get(id=pk)
    if request.method=='POST':
        customer.delete()
        return redirect('/')
    context= {'item':customer}
    return render(request, 'accounts/delete_customer.html', context)

# *************** CRUD Product************************
def add_product(request):
    if request.method=='POST':
        form=ProductForm(request.POST)
        if form.is_valid():
                form.save()
                return redirect('/')
    else:
        form=ProductForm()
    context= {'form':form}
    return render(request, 'accounts/order.html',context)


def update_product(request,pk):
    product = Product.objects.get(id= pk)
    
    if request.method=='POST':
        form=ProductForm(request.POST, instance=product)
        form.save()
        return redirect('/')
    else:
        form=ProductForm(instance=product)
    context ={'form':form}
    return render(request, 'accounts/order.html', context)

def delete_product(request,pk):
    product = Product.objects.get(id=pk)
    if request.method=='POST':
        product.delete()
        return redirect('/')
    context= {'item':product}
    return render(request, 'accounts/delete_product.html', context)
#Update to e-commerce web app
def login(request):
    context={}
    return render(request,'accounts/login.html', context)

def register(request):
    form = RegistrationForm()
    if request.method=='POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form=RegistrationForm()
    context={'form':form}
    return render(request,'accounts/register.html', context)