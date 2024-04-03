from django.shortcuts import render, redirect
from .forms import SignupForm, AdminProfileForm,UserProfileForm, CustomerForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth import authenticate,login,logout, update_session_auth_hash
from .models import Love, Story, Sci_Fyi, Kids, CartItem, CartItemL, CartItemS, CartItemT,Customer,Order,Order3,Order1,Order2
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
# paypal
from paypal.standard.forms import PayPalPaymentsForm
from django.conf import settings
import uuid
from django.urls import reverse

def home(request):
    return render (request, "suggestion/home.html")

def aboutus(request):
    return render (request, "suggestion/aboutus.html")
def h(request):
    return render (request, "suggestion/help.html")

def sign_up(request):
    if request.method == 'POST':
        mf = SignupForm(request.POST)
        if mf.is_valid():
            mf.save()
            return redirect('/signup/') 
        
        
    else:

        mf = SignupForm()
    return render(request, "suggestion/signup.html", {'mf': mf})

def log_in(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            mf = AuthenticationForm(request,request.POST)
            if mf.is_valid():
                name = mf.cleaned_data['username']
                pas = mf.cleaned_data['password']
                user = authenticate(username=name, password=pas)
                if user is not None:
                    login(request, user)
                    return redirect('/profile/')
        else:
             mf = AuthenticationForm()
        return render (request, "suggestion/login.html", {'mf': mf})
    else:
        return redirect ('/profile/')


def profile(request):
    if request.user.is_authenticated: 
            if request.method == 'POST':
                if request.user.is_superuser == True:
                    mf = AdminProfileForm(request.POST,instance=request.user)
            else:
                mf = UserProfileForm(request.POST,instance=request.user)
            if mf.is_valid():
                mf.save()
            else:
                if request.user.is_superuser == True:
                    mf = AdminProfileForm(instance=request.user)
                else:
                    mf = UserProfileForm(instance=request.user) 
            return render(request,'suggestion/profile.html',{'name':request.user,'mf':mf})
    else:                                                
        return redirect('/login/')
    

def log_out(request):
    logout(request)
    return redirect('/login/')


def L(request):
    mf = Love.objects.all()
    return render(request, 'suggestion/love.html', {'mf':mf})

def S(request):
    mf = Story.objects.all()
    return render(request, 'suggestion/story.html', {'mf':mf})

def F(request):
    mf = Sci_Fyi.objects.all()
    return render(request, 'suggestion/SCI_FYI.html', {'mf':mf})

def K(request):
    mf = Kids.objects.all()
    return render(request, 'suggestion/Kids.html', {'mf':mf})

def Seach_Book(request):
    query = request.GET.get('q')
    if query:
        kids_books = Kids.objects.filter(Book_Name__icontains=query)
        sci_fyi_books = Sci_Fyi.objects.filter(Book_Name__icontains=query)
        love_books = Love.objects.filter(Book_Name__icontains=query)
        story_books = Story.objects.filter(Book_Name__icontains=query)
        search_results = list(kids_books) + list(sci_fyi_books) + list(love_books) + list(story_books)
    else:
        search_results = []
    return render(request, "suggestion/Search.html", {'search_results': search_results, 'query': query})

def pcf(request):
    if request.user.is_authenticated:                              # pcf - Include old password 
        if request.method == 'POST':                               
            mf =PasswordChangeForm(request.user,request.POST)
            if mf.is_valid():
                mf.save()
                update_session_auth_hash(request,mf.user)
                return redirect('/profile/')
        else: 
            mf = PasswordChangeForm(request.user)
        return render(request,'suggestion/pcf.html',{'mf':mf})
    else:
        return redirect('/login/')
    

def my_view(request,id):
    mf = Kids.objects.get(pk=id)
    return render(request, 'suggestion/BuyNow.html', {'mf':mf})

def my_viewL(request,id):
    mf = Love.objects.get(pk=id)
    return render(request, 'suggestion/BuyNow.html', {'mf':mf})

def my_viewS(request,id):
    mf = Sci_Fyi.objects.get(pk=id)
    return render(request, 'suggestion/BuyNow.html', {'mf':mf})

def my_viewT(request,id):
    mf = Story.objects.get(pk=id)
    return render(request, 'suggestion/BuyNow.html', {'mf':mf})



def add_to_cart(request, id):   
    if request.user.is_authenticated:
        product = Kids.objects.get(pk=id)
        
        user=request.user                
        CartItem(user=user,product=product).save() 
        return redirect('K')   
    else:   
        return redirect('login')  
    
def add_to_cartL(request, id):   
    if request.user.is_authenticated:
        product = Love.objects.get(pk=id)
        
        user=request.user                
        CartItemL(user=user,product=product).save() 
        return redirect('L')   
    else:   
        return redirect('login') 
    
def add_to_cartS(request, id):   
    if request.user.is_authenticated:
        product = Sci_Fyi.objects.get(pk=id)
        
        user=request.user                
        CartItemS(user=user,product=product).save() 
        return redirect('F')   
    else:   
        return redirect('login') 

def add_to_cartT(request, id):   
    if request.user.is_authenticated:
        product = Story.objects.get(pk=id)
        
        user=request.user                
        CartItemT(user=user,product=product).save() 
        return redirect('S')   
    else:   
        return redirect('login') 
    


  
    
def view_cart(request):
    cart_items = CartItem.objects.filter(user=request.user)      # cart_items will fetch product of current user, and show product available in the cart of the current user.
    cart_itemsl = CartItemL.objects.filter(user=request.user)
    cart_itemsS = CartItemS.objects.filter(user=request.user)  
    cart_itemsT = CartItemT.objects.filter(user=request.user) 
    total =0
    totalL=0
    totalS=0
    totalT=0
    delhivery_charge =50
    for item in cart_items:
        item.product.price_and_quantity_total = item.product.Book_Price * item.quantity
        total += item.product.price_and_quantity_total
       
    final_price= total
    for item in cart_itemsl:
        item.product.price_and_quantity_total = item.product.Book_Price * item.quantity
        totalL += item.product.price_and_quantity_total
    final_priceL=totalL
    for item in cart_itemsS:
        item.product.price_and_quantity_total = item.product.Book_Price * item.quantity
        totalS += item.product.price_and_quantity_total
    final_priceS=totalS
    for item in cart_itemsT:
        item.product.price_and_quantity_total = item.product.Book_Price * item.quantity
        totalT += item.product.price_and_quantity_total
    final_priceT= totalT
    Final_Value = final_price+final_priceL+final_priceS+final_priceT+delhivery_charge
    total_value = total+totalL+totalS+totalT     # cart_items will fetch product of current user, and show product available in the cart of the current user.
    return render(request, 'suggestion/view_cart.html',{'cart_items': cart_items,'cart_itemsl': cart_itemsl,'cart_itemsS': cart_itemsS, 'cart_itemsT': cart_itemsT,'total':total,'final_price':final_price,'totalL':totalL,'final_priceL':final_priceL,'totalS':totalS,'final_priceS':final_priceS,'totalL':totalL,'final_priceT':final_priceT, 'Final_value':Final_Value, ' total_value':total_value,})


def add_quantity(request, id):
    product = get_object_or_404(CartItem, pk=id)    # If the object is found, it returns the object. If not, it raises an HTTP 404 exception (Http404).
    product.quantity += 1                       # If object found it will be add 1 quantity to the current object   
    product.save()
    return redirect('view_cart')

def delete_quantity(request, id):
    product = get_object_or_404(CartItem, pk=id)
    if product.quantity > 1:
        product.quantity -= 1
        product.save()
    return redirect('view_cart')

def add_quantityL(request, id):
    product = get_object_or_404(CartItemL, pk=id)    # If the object is found, it returns the object. If not, it raises an HTTP 404 exception (Http404).
    product.quantity += 1                       # If object found it will be add 1 quantity to the current object   
    product.save()
    return redirect('view_cart')

def delete_quantityL(request, id):
    product = get_object_or_404(CartItemL, pk=id)
    if product.quantity > 1:
        product.quantity -= 1
        product.save()
    return redirect('view_cart')

def add_quantityS(request, id):
    product = get_object_or_404(CartItemS, pk=id)    # If the object is found, it returns the object. If not, it raises an HTTP 404 exception (Http404).
    product.quantity += 1                       # If object found it will be add 1 quantity to the current object   
    product.save()
    return redirect('view_cart')

def delete_quantityS(request, id):
    product = get_object_or_404(CartItemS, pk=id)
    if product.quantity > 1:
        product.quantity -= 1
        product.save()
    return redirect('view_cart')


def add_quantityT(request, id):
    product = get_object_or_404(CartItemT, pk=id)    # If the object is found, it returns the object. If not, it raises an HTTP 404 exception (Http404).
    product.quantity += 1                       # If object found it will be add 1 quantity to the current object   
    product.save()
    return redirect('view_cart')

def delete_quantityT(request, id):
    product = get_object_or_404(CartItemT, pk=id)
    if product.quantity > 1:
        product.quantity -= 1
        product.save()
    return redirect('view_cart')

def delete(request,id):
    
    de = get_object_or_404(CartItem, pk=id)
    de.delete()
    return redirect('view_cart')

def deleteL(request,id):
    
    de = get_object_or_404(CartItemL, pk=id)
    de.delete()
    return redirect('view_cart')

def deleteS(request,id):
    
    de = get_object_or_404(CartItemS, pk=id)
    de.delete()
    return redirect('view_cart')

def deleteT(request,id):
    
    de = get_object_or_404(CartItemT, pk=id)
    de.delete()
    return redirect('view_cart')

def address(request):
    if request.method == 'POST':
        mf = CustomerForm(request.POST)
        if mf.is_valid():
            user = request.user
            name = mf.cleaned_data['name']
            address = mf.cleaned_data['address']
            city = mf.cleaned_data['city']
            state = mf.cleaned_data['state']
            pincode = mf.cleaned_data['pincode']
            Customer(user=user, name=name, address=address, city=city, state=state, pincode=pincode).save()
            return redirect('address')
    else:
        mf = CustomerForm()
        address = Customer.objects.filter(user=request.user)
    return render(request, 'suggestion/address.html', {'mf': mf, 'address': address})

def delete_address(request,id):
    if request.method == 'POST':
        de = Customer.objects.get(pk=id)
        de.delete()
    return redirect('address')

def Chekcout(request):
    cart_items = CartItem.objects.filter(user=request.user)      # cart_items will fetch product of current user, and show product available in the cart of the current user.
    cart_itemsl = CartItemL.objects.filter(user=request.user)
    cart_itemsS = CartItemS.objects.filter(user=request.user)  
    cart_itemsT = CartItemT.objects.filter(user=request.user) 
    total =0
    totalL=0
    totalS=0
    totalT=0
    delhivery_charge =50
    for item in cart_items:
        item.product.price_and_quantity_total = item.product.Book_Price * item.quantity
        total += item.product.price_and_quantity_total
    final_price= total
    for item in cart_itemsl:
        item.product.price_and_quantity_total = item.product.Book_Price * item.quantity
        totalL += item.product.price_and_quantity_total
    final_priceL=totalL
    for item in cart_itemsS:
        item.product.price_and_quantity_total = item.product.Book_Price * item.quantity
        totalS += item.product.price_and_quantity_total
    final_priceS=totalS
    for item in cart_itemsT:
        item.product.price_and_quantity_total = item.product.Book_Price * item.quantity
        totalT += item.product.price_and_quantity_total
    final_priceT= totalT
    Final_Value = final_price+final_priceL+final_priceS+final_priceT+delhivery_charge
    total_value = total+totalL+totalS+totalT
    address = Customer.objects.filter(user=request.user)     # cart_items will fetch product of current user, and show product available in the cart of the current user.
    # host = request.get_host()   # Will fecth the domain site is currently hosted on.
   
    # paypal_checkout = {
    #     'business': settings.PAYPAL_RECEIVER_EMAIL,   #This is typically the email address associated with the PayPal account that will receive the payment.
    #     'amount': Final_Value ,    #: The amount of money to be charged for the transaction. 
    #     'item_name': 'Pet',       # Describes the item being purchased.
    #     'invoice': uuid.uuid4(),  #A unique identifier for the invoice. It uses uuid.uuid4() to generate a random UUID.
    #     'currency_code': 'USD',
    #     'notify_url': f"http://{host}{reverse('paypal-ipn')}",         #The URL where PayPal will send Instant Payment Notifications (IPN) to notify the merchant about payment-related events
    #     'return_url': f"http://{host}{reverse('paymentsuccess')}",     #The URL where the customer will be redirected after a successful payment. 
    #     'cancel_url': f"http://{host}{reverse('paymentfailed')}",      #The URL where the customer will be redirected if they choose to cancel the payment. 
    # }

    # paypal_payment = PayPalPaymentsForm(initial=paypal_checkout)
    return render(request, 'suggestion/Checkout.html',{'cart_items': cart_items,'cart_itemsl': cart_itemsl,'cart_itemsS': cart_itemsS, 'cart_itemsT': cart_itemsT,'total':total,'final_price':final_price,'totalL':totalL,'final_priceL':final_priceL,'totalS':totalS,'final_priceS':final_priceS,'totalL':totalL,'final_priceT':final_priceT, 'Final_value':Final_Value, ' total_value':total_value, 'address':address,})

def Payment(request):
    if request.method == 'POST':
        selected_address_id = request.POST.get('selected_address')

    host = request.get_host() 
    cart_items = CartItem.objects.filter(user=request.user)      # cart_items will fetch product of current user, and show product available in the cart of the current user.
    cart_itemsl = CartItemL.objects.filter(user=request.user)
    cart_itemsS = CartItemS.objects.filter(user=request.user)  
    cart_itemsT = CartItemT.objects.filter(user=request.user) 
    total =0
    totalL=0
    totalS=0
    totalT=0
    delhivery_charge =50
    for item in cart_items:
        item.product.price_and_quantity_total = item.product.Book_Price * item.quantity
        total += item.product.price_and_quantity_total
    final_price= total
    for item in cart_itemsl:
        item.product.price_and_quantity_total = item.product.Book_Price * item.quantity
        totalL += item.product.price_and_quantity_total
    final_priceL=totalL
    for item in cart_itemsS:
        item.product.price_and_quantity_total = item.product.Book_Price * item.quantity
        totalS += item.product.price_and_quantity_total
    final_priceS=totalS
    for item in cart_itemsT:
        item.product.price_and_quantity_total = item.product.Book_Price * item.quantity
        totalT += item.product.price_and_quantity_total
    final_priceT= totalT
    Final_Value = final_price+final_priceL+final_priceS+final_priceT+delhivery_charge
    total_value = total+totalL+totalS+totalT
    address = Customer.objects.filter(user=request.user)     # cart_items will fetch product of current user, and show product available in the cart of the current user.
    host = request.get_host()   # Will fecth the domain site is currently hosted on.
   
    paypal_checkout = {
        'business': settings.PAYPAL_RECEIVER_EMAIL,
        'amount': Final_Value,
        'item_name': 'Pet',
        'invoice': uuid.uuid4(),
        'currency_code': 'USD',
        'notify_url': f"http://{host}{reverse('paypal-ipn')}",
        'return_url': f"http://{host}{reverse('paymentsuccess', args=[selected_address_id])}",
        'cancel_url': f"http://{host}{reverse('paymentfailed')}",
    }

    paypal_payment = PayPalPaymentsForm(initial=paypal_checkout)
    return render(request, 'suggestion/Payment.html',{'cart_items': cart_items,'cart_itemsl': cart_itemsl,'cart_itemsS': cart_itemsS, 'cart_itemsT': cart_itemsT,'total':total,'final_price':final_price,'totalL':totalL,'final_priceL':final_priceL,'totalS':totalS,'final_priceS':final_priceS,'totalL':totalL,'final_priceT':final_priceT, 'Final_value':Final_Value, ' total_value':total_value, 'address':address,'paypal':paypal_payment})
def payment_success(request,selected_address_id):
   
    print('payment sucess',selected_address_id) 
    user =request.user
    customer_data = Customer.objects.get(pk=selected_address_id,)
    cart_items = CartItem.objects.filter(user=request.user)      # cart_items will fetch product of current user, and show product available in the cart of the current user.
    cart_itemsl = CartItemL.objects.filter(user=request.user)
    cart_itemsS = CartItemS.objects.filter(user=request.user)  
    cart_itemsT = CartItemT.objects.filter(user=request.user)
    for c in cart_items:
        Order(user=user,customer=customer_data,Kids=c.product,quantity=c.quantity).save()
        c.delete()
    for c1 in cart_itemsl:
        Order1(user=user,customer=customer_data,Love=c1.product,quantity=c1.quantity).save()
        c1.delete()
    for c2 in cart_itemsS:
        Order2(user=user,customer=customer_data,Sci_Fyi=c2.product,quantity=c2.quantity).save()
        c2.delete()
    for c3 in cart_itemsT:
        Order3(user=user,customer=customer_data,Story=c3.product,quantity=c3.quantity).save()
        c3.delete()
    return render(request,'suggestion/payment_success.html')


def payment_failed(request):
    return render(request,'suggestion/payment_failed.html')

def order(request):
    ord=Order.objects.filter(user=request.user)
    return render(request,'suggestion/order.html',{'ord':ord})

# @login_required
def Buynow(request, id):
    if request.user.is_authenticated:
        mf = Kids.objects.get(pk=id)
  
        delhivery_charge =50
        Final_Price= delhivery_charge + mf.Book_Price
        Final_Value=Final_Price

        address = Customer.objects.filter(user=request.user)
        return render(request, 'suggestion/Buy.html', {'Final_Price':Final_Price,'mf':mf,'address':address,'Final_Value':Final_Value})
    else:   
        return redirect('login') 
    
def Buynowl(request, id):
    if request.user.is_authenticated:
        mf1 = Love.objects.get(pk=id)
        quantity = 1
  
        delhivery_charge =50
        Final_Price= delhivery_charge + mf1.Book_Price
        Final_Value=Final_Price

        address = Customer.objects.filter(user=request.user)
        return render(request, 'suggestion/Buyl.html', {'Final_Price':Final_Price,'mf1':mf1,'address':address,'Final_Value':Final_Value,'quantity':quantity})
    else:   
        return redirect('login') 
    

def BuynowS(request, id):
    if request.user.is_authenticated:
        mf2 = Sci_Fyi.objects.get(pk=id)
        quantity = 1
  
        delhivery_charge =50
        Final_Price= delhivery_charge + mf2.Book_Price
        Final_Value=Final_Price

        address = Customer.objects.filter(user=request.user)
        return render(request, 'suggestion/BuyS.html', {'Final_Price':Final_Price,'mf2':mf2,'address':address,'Final_Value':Final_Value,'quantity':quantity})
    else:   
        return redirect('login') 
    
def BuynowT(request, id):
    if request.user.is_authenticated:
        mf3 = Story.objects.get(pk=id)
        quantity = 1
  
        delhivery_charge =50
        Final_Price= delhivery_charge + mf3.Book_Price
        Final_Value=Final_Price

        address = Customer.objects.filter(user=request.user)
        return render(request, 'suggestion/BuyT.html', {'Final_Price':Final_Price,'mf3':mf3,'address':address,'Final_Value':Final_Value,'quantity':quantity})
    else:   
        return redirect('login') 
    

def Buy_Now_Payment(request, id):
    if request.user.is_authenticated:
        selected_address_id = request.POST.get('selected_address')
        mf = Kids.objects.get(pk=id)
  
        delhivery_charge =50
        Final_Price= delhivery_charge + mf.Book_Price
        address = Customer.objects.filter(user=request.user)
        
    host = request.get_host()   # Will fecth the domain site is currently hosted on.

    paypal_checkout = {
        'business': settings.PAYPAL_RECEIVER_EMAIL,
        'amount': Final_Price,
        'item_name': 'Pet',
        'invoice': uuid.uuid4(),
        'currency_code': 'USD',
        'notify_url': f"http://{host}{reverse('paypal-ipn')}",
       'return_url': f"http://{host}{reverse('buynowpaymentsuccess', args=[selected_address_id, id])}",
        'cancel_url': f"http://{host}{reverse('paymentfailed')}",
    }
    paypal_payment = PayPalPaymentsForm(initial=paypal_checkout)
    return render(request, 'suggestion/Payment.html',{'address':address,'paypal':paypal_payment, 'Final_Price':Final_Price, 'mf':mf})


def buynow_payment_success(request,selected_address_id,id):
    print('payment sucess',selected_address_id)   # we have fetch this id from return_url': f"http://{host}{reverse('paymentsuccess', args=[selected_address_id])}
                                                  # This id contain address detail of particular customer
    user =request.user
    customer_data = Customer.objects.get(pk=selected_address_id,)
    
    mf = Kids.objects.get(pk=id)
    Order(user=user,customer=customer_data,Kids=mf,quantity=1).save()
   
    return render(request,'suggestion/buynow_payment_success.html')


def Buy_Now_Paymentl(request, id):
    if request.user.is_authenticated:
        selected_address_id = request.POST.get('selected_address')
        mf1 = Love.objects.get(pk=id)
  
        delhivery_charge =50
        Final_Price= delhivery_charge + mf1.Book_Price
        address = Customer.objects.filter(user=request.user)
        
    host = request.get_host()   # Will fecth the domain site is currently hosted on.

    paypal_checkout = {
        'business': settings.PAYPAL_RECEIVER_EMAIL,
        'amount': Final_Price,
        'item_name': 'Pet',
        'invoice': uuid.uuid4(),
        'currency_code': 'USD',
        'notify_url': f"http://{host}{reverse('paypal-ipn')}",
       'return_url': f"http://{host}{reverse('buynowpaymentsuccessl', args=[selected_address_id, id])}",
        'cancel_url': f"http://{host}{reverse('paymentfailed')}",
    }
    paypal_payment = PayPalPaymentsForm(initial=paypal_checkout)
    return render(request, 'suggestion/Payment.html',{'address':address,'paypal':paypal_payment, 'Final_Price':Final_Price, 'mf1':mf1})
    

def buynow_payment_successl(request,selected_address_id,id):
    print('payment sucess',selected_address_id)   # we have fetch this id from return_url': f"http://{host}{reverse('paymentsuccess', args=[selected_address_id])}
                                                  # This id contain address detail of particular customer
    user =request.user
    customer_data = Customer.objects.get(pk=selected_address_id,)
    
    mf1 = Love.objects.get(pk=id)
    Order1(user=user,customer=customer_data,Love=mf1,quantity=1).save()
   
    return render(request,'suggestion/buynow_payment_success.html')


def Buy_Now_PaymentS(request, id):
    if request.user.is_authenticated:
        selected_address_id = request.POST.get('selected_address')
        mf2 = S.objects.get(pk=id)
  
        delhivery_charge =50
        Final_Price= delhivery_charge + mf2.Book_Price
        address = Customer.objects.filter(user=request.user)
        
    host = request.get_host()   # Will fecth the domain site is currently hosted on.

    paypal_checkout = {
        'business': settings.PAYPAL_RECEIVER_EMAIL,
        'amount': Final_Price,
        'item_name': 'Pet',
        'invoice': uuid.uuid4(),
        'currency_code': 'USD',
        'notify_url': f"http://{host}{reverse('paypal-ipn')}",
       'return_url': f"http://{host}{reverse('buynowpaymentsuccesss', args=[selected_address_id, id])}",
        'cancel_url': f"http://{host}{reverse('paymentfailed')}",
    }
    paypal_payment = PayPalPaymentsForm(initial=paypal_checkout)
    return render(request, 'suggestion/Payment.html',{'address':address,'paypal':paypal_payment, 'Final_Price':Final_Price, 'mf2':mf2})
    

def buynow_payment_successS(request,selected_address_id,id):
    print('payment sucess',selected_address_id)   # we have fetch this id from return_url': f"http://{host}{reverse('paymentsuccess', args=[selected_address_id])}
                                                  # This id contain address detail of particular customer
    user =request.user
    customer_data = Customer.objects.get(pk=selected_address_id,)
    
    mf2 = Sci_Fyi.objects.get(pk=id)
    Order2(user=user,customer=customer_data,Sci_Fyi=mf2,quantity=1).save()
   
    return render(request,'suggestion/buynow_payment_success.html')


def Buy_Now_PaymentT(request, id):
    if request.user.is_authenticated:
        selected_address_id = request.POST.get('selected_address')
        mf3 = Story.objects.get(pk=id)
  
        delhivery_charge =50
        Final_Price= delhivery_charge + mf3.Book_Price
        address = Customer.objects.filter(user=request.user)
        
    host = request.get_host()   # Will fecth the domain site is currently hosted on.

    paypal_checkout = {
        'business': settings.PAYPAL_RECEIVER_EMAIL,
        'amount': Final_Price,
        'item_name': 'Pet',
        'invoice': uuid.uuid4(),
        'currency_code': 'USD',
        'notify_url': f"http://{host}{reverse('paypal-ipn')}",
       'return_url': f"http://{host}{reverse('buynowpaymentsuccesst', args=[selected_address_id, id])}",
        'cancel_url': f"http://{host}{reverse('paymentfailed')}",
    }
    paypal_payment = PayPalPaymentsForm(initial=paypal_checkout)
    return render(request, 'suggestion/Payment.html',{'address':address,'paypal':paypal_payment, 'Final_Price':Final_Price, 'mf3':mf3})
    

def buynow_payment_successT(request,selected_address_id,id):
    print('payment sucess',selected_address_id)   # we have fetch this id from return_url': f"http://{host}{reverse('paymentsuccess', args=[selected_address_id])}
                                                  # This id contain address detail of particular customer
    user =request.user
    customer_data = Customer.objects.get(pk=selected_address_id,)
    
    mf3 = Story.objects.get(pk=id)
    Order3(user=user,customer=customer_data,Story=mf3,quantity=1).save()
   
    return render(request,'suggestion/buynow_payment_success.html')








# Create your views here.




