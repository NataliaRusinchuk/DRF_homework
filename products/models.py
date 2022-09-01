from django.db import models

class Product(models.Model):
    """Class for product model"""
    name = models.CharField(
        max_length=30        
    )
    description = models.CharField(
        max_length=500
    )
    price = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Order(models.Model):
    """Class for order model woth a foreing key of product"""
    product = models.ForeignKey(
        Product, 
        related_name='orders',
        on_delete = models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.product_name} ordred at {self.created_at}"
