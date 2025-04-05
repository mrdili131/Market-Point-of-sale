from django.shortcuts import render, redirect
from .models import Market, Product, Order, OrderItem
from django.views import View
from .cart import Cart
from django.http import JsonResponse
from django.contrib.auth.mixins import LoginRequiredMixin


class IndexView(View,LoginRequiredMixin):
    def get(self,request):
        market = Market.objects.get(user=request.user)
        prods = Product.objects.filter(market_id=market.id,is_available=True)
        orders = Order.objects.filter(user=request.user)
        session = request.session
        cart = session.get('cart',{})
        return render(request,'index.html',{"prods":prods,"cart":cart,"orders":orders})
    
def submit(request):
    cart_py = Cart(request)
    total = 0
    cart = request.session.get('cart',{})
    if cart != {}:
        order = Order.objects.create(
            user = request.user,
            total_price = 0
        )
        for key,value in cart.items():
            total = total + (float(value["price"])*int(value["quantity"]))
            print(value)
            prod = Product.objects.get(id=int(key))
            prod.quantity = int(prod.quantity) - int(value["quantity"])
            prod.save()
            OrderItem(
                order = order,
                product = prod,
                price = float(value["price"]),
                quantity = int(value["quantity"]),
            ).save()
            order.total_price = total
            order.save()
            cart_py.clean()
        return redirect("home")
    return redirect("home")
    
def add_cart(request):
    cart = Cart(request)
    if request.method == 'POST' and request.POST.get('action') == 'post':
        product_id = request.POST.get('product_id')
        quantity = request.POST.get('quantity')
        cart.add(product_id,quantity)
        print(cart.view_cart())
    return redirect('home')

def delete(request,product_id):
    cart = Cart(request)
    cart.delete(product_id)
    return redirect('home')

def clean_cart(request):
    cart = Cart(request)
    cart.clean()
    return JsonResponse({"status":True})

