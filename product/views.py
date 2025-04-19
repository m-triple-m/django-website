from django.shortcuts import render, get_object_or_404
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

def productDetails(request, product_id):

    product = get_object_or_404(Product, id=product_id)
    context = {
        "product": product
    }
    
    return render(request, "product_details.html", context)