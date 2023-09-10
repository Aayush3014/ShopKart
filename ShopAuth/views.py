from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
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
        user.save()
        messages.success(request, f"Congratulations {email}, You are Registered.")
    return render(request, 'signup.html')
    


def handlelogin(request):
    return render(request, "login.html")

def handlelogout(request):
    return redirect("/auth/login")