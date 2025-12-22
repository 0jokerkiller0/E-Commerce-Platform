from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import User
from .forms import CustomUserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from orders.models import Order

@login_required
def profile_view(request):
    """Display user profile"""
    context = {
        'user': request.user
    }
    return render(request, 'profile.html', context)

@login_required
def orders_view(request):
    """Display user orders"""
    orders = Order.objects.filter(user=request.user).order_by('-created_at')
    context = {
        'orders': orders
    }
    return render(request, 'orders.html', context)

@login_required
def vendor_dashboard(request):
    """Display vendor dashboard"""
    # This would need to be implemented with vendor-specific data
    context = {
        'user': request.user
    }
    return render(request, 'vendor_dashboard.html', context)

@login_required
def vendor_products(request):
    """Display vendor products"""
    # This would need to be implemented with vendor-specific data
    context = {
        'user': request.user
    }
    return render(request, 'vendor_products.html', context)

def login_view(request):
    """Handle user login"""
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                # Redirect based on user type
                if user.user_type == 'admin':
                    return redirect('/admin/')
                elif user.user_type == 'vendor':
                    return redirect('vendor_dashboard')
                else:  # customer
                    return redirect('home')
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    else:
        form = AuthenticationForm()
        # Add placeholders and CSS classes to the form fields
        form.fields['username'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Enter your username'
        })
        form.fields['password'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Enter your password'
        })
    
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    """Handle user logout"""
    logout(request)
    messages.info(request, 'You have been logged out.')
    return render(request, 'logout.html')

def register_view(request):
    """Handle user registration"""
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            
            # Log in the user
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            messages.success(request, f'Account created for {username}!')
            
            # Redirect based on user type
            if user.user_type == 'vendor':
                return redirect('vendor_dashboard')
            else:  # customer or admin
                return redirect('home')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = CustomUserCreationForm()
    
    return render(request, 'register.html', {'form': form})