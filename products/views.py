from django.shortcuts import render, get_object_or_404
from .models import Product

# Create your views here.
def product_detail_view(request, id):
    
    product = get_object_or_404(Product, id= id)
    context = {
        'products' : product
    }
    return render(request, 'product_detail.html', context= context)