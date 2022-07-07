from django.db import models

# class Manufacturer(models.Model):  # ishlab chiqarish
#     name = models.CharField(max_length=200)
#
#     def __str__(self):
#         return self.name
#
#
# class Model(models.Model):
#     name = models.CharField(max_length=35)
#
#     def __str__(self):
#         return self.name
from core.models import CustomUser


class Device(models.Model):  # qurilma
    manufacturer = models.CharField(max_length=30)  # ishlab chiqarish
    model = models.CharField(max_length=30)
    price = models.FloatField()
    actual_price = models.FloatField()
    is_active = models.BooleanField()

    def __str__(self):
        return self.model


class Client(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    fullname = models.CharField(max_length=35)
    birthdate = models.DateField()
    passport = models.CharField(max_length=35)
    image = models.ImageField(upload_to='images/')
    address = models.CharField(max_length=50)
    phone = models.CharField(max_length=30)

    def __str__(self):
        return self.fullname


class Loan(models.Model):  # qarz
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    created = models.DateTimeField()
    updated = models.DateTimeField()
    payed = models.FloatField()
    first_pay = models.FloatField()
    end_date = models.DateTimeField()
    month_pay = models.FloatField()


class LoadPayment(models.Model):  # kredit tulovi
    loan = models.ForeignKey(Loan, on_delete=models.CASCADE)
    amount = models.FloatField()
    created = models.DateTimeField()
    updated = models.DateTimeField()
    state = models.CharField(max_length=50)
