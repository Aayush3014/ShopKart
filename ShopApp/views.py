from django.shortcuts import render
from ShopApp.models import Contact
from django.contrib import messages
# Create your views here.


def index(request):
    return render(request, 'index.html')


def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        description = request.POST.get("desc")
        phone_number = request.POST.get("pnumber")

        query = Contact(name=name, email=email, description=description, phone_number=phone_number)
        query.save()
        messages.success(request, "We will get back to you soon...")
    return render(request, 'contact.html')


def about(request):
    return render(request, 'about.html')