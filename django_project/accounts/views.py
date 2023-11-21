from accounts.models import Profile
from django.shortcuts import redirect, render
from django.contrib.auth.models import User,auth
from django.contrib import messages
from .models import *
import uuid
from django.conf import settings
from django.core.mail import send_mail
from .helpers import send_forget_password_mail
from django.contrib.auth import authenticate,login
from django.contrib.auth.decorators import login_required
from django.core.signing import TimestampSigner, BadSignature, SignatureExpired
from django.urls import reverse
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
from django.contrib.auth import get_user_model
# from django.contrib.auth.tokens import default_token_generator
# from django.core.mail import EmailMessage
# from django.shortcuts import render, redirect, get_object_or_404
# from django.template.loader import render_to_string
# from django.utils.encoding import force_bytes
# from django.utils.http import urlsafe_base64_encode
# from django.contrib import messages
# from django.contrib.auth import update_session_auth_hash
# from django.contrib.auth.forms import PasswordChangeForm
# from django.utils.http import urlsafe_base64_decode

# Create your views here.

def login_attempt(request):
    try:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user_obj = User.objects.filter(username = username).first()
            if user_obj is None:
                messages.success(request, 'User not found.')
                return redirect('login')
            
            
            profile_obj = Profile.objects.filter(user = user_obj ).first()

            if not profile_obj.is_verified:
                messages.success(request, 'Profile is not verified check your mail.')
                return redirect('login')

            user = authenticate(username = username , password = password)

            if user is None:
                print(password)
                messages.success(request, 'Wrong password.')
                print(password)
                print(username)
                return redirect('login')
            
            login(request , user)
            return redirect('/')

    except Exception as e:
        print(e)
    return render(request , 'login.html')


def register_attempt(request):

    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        print(password)

        try:
            if User.objects.filter(username = username).first():
                messages.success(request, 'Username is taken.')
                return redirect('register')

            if User.objects.filter(email = email).first():
                messages.success(request, 'Email is taken.')
                return redirect('register')
            
            user_obj = User.objects.create_user(username = username , email = email , password=password, first_name=first_name, last_name=last_name)
            user_obj.set_password(password)
            user_obj.save();
            print('user created')
            print(username)
            print(password)
            auth_token = str(uuid.uuid4())
            profile_obj = Profile.objects.create(user = user_obj , auth_token = auth_token)
            profile_obj.save()
            send_mail_after_registration(email , auth_token)
            return redirect('token')

        except Exception as e:
            print(e)


    return render(request , 'register.html')


def logout(request):
    auth.logout(request)
    return redirect('/')


def success(request):
    return render(request , 'success.html')


def token_send(request):
    return render(request , 'token_send.html')



def verify(request , auth_token):
    try:
        profile_obj = Profile.objects.filter(auth_token = auth_token).first()
    

        if profile_obj:
            if profile_obj.is_verified:
                messages.success(request, 'Your account is already verified.')
                return redirect('login')
            profile_obj.is_verified = True
            profile_obj.save()
            messages.success(request, 'Your account has been verified.')
            return redirect('login')
        else:
            return redirect('error')
    except Exception as e:
        print(e)
        return redirect('/')

def error_page(request):
    return  render(request , 'error.html')








def send_mail_after_registration(email , token):
    subject = 'Your accounts need to be verified'
    message = f'Hi paste the link to verify your account http://127.0.0.1:8000/accounts/verify/{token}'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email]
    send_mail(subject, message , email_from ,recipient_list )


def ChangePassword(request , token):
    context = {}
    
    
    try:
        profile_obj = Profile.objects.filter(auth_token = token).first()
        context = {'user_id' : profile_obj.user.id}
        
        if request.method == 'POST':
            new_password = request.POST.get('new_password')
            confirm_password = request.POST.get('reconfirm_password')
            user_id = request.POST.get('user_id')
            
            if user_id is  None:
                messages.success(request, 'No user id found.')
                return redirect(f'change-password/{token}')
                
            
            if  new_password != confirm_password:
                messages.success(request, 'both should  be equal.')
                return redirect(f'change-password/{token}')
                         
            
            user_obj = User.objects.get(id = user_id)
            user_obj.set_password(new_password)
            user_obj.save()
            return redirect('login')
            
            
            
        
        
    except Exception as e:
        print(e)
    return render(request , 'change-password.html' , context)


def ForgetPassword(request):
    try:
        if request.method == 'POST':
            email = request.POST.get('email')
            
            if not User.objects.filter(email=email).first():
                messages.info(request, 'Not user found with this email address.')
                return redirect('forget-password')
                
            
            user_obj = User.objects.get(email = email)
            token = str(uuid.uuid4())
            profile_obj= Profile.objects.get(user = user_obj)
            profile_obj.auth_token = token
            profile_obj.save()
            send_forget_password_mail(user_obj.email , token)
            messages.info(request, 'An email is sent.')
            return redirect('forget-password')
                
    
    
    except Exception as e:
        print(e)
    return render(request , 'forget-password.html')
    



def PasswordUpdate(request):
    context={}
    if request.method == 'POST':
        current = request.POST['cpwd']
        new_pas = request.POST['npwd']
        user = User.objects.get(id=request.user.id)
        un = user.username
        check = user.check_password(current)
        if check==True:
            user.set_password(new_pas)
            user.save()
            context["msz"]= "Password Updated Chagesucessfully !!!"
            context["col"]= "alert-success"
            user=User.objects.get(username=un)
            login(request,user)
        else:
            context["msz"]= "Incorect Current password"
            context["col"]= "alert-danger"
            


    
    return render(request , 'update_passwords.html',context)




def Edit(request):
    user = request.user
    
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        old_username = request.POST.get('old_username', None)
        
        try:
            user_obj = User.objects.get(username=username)
            # If the user already exists, update their first and last name
            user_obj.first_name = first_name
            user_obj.last_name = last_name
        except User.DoesNotExist:
            # If the user does not exist, create a new one with the new username
            if old_username is not None:
                user_obj = User.objects.get(username=old_username)
                user_obj.first_name = first_name
                user_obj.last_name = last_name
                user_obj.username = username
            else:
                user_obj = User(first_name=first_name, last_name=last_name, username=username)
            
        user_obj.save()
        messages.info(request, 'Profile Updated Successfully.')
        print('user created/updated')
       
    return render(request, 'edit.html', {'user': user})


User = get_user_model()

@login_required
def update_email(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        if User.objects.filter(email = email).first():
            messages.success(request, 'Email is already taken.')
            return redirect('update_email')

        # Generate a signed token for the new email address
        signer = TimestampSigner()
        token = signer.sign(email)

        # Construct the verification URL
        verify_url = reverse('verify_email')
        verify_url += f'?token={token}'

        # Send the verification email
        subject = 'Verify your new email address'
        message = f'Click this link to verify your new email address: {settings.BASE_URL}{verify_url}'
        from_email = settings.DEFAULT_FROM_EMAIL
        recipient_list = [email]
        send_mail(subject, message, from_email, recipient_list)

        # Display a success message to the user
        messages.success(request, 'A verification link has been sent to your new email address.')
        return redirect('update_email')

    return render(request, 'update_email.html')

@login_required
def verify_email(request):
    token = request.GET.get('token')

    # Verify the token and extract the email address
    try:
        signer = TimestampSigner()
        email = signer.unsign(token, max_age=86400)  # 86400 seconds = 24 hours
    except SignatureExpired:
        # The token has expired
        messages.error(request, 'The verification link has expired.')
        return redirect('update_email')
    except BadSignature:
        # The token is invalid
        messages.error(request, 'The verification link is invalid.')
        return redirect('update_email')
    else:
        # The token is valid, update the email address
        user = request.user
        user.email = email
        user.save()
        messages.success(request, 'Your email address has been updated successfully.')
        return redirect('update_email')
