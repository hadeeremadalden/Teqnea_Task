from django.db import models
from category.models import Category

# Create your models here.

class Product(models.Model):
    Name = models.JSONField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    Price = models.DecimalField(max_digits=8, decimal_places=2)
    Image = models.ImageField(blank= True , null = True)

    def __str__(self):
        return str(self.Name)
   
