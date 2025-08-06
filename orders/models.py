from django.db import models
from django.contrib.auth.models import User
from products.models import Menu

class Order(models.Model):
    STATUS_CHOICES = [
        ('PENDING', 'Pending'),
        ('CONFIRMED', 'Confirmed'),
        ('DELIVERED', 'Delivered'),
        ('CANCELLED', 'Cancelled'),
    ]

customer = models.ForeignKey(User, on_delete =models.CASCADE)
Menu_item = models.ForeignKey(Menu, on_delete=models.CASCADE)
quantity = models.positiveIntegerField()
total_amount = models.DecimalField(max_digits=10, decimal_places=2)
status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='PENDING')
created_at = models.DateTimeField(auto_now_add=True)

def __str__(self):
    return f"{self.customer.username} - {self.menu_item.name} - {self.status}"
