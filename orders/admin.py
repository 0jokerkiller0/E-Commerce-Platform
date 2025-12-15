from django.contrib import admin
from .models import Order, OrderItem, OrderTracking, Payment

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0
    readonly_fields = ('created_at',)

class OrderTrackingInline(admin.TabularInline):
    model = OrderTracking
    extra = 0
    readonly_fields = ('created_at',)

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('order_number', 'user', 'status', 'payment_status', 'total', 'created_at')
    list_filter = ('status', 'payment_status', 'payment_method', 'created_at')
    search_fields = ('order_number', 'user__username', 'user__email', 'shipping_email')
    readonly_fields = ('order_number', 'created_at', 'updated_at')
    inlines = [OrderItemInline, OrderTrackingInline]
    
    fieldsets = (
        ('Order Information', {
            'fields': ('order_number', 'user', 'status', 'payment_status', 'payment_method')
        }),
        ('Pricing', {
            'fields': ('subtotal', 'tax', 'shipping_cost', 'discount', 'total')
        }),
        ('Shipping Address', {
            'fields': ('shipping_name', 'shipping_email', 'shipping_phone', 'shipping_address', 
                      'shipping_city', 'shipping_state', 'shipping_country', 'shipping_pincode')
        }),
        ('Billing Address', {
            'fields': ('billing_name', 'billing_email', 'billing_phone', 'billing_address', 
                      'billing_city', 'billing_state', 'billing_country', 'billing_pincode'),
            'classes': ('collapse',)
        }),
        ('Additional Information', {
            'fields': ('notes', 'coupon_code')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at')
        }),
    )

@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('order', 'product_name', 'vendor', 'quantity', 'price', 'total')
    list_filter = ('created_at',)
    search_fields = ('order__order_number', 'product_name', 'vendor__store_name')

@admin.register(OrderTracking)
class OrderTrackingAdmin(admin.ModelAdmin):
    list_display = ('order', 'status', 'location', 'created_at')
    list_filter = ('status', 'created_at')
    search_fields = ('order__order_number', 'description')

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('payment_id', 'order', 'payment_method', 'amount', 'status', 'created_at')
    list_filter = ('status', 'payment_method', 'created_at')
    search_fields = ('payment_id', 'order__order_number', 'transaction_id')
    readonly_fields = ('created_at', 'updated_at')
