from django.urls import path,include
from . import views


urlpatterns = [
    path('',views.index,name='home'),
    path('about',views.about,name='about'),
    path('booking',views.booking,name='booking'),
    path('doctors',views.doctors,name='doctors'),
    path('contact',views.contact,name='contact'),
    path('department',views. department,name='department'),
    path('userdetails',views. userdetails,name='userdetails'),
    path('bookingdetails',views.bookingdetails,name='bookingdetails'),
    path('update/<int:book_id>/',views.update,name='update'),
    path('delete/<int:book_id>/',views.delete,name='delete'),
    path('services',views. Services,name='services'),
]
