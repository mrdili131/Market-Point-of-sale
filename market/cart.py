from .models import Market, Product

class Cart:
    def __init__(self,request):
        self.session = request.session
        self.cart = self.session.get('cart',{})

    def add(self,product_id,quantity):
        prod = Product.objects.get(id=product_id)

        if product_id in self.cart:
            new = self.cart[str(product_id)]['quantity'] = int(self.cart[str(product_id)]['quantity'])+int(quantity)
            if new <= prod.quantity:
                self.cart[str(product_id)]['quantity'] = new
                self.session['cart'] = self.cart
                self.session.modified = True
            else:
                pass
        else:
            if int(quantity) > 0 :
                self.cart[str(product_id)] = {
                    'name':str(prod.name),
                    'price':str(prod.price),
                    'quantity':str(quantity),
                    'total':str(int(quantity)*int(prod.price))
                }
            for key,value in self.cart.items():
                if prod.name == value["name"]:
                    if (int(prod.quantity)+int(value["quantity"]))>int(quantity):
                        self.session['cart'] = self.cart
                        self.session.modified = True
                        print(self.cart)

    def delete(self,product_id):
        del self.cart[str(product_id)]
        self.session['cart'] = self.cart
        self.session.modified = True
        print(self.cart)

    def view_cart(self):
        print("\n\n",self.cart,"\n\n")

    def clean(self):
        self.cart = {}
        self.session['cart'] = self.cart
        self.session.modified = True