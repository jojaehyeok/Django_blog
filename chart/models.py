from django.db import models

# Create your models here.

class Stock(models.Model):
    name = models.CharField(max_length=20)
    code = models.CharField(max_length=9)
    ipo_date = models.DateField(null=True)
    def __str__(self):
        return self.name
