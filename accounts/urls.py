from django.urls import path
from . import views

urlpatterns = [
    path('profile/', views.profile_view, name='profile'),
    path('orders/', views.orders_view, name='orders'),
    path('dashboard/', views.vendor_dashboard, name='vendor_dashboard'),
    path('products/', views.vendor_products, name='vendor_products'),
]