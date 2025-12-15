from django.contrib import admin
from .models import Vendor, VendorReview

@admin.register(Vendor)
class VendorAdmin(admin.ModelAdmin):
    list_display = ('store_name', 'user', 'is_approved', 'is_active', 'commission_rate', 'created_at')
    list_filter = ('is_approved', 'is_active', 'created_at')
    search_fields = ('store_name', 'user__username', 'business_email')
    readonly_fields = ('created_at', 'updated_at')
    
    fieldsets = (
        ('Store Information', {
            'fields': ('user', 'store_name', 'store_description', 'store_logo', 'store_banner')
        }),
        ('Business Information', {
            'fields': ('business_email', 'business_phone', 'business_address', 'tax_id')
        }),
        ('Bank Details', {
            'fields': ('bank_name', 'account_number', 'account_holder_name')
        }),
        ('Status & Commission', {
            'fields': ('is_approved', 'is_active', 'commission_rate')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at')
        }),
    )

@admin.register(VendorReview)
class VendorReviewAdmin(admin.ModelAdmin):
    list_display = ('vendor', 'user', 'rating', 'created_at')
    list_filter = ('rating', 'created_at')
    search_fields = ('vendor__store_name', 'user__username', 'review')
    readonly_fields = ('created_at',)
