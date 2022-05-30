from django.urls import path
from SellingCarsApp import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    #path("", views.home, name="home"),
    path("", views.CarListView.as_view(), name="car_list"),
    path("addcar/", views.CarSellerView.as_view(), name="addcar"),
    path("thanku/", views.showGreetings, name="greeting"),
    path("buyerinfo/<int:id>/", views.addBuyer, name="buyerinfo"),
    path("sendmail/<int:id>/", views.sendEmail, name="informdealer"),
    path("login/", views.signin, name="login"),
    path("postsignIn/", views.postsignIn, name="postsignIn"),
    path("buy/", views.sendEmail),
    path('logout/', auth_views.LogoutView.as_view(template_name="home.html"), name='logout'),
    
    

]
