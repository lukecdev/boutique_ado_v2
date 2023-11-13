from django.shortcuts import render
from .models import Product, et_object_or_404

# Create your views here.

def all_products(request):
    """ A view to show all products, including sorting and search queries """

    products = Product.objects.all()

    context = {
        'products': products,
    }

    return render(request, 'products/products.html', context)

def product_detail(request, product_id):
    """ A view to show individual prduct details """

    product = get_object_or_404(product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_detail.html', context)