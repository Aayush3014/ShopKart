from django.urls import path
from ShopApp.views import index, contact, about, checkout ,handlerequest, order



urlpatterns = [
    path("",index,name = "index"),
    path("contact",contact, name="contact"),
    path("about",about,name="about"),
    path("order",order,name="order"),
    path('checkout/',checkout, name="checkout"),
    path('handlerequest/',handlerequest,name= "HandleRequest"),


]
