from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.views import LoginView
from django.template.loader import render_to_string
from django.views.generic.edit import CreateView, FormView, UpdateView
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import UserForm, SellerForm
from django.urls import reverse_lazy
from .models import User, Seller
import smtplib
from django.contrib.auth import authenticate, login
from django.template.loader import render_to_string
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

def logout(request):
	return render(request,"Login.html")


def showGreetings(request):
    return render(request, "greetings.html")

def addBuyer(request, id):
    context={}
    context["id"] = id
    return render(request, "buyerinfo.html", context)

def sendEmail(request, id):
    getobj = Seller.objects.filter(id=id).first()
    getobj.is_sold = True
    getobj.save()
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login('mike@example.org', 'mikeymike123')
    #username: "mike@example.org" password: mikeymike123
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
    
    server.sendmail('mike@example.org', 'mehtahemangi09@gmail.com', emailValue)
    print('Mail sent')
    return render(request, "greetings.html")

def postsignIn(request):
	name=request.POST.get('username')
	pasw=request.POST.get('password')
	user = User.objects.filter(username=name).first()
	if user is not None:
		login(request, user)
		print(request)
		session_id=str(user.id)
		request.session['uid']=str(session_id)
		return HttpResponseRedirect('/')
	else:
		message="Invalid Credentials!!Please ChecK your Data"
		return render(request,"Login.html",{"message":message})
		

class CarSellerView(FormView):
    form_class = SellerForm
    template_name = 'addcar_details.html'
    success_url = reverse_lazy('/')

    def form_valid(self, form):
        car_obj = form.save(commit=False)
        car_obj.save()
        return HttpResponseRedirect('/')


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

