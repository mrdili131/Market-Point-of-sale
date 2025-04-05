from django.contrib import admin
from .models import Market, Product, Order, OrderItem

admin.site.register([Market, Product, Order, OrderItem])