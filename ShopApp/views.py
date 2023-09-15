from django.shortcuts import render,redirect
from ShopApp.models import Contact, Product, Orders, OrderUpdate
from django.contrib import messages
from math import ceil


# Payment Integration.
from . import keys


def index(request):

    """
    The function first creates an empty list called allProds. This list will be used to store the products that will 
    be displayed on the home page.

    The next step is to get all the unique categories of products from the database. This is done using 
    the Product.objects.values('category','id') query. The results of this query are stored in a dictionary called cats.

    The for loop then iterates over the cats dictionary. For each category, the function gets all the products in 
    that category using the Product.objects.filter(category=cat) query. The number of products in each category is 
    then stored in a variable called n.

    The next step is to calculate the number of slides that will be used to display the products in each 
    category. The number of slides is calculated by dividing the number of products by 4 and rounding up the 
    result. This is done using the following formula:

    nSlides = n // 4 + ceil((n / 4) - (n // 4))
    
    The ceil() function is used to round up the result. This ensures that there will always be at least 
    one slide, even if there are only a few products in the category.

    The final step is to append the following information to the allProds list:

    The list of products in the category
    A list of numbers from 1 to the number of slides
    The total number of slides
    The params dictionary is then created and it is passed to the render() function along with the index.html template. 
    The render() function then renders the index.html template and returns the rendered HTML as an HTTP response.

    In more detail, the index() function performs the following tasks:

    Gets all the unique product categories from the database.
    Gets all the products in each category.
    Calculates the number of slides that will be used to display the products in each category.
    Creates a list of products and slides for each category.
    Returns the list of products and slides to the index.html template.
    The index() function is a very important function in an e-commerce website. It is responsible for displaying 
    the home page, which is the first page that users see when they visit the website. The function ensures that the 
    home page is properly displayed and that the products are organized in a way that is easy for users to browse.
    """


    allProds = []
    catprods = Product.objects.values('category','id')
    cats = {item['category'] for item in catprods}
    for cat in cats:
        prod = Product.objects.filter(category = cat)
        n = len(prod)
        nSlides = n//4 + ceil((n / 4) - (n // 4))
        allProds.append([prod,range(1, nSlides), nSlides])

    params = {'allProds':allProds}

    return render(request, 'index.html', params)




def contact(request):

    """
    The function first checks if the request method is POST. If it is, then the function gets the 
    name, email, description, and phone number from the request POST data.
    
    The function then creates a Contact object and saves it to the database. The Contact object is a 
    Django model that represents a contact form submission.
    
    Finally, the function sends a success message to the user and returns the contact.html template.
    
    The contact() function performs the following tasks:
    Validates the contact form data.
    Saves the contact form data to the database.
    Sends a success message to the user.
    Returns the contact.html template.
    
    """
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




def checkout(request):
    def checkout(request):
        if not request.user.is_authenticated:
            messages.warning(request,"Login & Try Again")
            return redirect('/auth/login')

        if request.method=="POST":
            items_json = request.POST.get('itemsJson', '')
            name = request.POST.get('name', '')
            amount = request.POST.get('amt')
            email = request.POST.get('email', '')
            address1 = request.POST.get('address1', '')
            address2 = request.POST.get('address2','')
            city = request.POST.get('city', '')
            state = request.POST.get('state', '')
            zip_code = request.POST.get('zip_code', '')
            phone = request.POST.get('phone', '')
            Order = Orders(items_json=items_json,name=name,amount=amount, email=email, address1=address1,address2=address2,city=city,state=state,zip_code=zip_code,phone=phone)
            print(amount)
            Order.save()
            update = OrderUpdate(order_id=Order.order_id,update_desc="the order has been placed")
            update.save()
            paid = True


            # # PAYMENT INTEGRATION

            id = Order.order_id
            oid=str(id)+"ShopyCart"
            param_dict = {

                'MID':keys.MID,
                'ORDER_ID': oid,
                'TXN_AMOUNT': str(amount),
                'CUST_ID': email,
                'INDUSTRY_TYPE_ID': 'Retail',
                'WEBSITE': 'WEBSTAGING',
                'CHANNEL_ID': 'WEB',
                'CALLBACK_URL': 'http://127.0.0.1:8000/handlerequest/',

            }
            param_dict['CHECKSUMHASH'] = Checksum.generate_checksum(param_dict, MERCHANT_KEY)
            return render(request, 'paytm.html', {'param_dict': param_dict})

        return render(request, 'checkout.html')