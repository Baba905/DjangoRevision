from django.contrib import admin
from .models import *
# Register your models here.

class CustomerAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone', 'date_created']

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'category', 'date_created']

class OrderAdmin(admin.ModelAdmin):
    list_display = ['customer','product','status', 'date_created']

class TagAdmin(admin.ModelAdmin):
    list_display = ['name']

admin.site.register(Customer,CustomerAdmin)
admin.site.register(Product,ProductAdmin)
admin.site.register(Order,OrderAdmin)
admin.site.register(Tag,TagAdmin)