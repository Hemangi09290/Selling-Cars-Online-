from django.db import models
import datetime
# Create your models here.


class Seller(models.Model):
    car_condition = (
        ('poor', 'Poor'),
        ('fair', 'Fair'),
        ('good', 'Good'),
        ('excellent', 'Excellent'),
    )

    year_choices = (
        [(r,r) for r in range(1950, datetime.date.today().year+1)]
    )


    name = models.CharField(max_length=200)
    mobile = models.BigIntegerField()
    make = models.CharField(max_length=200)
    model = models.CharField(max_length=200)
    year = models.IntegerField(max_length=5, choices=year_choices)
    condition = models.CharField(max_length=10, choices=car_condition)
    price = models.PositiveIntegerField()
    is_sold = models.BooleanField(default=False)

class User(models.Model):
    username = models.CharField(max_length=200)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    password = models.CharField(max_length=100, help_text='Enter 8 digits password')
    email = models.EmailField()
    mobile = models.CharField(max_length=200)
    is_makecar_avail = models.BooleanField(default=False)
    last_login = models.DateTimeField(null=True)
    
