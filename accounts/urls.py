from django.urls import path
from accounts import views
urlpatterns=[
    path('',views.home, name='home'),
    path('customer/<int:customer_id>', views.customer, name='customer'),
    path('products', views.products,name='products'),
    path('create_order', views.create_order, name="create_order"),
    path('update_order/<int:pk>', views.update_order, name='update_order'),
    path('delete/<int:pk>', views.delete_order,name='delete'),
    path('create_customer', views.create_customer, name='create_customer'),
    path('update_customer/<int:pk>', views.update_customer,name='update_customer'),
    path('delete_customer/<int:pk>',views.delete_customer,name='delete_customer'),
    path('add_product', views.add_product, name='add_product'),
    path('update_product/<int:pk>', views.update_product,name='update_product'),
    path('delete_product/<int:pk>',views.delete_product, name="delete_product"),

    path('register',views.register, name='register'),
    path('login', views.login, name='login'),
]