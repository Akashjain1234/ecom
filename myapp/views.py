from multiprocessing import context
from django.contrib.auth import forms
from django.shortcuts import redirect, render
from django.urls.conf import path
from .form import SignupForm
from .form import AddressForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from .models import *
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
import razorpay
from django.core.paginator import Paginator



# -------------- Shop --------------------

def HomeView(request):
    if request.user.is_authenticated:
        all_mcate = MainCategoryModel.objects.all()
        show_data = ProductModel.objects.all()
        all_data = ProductModel.objects.order_by("?")
        cart_items = CartModel.objects.filter(user=request.user)
        cart_count = CartModel.objects.filter(user=request.user).count()
        paginator = Paginator(show_data, 8, orphans=1)
        page_number = request.GET.get('page')
        show_data = paginator.get_page(page_number)
        #product filter 
        men = ProductModel.objects.filter(mcate__id = 1)[:8]
        women = ProductModel.objects.filter(mcate__id = 3)[:8]
        kids = ProductModel.objects.filter(mcate__id = 4)[:8]
        context = {'men':men,'women':women,'kids':kids,'all_mcate':all_mcate,'all_products':show_data,'cart_items':cart_items,'cart_count':cart_count,'page_number':page_number,'all_data':all_data}
    else:
        messages.info(request,'Please Login First')
        return redirect('/signin/')
    return render(request,'home.html',context)
    
def CheckoutView(request):
    cart_count = CartModel.objects.filter(user=request.user).count()
    cart_items = CartModel.objects.filter(user=request.user)
    list1 = []
    sum = 0
    subtotal = 0
    total = 50
    all_address = AddressModel.objects.filter(user=request.user)
    for x in cart_items:
        z = x.product.sell_price*x.quantity
        sum = sum + z
        list1.append(sum)
        subtotal = list1[-1]
        total = subtotal + 50
    amount = total * 100 
    client = razorpay.Client(auth=('rzp_test_3MiCqcvhaYTvEk','woHlvwzlT0Q5jpeHm4jjaQx4'))
    response = client.order.create({'amount':amount,'currency':'INR','payment_capture':1})
    user = authenticate(address=address)
    if cart_count == 0:
        return render(request,'cart.html')
    else:
        con = {'all_address':all_address,'user':user,'cart_items':cart_items,'cart_count':cart_count,'subtotal':subtotal,'total':total,'response':response}
        return render(request,'checkout.html',con)

def OrderView(request):
    get_add = request.GET.get('all_address')
    cart_items = CartModel.objects.filter(user=request.user)
    for x in cart_items:
        prod = x.product
        qty = x.quantity
        if get_add:
            add = AddressModel.objects.get(id=get_add)
            Placeorder(user=request.user,product=prod,address=add,quantity=qty).save()
            x.delete()
    ord = Placeorder.objects.filter(user=request.user)
    con = {'placeord':ord,'cart_items':cart_items}
    return render(request,'order.html',con)

def CartView(request):
    cart_items = CartModel.objects.filter(user=request.user)
    cart_count = CartModel.objects.filter(user=request.user).count()
    list1 = []
    subtotal = 0
    total = 0
    sum = 0
    for x in cart_items:
       z = x.product.sell_price*x.quantity
       sum = sum + z
       list1.append(sum)
       subtotal = list1[-1]
       total = subtotal + 50
    context = {'cart_items':cart_items,'cart_count':cart_count,'subtotal':subtotal,'total':total}
    return render(request,'cart.html',context)



def addcartview(request,id):
    user = request.user
    prod = ProductModel.objects.get(id=id)
    prod_id = CartModel.objects.filter(product__id=id,user=request.user).exists()
    if prod_id:
        cart = CartModel.objects.get(product__id=id)
        cart.quantity += 1
        cart.save()
        return redirect('/cart/')
    else:
        CartModel(user = user,product = prod).save()
        return redirect('/home/')

def AllproductsView(request):
    all_mcate = MainCategoryModel.objects.all()
    cid = request.GET.get("cid")
    if cid:
        all_products = ProductModel.objects.filter(mcate__id=cid)
    else:
        all_products = ProductModel.objects.all()
    paginator = Paginator(all_products, 8, orphans=1)
    page_number = request.GET.get('page')
    show_data = paginator.get_page(page_number)
    context = {'all_mcate':all_mcate,'all_products':show_data}
    return render(request,'allproducts.html',context)
    
def ProductinformationView(request,id):
    get_product = ProductModel.objects.get(id=id)
    context ={'get_product':get_product}
    return render(request,'productinformation.html',context)

def ContactView(request):
    return render(request,'contact.html')



def BlogView(request):
    return render(request,'blog.html')

def SearchView(request):
    return render(request,'Search.html')

def DeleteView(request,id):
    productdel = CartModel.objects.get(id=id)
    productdel.delete()
    return redirect("/cart/")

def PlusView(request,id):
    cart_obj = CartModel.objects.get(id=id)
    cart_obj.quantity += 1
    cart_obj.save()
    return redirect("/cart/")

def MinusView(request,id):
    cart_obj = CartModel.objects.get(id=id)
    cart_obj.quantity -= 1
    cart_obj.save()
    if cart_obj.quantity <= 0:
        cart_obj.delete()
    return redirect("/cart/")

def address(request):
    form = AddressForm()
    if request.method == 'POST':
        form = AddressForm(request.POST)
        if form.is_valid():
            x = form.save(commit=False)
            x.user = request.user
            x.save()
            return redirect('/address/')
        else:
            pass
    context = {'form':form}
    return render(request,"address.html",context)


def searchview(request):
    get_name = request.GET['s_name']
    all_main_product = ProductModel.objects.filter(name__icontains=get_name)
    con = {'all_products':all_main_product}
    return render(request,"search.html",con)


# ---------------- Auth --------------------------

def SignupView(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'✔	User Successfully Registred...!')
            return redirect('/signup/')
    else:
        form = SignupForm()
    context = {'form':form}
    return render(request,'signup.html',context)


def SigninView(request):
    if request.method == 'POST':
        uname = request.POST.get('uname')
        upass = request.POST.get('upass')
        user = authenticate(username=uname,password=upass)
        if user == None:
            messages.info(request,'Please Enter Correct Username or Password....! ')
        login(request,user)
        messages.info(request,'Login Successful')
        return redirect('/home/')
    else:
        if request.user.is_authenticated:
            return redirect('/home/')
    return render(request,'signin.html')


def Outuser(request):
    logout(request)
    messages.info(request,'User Successfully Logout')
    return redirect('/signin/')