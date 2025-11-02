from django.db import models

class OrderStatus(models.Model):
    name = models.CharField(max_length=50, unique=True)
    PENDING = 'pending'
    PROCESSING = 'processing'
    COMPLETED = 'completed'
    CANCELLED = 'cancelled'

    def __str__(self):
        return self.name
class Order(models.Model):
    order_id = models.CharField(max_length=100)
    customer = models.CharField(max_length=100)

    status = models.ForeignKey(OrderStatus, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.order_id