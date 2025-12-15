from django.db import models
from django.conf import settings

class Vendor(models.Model):
    """Vendor/Seller Model"""
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='vendor_profile')
    store_name = models.CharField(max_length=200)
    store_description = models.TextField(blank=True, null=True)
    store_logo = models.ImageField(upload_to='vendor/logos/', blank=True, null=True)
    store_banner = models.ImageField(upload_to='vendor/banners/', blank=True, null=True)
    
    # Business Information
    business_email = models.EmailField()
    business_phone = models.CharField(max_length=15)
    business_address = models.TextField()
    tax_id = models.CharField(max_length=50, blank=True, null=True)
    
    # Bank Details for Payment
    bank_name = models.CharField(max_length=100, blank=True, null=True)
    account_number = models.CharField(max_length=50, blank=True, null=True)
    account_holder_name = models.CharField(max_length=100, blank=True, null=True)
    
    # Status
    is_approved = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    
    # Commission
    commission_rate = models.DecimalField(max_digits=5, decimal_places=2, default=10.00, help_text="Commission percentage")
    
    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.store_name
    
    class Meta:
        verbose_name = 'Vendor'
        verbose_name_plural = 'Vendors'
        ordering = ['-created_at']


class VendorReview(models.Model):
    """Vendor Review Model"""
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)])
    review = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.vendor.store_name} - {self.rating} stars"
    
    class Meta:
        verbose_name = 'Vendor Review'
        verbose_name_plural = 'Vendor Reviews'
        unique_together = ('vendor', 'user')
        ordering = ['-created_at']
