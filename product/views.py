from django.shortcuts import render
from .models import Product

# Create your views here.
def browse(request):
    
    # fetch products from database
    productList = Product.objects.all()
    print(productList)
    
    context = {
        'productList': productList,
    }
    
    return render(request, "browse.html", context)