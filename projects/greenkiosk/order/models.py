

from django.db import models
from payment.models import Payment
# from shipmping.models import Shipping
from customer.models import Customer
from cart.models import Cart

class Order(models.Model):
    payment = models.OneToOneField(Payment, on_delete=models.PROTECT, null=True)
    shipping = models.OneToOneField(Shipping, on_delete=models.PROTECT, null=True)
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT, null=True)
    cart = models.OneToOneField(Cart, on_delete=models.PROTECT, null=True)
    order_name = models.CharField(max_length=32)
    order_id = models.CharField(max_length=32)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    order_status = models.CharField(max_length=32)
    number_of_orders = models.IntegerField()
    stock_amount = models.IntegerField()

    def __str__(self):
        return self.order_status
