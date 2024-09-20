from django.shortcuts import render
from .models import Product, Category, Brand

def products_view(request):

    title = 'Mostrando todos los productos'
    products_to_show = Product.objects.all()

    if request.GET:
        category_value = request.GET.get('categories', default='')
        brand_value = request.GET.get('brands', default='')
        search_value = request.GET.get('search', default='')

        try:
            category = Category.objects.get(name=category_value)
        except:
            pass

        try: 
            brand = Brand.objects.get(name=brand_value)
        except:
            pass

        if category_value and brand_value:
            title = 'Filtrando ' + category_value + ' ' + brand_value
            products_to_show = Product.objects.filter(category=category, brand=brand)
        elif category_value:
            title = 'Filtrando categoría ' + category_value
            products_to_show = Product.objects.filter(category=category)
        elif brand_value:
            title = 'Filtrando marca ' + brand_value
            products_to_show = Product.objects.filter(brand=brand)
        elif search_value:
            title = 'Resultados de "' + search_value + '"'
            products_to_show = Product.objects.filter(name__icontains=search_value)

    context = {
        'all_categories' : Category.objects.all(),
        'all_brands' : Brand.objects.all(),
        'header' : title,
        'products_to_show': products_to_show
    }

    return render(request, 'products-view.html', context=context)

def product_detail_view(request, slug):

    product = Product.objects.get(slug=slug)

    context = {
        'product' : product,
        'product_button_type' : 'whatsapp'
    }
    
    return render(request, 'product-detail-view.html', context=context)
