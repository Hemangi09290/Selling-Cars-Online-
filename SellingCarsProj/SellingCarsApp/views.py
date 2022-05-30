from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.template.loader import render_to_string
from django.views.generic.edit import FormView
from django.views.generic import ListView
from .forms import UserForm, SellerForm
from django.urls import reverse_lazy
from .models import User, Seller
from django.contrib.auth.models import auth
import smtplib
from django.contrib.auth import login, logout
from django.template.loader import render_to_string
from django.contrib import sessions
# Create your views here.

'''
This function shows home page of Dodg Brother site
and it will display list of cars if available 
along with Login button, List car button(to add new car) and Filter By to sort cars by filter
'''
def home(request):
    return render(request,"home.html")

'''
This function will add car details on add car form along
with seller information
'''
def getDetailsofCar(request):
    return render(request, "addcar_details.html")

def signin(request):
	return render(request,"Login.html")

def signoff(request):
    logout(request)
    return HttpResponseRedirect('/')

def showGreetings(request):
    return render(request, "greetings.html")

'''
This function will display buyer information form 
when enduser click to Buy car this will be called
'''
def addBuyer(request, id):
    context={}
    context["id"] = id
    return render(request, "buyerinfo.html", context)

'''
This function will send the email to the owner of 
Doggy brothers i.e Mike with selling car details
'''
def sendEmail(request, id):
    getobj = Seller.objects.filter(id=id).first()
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login('digitrix@example.org', 'digitrix123')
    commission = (getobj.price * 5 /100)
    emailValue = "Car Name "+ getobj.make 
    emailValue += "\r\n Car Model:  " + getobj.model
    emailValue += "\r\n Car Age:  "+ str(getobj.year)
    emailValue += "\r\n Car Condition:  "+ getobj.condition
    emailValue += "\r\n Car Seller Name:  "+ getobj.name
    emailValue += "\r\n Car Seller Mobile:  "+ str(getobj.mobile)
    emailValue += "\r\n Car Price:  "+ str(getobj.price)
    emailValue += "\r\n Commission:  "+ str(commission)
    emailValue += "\r\n Net Amount:  "+ str(int(getobj.price) - commission)
    server.sendmail('digitrix@example.org', 'mike@example.org', emailValue)
    getobj.is_sold = True
    getobj.save()
    print('Mail sent')
    return render(request, "greetings.html")

'''
This function is for logging in the site
that is for owner Mike to login the site
'''
def postsignIn(request):
	name=request.POST.get('username')
	pasw=request.POST.get('password')
	user = auth.authenticate(username=name, password=pasw)
	if user is not None:        
		login(request, user)
		session_id=str(user.id)
		request.session['uid']=str(session_id)
		return HttpResponseRedirect('/')
	else:
		message="Invalid Credentials!!Please ChecK your Data"
		return render(request,"Login.html",{"message":message})
		
'''
This function is to add new car details with its seller name
'''
class CarSellerView(FormView):
    form_class = SellerForm
    template_name = 'addcar_details.html'
    success_url = reverse_lazy('/')

    def form_valid(self, form):
        car_obj = form.save(commit=False)
        car_obj.save()
        return HttpResponseRedirect('/')

'''
This function display the List of cars with paging functionality
it will also display Filter fiunctionality which will be applicable on listing of cars
'''
class CarListView(ListView):
    template_name = "home.html"
    context_object_name = "car_list"
    paginate_by = 10
    def get_queryset(self):
        queryset = Seller.objects.all()
        if self.request.GET:
            make = self.request.GET.get('make')
            year = self.request.GET.get('year')            
            clear_filter = self.request.GET.get('clear')
            if make:
                queryset = queryset.filter(make=make)
            if year:
                queryset = queryset.filter(year=year)
            if clear_filter:
                queryset = Seller.objects.all()
        return queryset


