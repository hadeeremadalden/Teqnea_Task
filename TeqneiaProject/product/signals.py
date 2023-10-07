from django.db.models.signals import pre_save
from django.dispatch import receiver
from product.models import Product

@receiver(pre_save, sender=Product)
def limit_products_in_category(sender, instance, **kwargs):
    if instance.category.products.count() >= 5:
        raise ValueError("Cannot add more than 5 products in a category.")