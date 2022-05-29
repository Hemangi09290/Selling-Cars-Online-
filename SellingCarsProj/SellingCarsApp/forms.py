from django import forms
from .models import User, Seller
from django.forms import fields
from django.contrib.auth.forms import UserCreationForm
import datetime

class UserForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'password', 'email']


class SellerForm(forms.ModelForm):
    
    def year_choices():
        return [(r,r) for r in range(1950, datetime.date.today().year+1)]

    def current_year():
        return datetime.date.today().year

    class Meta:
        model = Seller
        fields = ['name','mobile','make','model','year','condition','price']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
    def clean(self):
        cleaned_data = super(SellerForm, self).clean()
        price = int(cleaned_data.get("price"))

        if price not in range(1000, 100001):
            self.add_error('price', 'Enter valid price between 1000 to 100000')

        return cleaned_data
