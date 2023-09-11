from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages

from django.views.generic import View
from django.template.loader import render_to_string

from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode

from .utils import TokenGenerator, generate_token

from django.utils.encoding import force_bytes,force_str

from django.core.mail import EmailMessage

# from Shoppy import settings  we can use this also
from django.conf import settings


# Create your views here.


def signup(request):


    if request.method=="POST":
        email = request.POST['email']
        password = request.POST['pass1']
        confirm_password = request.POST['pass2']

        if password != confirm_password:
            messages.warning(request, "Password does not match.")
            return render(request, "signup.html")
        
        try:
            if User.objects.get(username = email):
                messages.warning(request, "User already exists.")
                return render(request, 'signup.html')
        except Exception as e:
            pass
        
        user = User.objects.create_user(email,email,password)
        user.is_active = False  # This is used for making user unauthenticated by default.
        user.save()



        email_subject = "Account Activation Required!!!"
        message = render_to_string('activate.html',{
            'user':user,
            'domain' : '127.0.0.1:8000',
            'uid':urlsafe_base64_encode(force_bytes(user.pk)),
            'token':generate_token.make_token(user)

        })


        email_message = EmailMessage(email_subject,message,settings.EMAIL_HOST_USER,[email])

        email_message.send()
        messages.success(request, f"Congratulations {email}, You are Registered.")
        return redirect('/auth/login/')
    
    
    
    return render(request, 'signup.html')
    


# Code for activating the account.

class ActivateAccountView(View):
    def get(self, request, uidb64,token):
        try:
            uid = force_str(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=uid)
        except Exception as e:
            user = None
        if user is not None and generate_token.check_token(user, token):
            user.is_active = True
            user.save()
            messages.success(request,f"{user} Your account is activated successfully.")
            return redirect('/auth/login/')
        return render(request,"activatefail.html")












def handlelogin(request):
    return render(request, "login.html")

def handlelogout(request):
    return redirect("/auth/login")