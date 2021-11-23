from django.db import models

# Create your models here.
class Sellrecord(models.Model):
    customer_name = models.CharField(max_length=255)
   
   
    price = models.DecimalField(max_digits=7, decimal_places=2)
    showroom = models.CharField(max_length=255)
    paid = models.BooleanField(default=False)
    date = models.DateField()

    def __str__(self):
        return self.customer_name