from django.db import models
from django import forms
from django.core.validators import MaxValueValidator, MinValueValidator


class User(models.Model):
    name: models.CharField(max_length=50)
    email: models.EmailField(max_length=30)
    created: models.DateTimeField(auto_now_add=True)
    updated: models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Import:
        file = 'users'


class Bond(models.Model):
    name = forms.CharField(max_length=40, min_length=3)
    number = models.IntegerField(default=1, validators=[MaxValueValidator(10000),
                                                        MinValueValidator(1)])
    price = models.DecimalField(max_digits=13, decimal_places=4,
                                validators=[MaxValueValidator(100000000), MinValueValidator(0)])
    status = models.CharField(max_length=15, default="on sale")
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Import:
        file: 'bonds'
        fields_map: {'user': 'user_id'}


class Purchase(models.Model):
    bond = models.ForeignKey(Bond, on_delete=models.PROTECT)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.bond

    class Import:
        file: 'purchased'
        fields_map: {'bond': 'bond_id', 'user': 'user_id'}
