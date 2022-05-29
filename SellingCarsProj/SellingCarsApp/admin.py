from django.contrib import admin

# Register your models here.
from SellingCarsApp.models import Seller, User

admin.site.register(Seller)
admin.site.register(User)