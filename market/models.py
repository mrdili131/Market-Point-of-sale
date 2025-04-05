from django.db import models
from users.models import User
import uuid

class Market(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name}'
    
class Product(models.Model):
    name = models.CharField(max_length=50)
    quantity = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    market = models.ForeignKey(Market,on_delete=models.CASCADE,related_name='products')
    is_available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if self.quantity == 0:
            self.is_available = False
        else:
            self.is_available = True
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.name} | 1x = {self.price} so\'m | qoldi {self.quantity} dona | jami {int(self.quantity*int(self.price))} so\'m'
    

class Order(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    order_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.order_id} {self.total_price} so\'m {self.created_at} vaqtida'

class OrderItem(models.Model):
    order = models.ForeignKey(Order,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.product.name} x{self.quantity} {self.price} so\'m dan'
