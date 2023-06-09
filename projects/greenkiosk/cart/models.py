from django.db import models
from order import Order
# Create your models here.
class Cart(models.Model):
    cart=models.ForeignKey(Order,on_delete=models.CASCADE)
    price = models.IntegerField()
    number_of_products = models.IntegerField()
    product = models.CharField(max_length=255)
    shipment_cost = models.IntegerField()
    payment_options = models.CharField(max_length=255)
    def __str__(self):
        return f"Cart #{self.pk} - {self.product}"
