from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Universitet(models.Model):
    name = models.CharField(max_length=100)
    manzil = models.CharField(max_length=255)
    oquvchilar_soni = models.IntegerField(default=100)
    ochilish_vaqti = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    

class Direktor(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    oytik = models.PositiveIntegerField()
    ishga_kelgan_vaqt = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
