from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render,redirect
from django.http import HttpResponse
from.models import Departments,Doctors,Booking
from.forms import BookingForm
from django.contrib import messages
# Create your views here.

# @login_required()

def index(request):
    person = {
        'num' : ["hello","hai","hey"]
    }
    return render(request, 'index.html',person)

@login_required()
def about(request):
   return render(request, 'abouts.html')

@login_required()
def booking(request):

    if request.method == "POST":
       form =BookingForm(request.POST)

       if form .is_valid():
           form.save()
           return render(request, 'confirmation.html')
       else:
          messages.info(request,'booking failed ')
          return redirect('booking')
    
    form = BookingForm()
    dict_form ={
        'form' : form
    }
    return render(request, 'booking.html',dict_form )


@login_required()
def doctors(request):
    dict_docs = {
        'doctors' : Doctors.objects.all()
    }
    return render(request, 'doctors.html' , dict_docs)

@login_required()
def contact(request):
    if request.method == "POST":
       form = BookingForm(request.POST)
       if form.is_valid():
           form.save()
           return render(request, 'confirmation.html')
    form = BookingForm()
    dict_form ={
        'form' : form
    }
    return render(request, 'contact.html',dict_form )

@login_required()
def department(request):
   dict_dept={
       'dept':Departments.objects.all()
   }
   return render(request, 'department.html',dict_dept)

@login_required()
def userdetails(request):
    return render(request,'userdetails.html')

@login_required()
def bookingdetails(request):

    dict_form ={
            'form' : Booking.objects.all()
        }
    return render(request, 'bookingdetails.html',dict_form )

@login_required()
def update(request,book_id):
    book = Booking.objects.get(id=book_id)
    form = BookingForm(instance = book)
    if request.method == 'POST':
        form = BookingForm(request.POST,instance=book)
        if form.is_valid():
            form.save()
            return redirect('bookingdetails')
    return render(request,'update.html',{'form':form})

@login_required()
def delete(request,book_id):
    if request.method == 'POST':
      b= Booking.objects.get(id=book_id)
      b.delete()
      return redirect('bookingdetails')
    
def Services(request):
    return render(request,'services.html')