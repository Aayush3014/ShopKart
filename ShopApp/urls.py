from django.urls import path
from ShopApp.views import index, contact, about, checkout ,handlerequest, profile



urlpatterns = [
    path("",index,name = "index"),
    path("contact",contact, name="contact"),
    path("about",about,name="about"),
    path("profile",profile,name="profile"),
    path('checkout/',checkout, name="checkout"),
    path('handlerequest/',handlerequest,name= "HandleRequest"),


]
