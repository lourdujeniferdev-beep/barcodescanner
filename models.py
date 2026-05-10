from django.db import models

class Product(models.Model):
    qr_code = models.CharField(max_length=200, unique=True)
    name = models.CharField(max_length=100)
    price = models.FloatField()   # ✅ correct indentation

    def __str__(self):
        return f"{self.name} ({self.qr_code})"