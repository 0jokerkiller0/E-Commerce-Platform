from django.shortcuts import render
from products.models import Product, Category
from vendors.models import Vendor

def home(request):
    """Home page view"""
    featured_products = Product.objects.filter(is_active=True, is_featured=True)[:8]
    bestseller_products = Product.objects.filter(is_active=True, is_bestseller=True)[:8]
    categories = Category.objects.filter(is_active=True, parent=None)[:6]
    
    context = {
        'featured_products': featured_products,
        'bestseller_products': bestseller_products,
        'categories': categories,
    }
    return render(request, 'home.html', context)
