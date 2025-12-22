from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.http import JsonResponse
from products.models import Product
from .models import Cart, CartItem

def cart_view(request):
    """Display shopping cart"""
    cart = None
    
    if request.user.is_authenticated:
        cart, created = Cart.objects.get_or_create(user=request.user)
    else:
        session_key = request.session.session_key
        if not session_key:
            request.session.create()
            session_key = request.session.session_key
        cart, created = Cart.objects.get_or_create(session_key=session_key)
    
    context = {
        'cart': cart
    }
    return render(request, 'cart.html', context)

def add_to_cart(request, product_id):
    """Add product to cart"""
    if request.method == 'POST':
        product = get_object_or_404(Product, id=product_id, is_active=True)
        quantity = int(request.POST.get('quantity', 1))
        
        if request.user.is_authenticated:
            cart, created = Cart.objects.get_or_create(user=request.user)
        else:
            session_key = request.session.session_key
            if not session_key:
                request.session.create()
                session_key = request.session.session_key
            cart, created = Cart.objects.get_or_create(session_key=session_key)
        
        # Check if item already in cart
        cart_item, created = CartItem.objects.get_or_create(
            cart=cart,
            product=product,
            defaults={'quantity': quantity}
        )
        
        # If item already exists, update quantity
        if not created:
            cart_item.quantity += quantity
            cart_item.save()
        
        messages.success(request, f'{product.name} added to cart successfully!')
        
        # Return JSON response for AJAX requests
        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            return JsonResponse({
                'success': True,
                'message': f'{product.name} added to cart successfully!',
                'cart_items_count': cart.get_total_items()
            })
        
        return redirect('cart')
    
    return redirect('products_list')

def remove_from_cart(request, item_id):
    """Remove item from cart"""
    cart_item = get_object_or_404(CartItem, id=item_id)
    
    # Check if user owns this cart item
    if request.user.is_authenticated:
        if cart_item.cart.user != request.user:
            messages.error(request, 'You do not have permission to remove this item.')
            return redirect('cart')
    else:
        session_key = request.session.session_key
        if cart_item.cart.session_key != session_key:
            messages.error(request, 'You do not have permission to remove this item.')
            return redirect('cart')
    
    product_name = cart_item.product.name
    cart_item.delete()
    messages.success(request, f'{product_name} removed from cart.')
    
    return redirect('cart')

def update_cart_item(request, item_id):
    """Update cart item quantity"""
    if request.method == 'POST':
        cart_item = get_object_or_404(CartItem, id=item_id)
        quantity = int(request.POST.get('quantity', 1))
        
        # Check if user owns this cart item
        if request.user.is_authenticated:
            if cart_item.cart.user != request.user:
                messages.error(request, 'You do not have permission to update this item.')
                return redirect('cart')
        else:
            session_key = request.session.session_key
            if cart_item.cart.session_key != session_key:
                messages.error(request, 'You do not have permission to update this item.')
                return redirect('cart')
        
        if quantity <= 0:
            cart_item.delete()
            messages.success(request, 'Item removed from cart.')
        else:
            cart_item.quantity = quantity
            cart_item.save()
            messages.success(request, 'Cart updated successfully.')
        
        return redirect('cart')
    
    return redirect('cart')
