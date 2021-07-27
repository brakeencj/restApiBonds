from django.db import models
from django import forms
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils import timezone


class User(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=30)
    created = models.DateTimeField(
        auto_now_add=True, editable=False)
    updated = models.DateTimeField(auto_now=True, editable=False)

    def __str__(self):
        return self.name

    class Import:
        file = 'users'


class Bond(models.Model):
    STATUS = (
        ('o', 'on sale'),
        ('p', 'purchased')
    )
    name = forms.CharField(max_length=40, min_length=3)
    number = models.IntegerField(default=1, validators=[MaxValueValidator(10000),
                                                        MinValueValidator(1)])
    price = models.DecimalField(max_digits=13, decimal_places=4,
                                validators=[MaxValueValidator(100000000), MinValueValidator(0)])
    status = models.CharField(max_length=1, choices=STATUS, default="o")
    seller = models.ForeignKey(User, on_delete=models.PROTECT)
    buyer = models.ForeignKey(User, models.SET_NULL, related_name="buyer", blank=True,
                              null=True)
    created = models.DateTimeField(
        auto_now_add=True, editable=False)
    updated = models.DateTimeField(auto_now=True, editable=False)

    def __str__(self):
        return self.name

    class Import:
        file: 'bonds'
        fields_map: {'seller': 'user_id', 'buyer': 'user_id'}
