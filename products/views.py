from django.shortcuts import render
from .models import Product
# Create your views here.
def home_view(request):
    
    product = Product.objects.all()
    context = {
        'products' : product
    }
    return render(request, 'home_view.html', context= context)