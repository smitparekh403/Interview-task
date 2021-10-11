from django.shortcuts import render
from django.http import HttpResponse
from .models.product import Product

# Create your views here.
def index(request):
   prds = Product.get_all_products()
   return render(request , 'index.html' , {'products' : prds})



def signup(request):
    return render(request , 'signup.html')
