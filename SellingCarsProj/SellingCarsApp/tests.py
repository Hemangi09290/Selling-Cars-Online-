from django.test import TestCase
from django.urls import reverse
from django.test.client import Client
from SellingCarsApp.models import Seller, User
# Create your tests here.

class UnitTest(TestCase):

    def create_seller(self):
        Seller.objects.create(
            name='seller abc',
            mobile='7384323451',
            make='Ford',
            model='Falcon',
            year=2001,
            condition='excellent',
            price=9000
        )

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create(
            username='mike@example.org',
            first_name='test',
            last_name='testing',
            password='mikeymike123',
            email='test@gmail.com',
            mobile='987654321',
            last_login='2022-05-28 19:12:37'
        )
        self.user.save()
        self.create_seller()

    def test_GETlogin(self):
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'Login.html')

    def test_POSTlogin(self):
        response = self.client.post(reverse('login'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'Login.html')

    def test_invalid_login_POST(self):
        response = self.client.post('/postsignIn/', {'username': 'testab', 'password': 'testab123'})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'Login.html')
        self.assertContains(response, 'Invalid Credentials!!Please ChecK your Data')

    def test_valid_login_POST(self):
        response = self.client.post('/postsignIn/', {'username': 'mike@example.org', 'password': 'mikeymike123'})
        self.assertEqual(response.status_code, 200)

    def test_add_valid_vehicle_data(self):
        response = self.client.post('/addcar/', data={
            "model": 'Commodore',
            "make": 'Holden',
            "condition": 'poor',
            "price": 6000,
            "name": 'seller pqr',
            "mobile": 7354231245,
            "year": 1990
        })
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'addcar_details.html')

    def test_add_invalid_vehicle_data(self):
        response = self.client.post('/addcar/', data={
            "model": 'Commodore',
            "make": 'Holden',
            "condition": 'poor',
            "price": 200,
            "name": 'seller pqr',
            "mobile": 7354231245,
            "year": 1990
        })
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'addcar_details.html')
        self.assertContains(response, 'Enter valid price between 1000 to 100000')

    def test_list_car(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')

    