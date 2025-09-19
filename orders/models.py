
from django.db import models
from products.models import Product

ORDER_STATUS_CHOICES = [
	("pending", "Pending"),
	("processing", "Processing"),
	("shipped", "Shipped"),
	("delivered", "Delivered"),
	("cancelled", "Cancelled"),
]

class Order(models.Model):
	customer_name = models.CharField(max_length=100)
	customer_email = models.EmailField()
	created_at = models.DateTimeField(auto_now_add=True)
	status = models.CharField(max_length=20, choices=ORDER_STATUS_CHOICES, default="pending")

	def __str__(self):
		return f"Order #{self.id} - {self.customer_name}"

class OrderItem(models.Model):
	order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="items")
	product = models.ForeignKey(Product, on_delete=models.CASCADE)
	quantity = models.PositiveIntegerField(default=1)
	price = models.DecimalField(max_digits=10, decimal_places=2)

	def __str__(self):
		return f"{self.product.name} x {self.quantity}"
