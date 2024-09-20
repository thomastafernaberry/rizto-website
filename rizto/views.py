from django.shortcuts import render
from products.models import Product 

def home_view(request):
    featured_products = []
    for product in Product.objects.all():
        if product.isFeatured:
            featured_products = featured_products + [product]

    context = {
        'featured_products' : featured_products
    }

    return render(request, 'home-view.html', context=context) # WHY IT TAKES REQUEST?
