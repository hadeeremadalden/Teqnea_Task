from django.db import models

# Create your models here.


class Category(models.Model):
    Name = models.JSONField()

    def __str__(self):
        return str(self.Name)
   

   
