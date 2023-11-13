from django.shortcuts import render
from .models import Product

# Create your views here.

def all_products(request):
    """ A view to show all products, inculding sorting and search queries """

    products = Product.objects.all()

    contect = {
        'products': products,
    }
    
    return render(request, 'products/products.html', context)
