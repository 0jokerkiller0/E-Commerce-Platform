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

def products_list(request):
    """Display all products with optional category filtering"""
    products = Product.objects.filter(is_active=True)
    categories = Category.objects.filter(is_active=True)
    
    # Filter by category if specified
    category_id = request.GET.get('category')
    if category_id:
        products = products.filter(category_id=category_id)
    
    context = {
        'products': products,
        'categories': categories,
    }
    return render(request, 'products_list.html', context)

def vendors_list(request):
    """Display all vendors"""
    vendors = Vendor.objects.filter(is_active=True)
    
    context = {
        'vendors': vendors,
    }
    return render(request, 'vendors_list.html', context)

