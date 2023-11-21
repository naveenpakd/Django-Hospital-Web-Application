from django import forms
from django.core.validators import RegexValidator
from .models import Booking
from django.contrib.auth.models import User

class DateInput(forms.DateInput):
    input_type = 'date'

class BookingForm(forms.ModelForm):
    p_phone = forms.CharField(
        max_length=10,
        validators=[
            RegexValidator(
                regex='^[0-9]{10}$',
                message='Phone number must be 10 digits',
                code='invalid_phone_number'
            )
        ],
    )

    class Meta:
        model = Booking
        fields = '__all__'
        widgets = {
            'booking_date': DateInput(),
        }
        labels = {
            'username': "",
            'p_name': "Patient Name",
            'p_phone': "Patient Phone ",
            'p_email': "Patient Email ",
            'doc_name': "Doctor Name ",
        }
        exclude = ('updated', 'created')

    def __init__(self, *args, **kwargs):
        super(BookingForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({
            'readonly': 'True',
            'hidden': 'True',
            'id': 'em',
            "class": " form-control"
        }),
        self.fields['p_email'].widget.attrs.update({
            # 'readonly':'True',
            # 'id': 'em',
            "class": " form-control"
        }),
        self.fields['booking_date'].widget.attrs.update({
            'booking_date': 'DateField()',
            'placeholder': '2023-03-15',
            "class": " form-control"
        }),
        self.fields['p_name'].widget.attrs.update({
            "class": " form-control"
        }),
        self.fields['p_phone'].widget.attrs.update({
            "class": " form-control"
        }),
        self.fields['doc_name'].widget.attrs.update({
            "class": " form-control"
        }),
        self.fields['booking_date'].widget.attrs.update({
            "class": " form-control"
        })




# from django import forms

# from .models import Booking
# from django.contrib.auth.models import User




# class DateInput(forms.DateInput):
#     input_type = 'date'


# class BookingForm(forms.ModelForm):
     

    


#     class Meta:
#         model = Booking
#         fields = '__all__'

#         widgets = {
#            'booking_date' : DateInput(),
            
            
#         }
#         labels = {
#             'username':"",
#             'p_name':"Patient Name",
#             'p_phone':"Patient Phone ",
#             'p_email':"Patient Email ", 
#             'doc_name':"Doctor Name ", 
            
            
#         }
#         exclude = ('updated', 'created')


#     def __init__(self, *args, **kwargs):
#         super(BookingForm, self).__init__(*args, **kwargs)

#         self.fields['username'].widget.attrs.update({
                
#                 'readonly':'True',
#                 'hidden':'True',
#                 'id': 'em',
#                 "class":" form-control"
#             }),


#         self.fields['p_email'].widget.attrs.update({
                
#                 # 'readonly':'True',
#                 # 'id': 'em',
#                 "class":" form-control"
#             }),
#         self.fields['booking_date'].widget.attrs.update({
                
#                 'booking_date' : 'DateField()',
#                 'placeholder':'2023-03-15',
#                 "class":" form-control"
#             }),   

#         self.fields['p_name'].widget.attrs\
#                 .update({
                    
                    
#                     "class":" form-control"
#                 }),
#         self.fields['p_phone'].widget.attrs\
#                 .update({
                    
                    
#                     "class":" form-control"
#                 }),
#         self.fields['doc_name'].widget.attrs\
#                 .update({
                    
                    
#                     "class":" form-control"
#                 }),
#         self.fields['booking_date'].widget.attrs\
#                 .update({
                    
                    
#                     "class":" form-control"
#                 })

        

#     labels = {
           
#             'p_name':"Patients Name",
#             'p_phone':"Patient Phone ",
#             'p_email':"Patient Email ", 
#             'doc_name':"Doctor Name ", 
            
            
#         }


        
        
