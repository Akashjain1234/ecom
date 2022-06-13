from django.urls import path
from myapp.views import *


urlpatterns = [
    # ----------------------- Shop ---------------------------
    
    path('home/',HomeView),
    path('checkout/',CheckoutView),
    path('cart/',CartView),
    path('addtocart/<int:id>/',addcartview),
    path('allproducts/',AllproductsView),
    path('productinformation/<int:id>/',ProductinformationView),
    path('contact/',ContactView),
    path('blog/',BlogView),
    path('search/',SearchView),
    path('delete/<int:id>/', DeleteView),
    path('MinusView/<int:id>/',MinusView,name='MinusView'),
    path('PlusView/<int:id>/',PlusView,name='PlusView'),
    path('address/',address,name='address'),
    path('order/',OrderView,name = "order"),
    path('searchview/',searchview,name = "searchview"),


    # ----------------------- Auth ---------------------------
    
    path('signup/',SignupView),
    path('signin/',SigninView),
    path('out/',Outuser),

]