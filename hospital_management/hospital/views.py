from django.shortcuts import render
from django.http import HttpResponse
from .models import Departments,Doctors
from .forms import BookingForm

# Create your views here.

def index(request):
    return render(request,'index.html')

def department(request):
    dict_dept={
        'dept': Departments.objects.all()
    }
    return render(request,"departments.html",dict_dept)

def doctors(request):
    dict_doc={
        'doct': Doctors.objects.all()
    }
    return render(request,"doctors.html",dict_doc)

def booking(request):
    if request.method=="POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'confirmation.html')
    form  = BookingForm()
    dict_book={
           'form': form
    }
    return render(request,"booking.html",dict_book)

def about(request):
    return render(request,"about.html")

def contact(request):
    return render(request,"contactus.html")