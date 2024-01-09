from django.db import models

# Create your models here.
class Owner(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)


class Car(models.Model):
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)
    license_plate = models.CharField(max_length=10)
    car_model = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
