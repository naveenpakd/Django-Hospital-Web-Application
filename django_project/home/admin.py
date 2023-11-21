from django.contrib import admin
from .models import Departments,Doctors,Booking
from django.contrib.auth.models import User

# Register your models here.

admin.site.register(Departments)
admin.site.register(Doctors)



class BookingAdmin(admin.ModelAdmin):
    list_display = ('id','p_name','p_phone','p_phone','doc_name','booking_date','booked_on','username')

admin.site.register(Booking, BookingAdmin)
