from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from products.models import Category, Product
from vendors.models import Vendor
from accounts.models import User

class Command(BaseCommand):
    help = 'Create sample data for demonstration purposes'

    def handle(self, *args, **options):
        # Create categories
        categories_data = [
            {'name': 'Electronics', 'slug': 'electronics', 'is_active': True},
            {'name': 'Fashion', 'slug': 'fashion', 'is_active': True},
            {'name': 'Home & Living', 'slug': 'home-living', 'is_active': True},
            {'name': 'Sports', 'slug': 'sports', 'is_active': True},
            {'name': 'Books', 'slug': 'books', 'is_active': True},
        ]
        
        for cat_data in categories_data:
            category, created = Category.objects.get_or_create(
                slug=cat_data['slug'],
                defaults=cat_data
            )
            if created:
                self.stdout.write(f'Created category: {category.name}')
            else:
                self.stdout.write(f'Category already exists: {category.name}')

        # Create vendor users
        User = get_user_model()
        vendor_users = []
        
        # Create vendor users
        vendor_data = [
            {'username': 'techstore', 'email': 'tech@store.com', 'password': 'vendor123', 'user_type': 'vendor'},
            {'username': 'fashionhub', 'email': 'fashion@hub.com', 'password': 'vendor123', 'user_type': 'vendor'},
            {'username': 'sportszone', 'email': 'sports@zone.com', 'password': 'vendor123', 'user_type': 'vendor'},
        ]
        
        for data in vendor_data:
            vendor_user, created = User.objects.get_or_create(
                username=data['username'],
                defaults={
                    'email': data['email'],
                    'user_type': data['user_type']
                }
            )
            if created:
                vendor_user.set_password(data['password'])
                vendor_user.save()
                self.stdout.write(f'Created vendor user: {vendor_user.username}')
            else:
                self.stdout.write(f'Vendor user already exists: {vendor_user.username}')
            vendor_users.append(vendor_user)

        # Create vendor profiles
        vendor_profiles_data = [
            {
                'user': vendor_users[0],
                'store_name': 'Tech Store',
                'store_description': 'Your one-stop shop for all electronics and gadgets',
                'business_email': 'tech@store.com',
                'business_phone': '+91 9876543210',
                'business_address': '123 Tech Street, Electronic City',
                'is_active': True
            },
            {
                'user': vendor_users[1],
                'store_name': 'Fashion Hub',
                'store_description': 'Trendy fashion and accessories for everyone',
                'business_email': 'fashion@hub.com',
                'business_phone': '+91 9876543211',
                'business_address': '456 Fashion Avenue, Style City',
                'is_active': True
            },
            {
                'user': vendor_users[2],
                'store_name': 'Sports Zone',
                'store_description': 'Premium sports gear and fitness equipment',
                'business_email': 'sports@zone.com',
                'business_phone': '+91 9876543212',
                'business_address': '789 Sports Road, Fitness City',
                'is_active': True
            }
        ]
        
        for profile_data in vendor_profiles_data:
            vendor_profile, created = Vendor.objects.get_or_create(
                user=profile_data['user'],
                defaults={
                    'store_name': profile_data['store_name'],
                    'store_description': profile_data['store_description'],
                    'business_email': profile_data['business_email'],
                    'business_phone': profile_data['business_phone'],
                    'business_address': profile_data['business_address'],
                    'is_active': profile_data['is_active']
                }
            )
            if created:
                self.stdout.write(f'Created vendor profile: {vendor_profile.store_name}')
            else:
                self.stdout.write(f'Vendor profile already exists: {vendor_profile.store_name}')

        # Get categories and vendors for products
        electronics_cat = Category.objects.get(slug='electronics')
        fashion_cat = Category.objects.get(slug='fashion')
        sports_cat = Category.objects.get(slug='sports')
        
        tech_store_vendor = Vendor.objects.get(store_name='Tech Store')
        fashion_hub_vendor = Vendor.objects.get(store_name='Fashion Hub')
        sports_zone_vendor = Vendor.objects.get(store_name='Sports Zone')

        # Create sample products
        products_data = [
            # Electronics
            {
                'name': 'Premium Wireless Headphones',
                'slug': 'premium-wireless-headphones',
                'category': electronics_cat,
                'vendor': tech_store_vendor,
                'description': 'High-quality wireless headphones with noise cancellation',
                'price': 2499.00,
                'compare_price': 2999.00,
                'stock': 50,
                'is_active': True,
                'is_featured': True
            },
            {
                'name': 'Smart Watch Series 5',
                'slug': 'smart-watch-series-5',
                'category': electronics_cat,
                'vendor': tech_store_vendor,
                'description': 'Advanced smartwatch with health monitoring features',
                'price': 15999.00,
                'compare_price': 17999.00,
                'stock': 30,
                'is_active': True,
                'is_featured': True
            },
            # Fashion
            {
                'name': 'Designer Cotton T-Shirt',
                'slug': 'designer-cotton-tshirt',
                'category': fashion_cat,
                'vendor': fashion_hub_vendor,
                'description': 'Comfortable and stylish cotton t-shirt for everyday wear',
                'price': 799.00,
                'compare_price': 999.00,
                'stock': 100,
                'is_active': True,
                'is_featured': True
            },
            {
                'name': 'Leather Jacket',
                'slug': 'leather-jacket',
                'category': fashion_cat,
                'vendor': fashion_hub_vendor,
                'description': 'Genuine leather jacket for a stylish look',
                'price': 4999.00,
                'compare_price': 5999.00,
                'stock': 25,
                'is_active': True,
                'is_featured': False
            },
            # Sports
            {
                'name': 'Running Shoes Pro',
                'slug': 'running-shoes-pro',
                'category': sports_cat,
                'vendor': sports_zone_vendor,
                'description': 'Professional running shoes for athletes',
                'price': 3199.00,
                'compare_price': 3999.00,
                'stock': 40,
                'is_active': True,
                'is_featured': True
            },
            {
                'name': 'Yoga Mat Premium',
                'slug': 'yoga-mat-premium',
                'category': sports_cat,
                'vendor': sports_zone_vendor,
                'description': 'Non-slip premium yoga mat for all your yoga sessions',
                'price': 1299.00,
                'compare_price': 1499.00,
                'stock': 60,
                'is_active': True,
                'is_featured': False
            }
        ]
        
        for product_data in products_data:
            product, created = Product.objects.get_or_create(
                slug=product_data['slug'],
                defaults=product_data
            )
            if created:
                self.stdout.write(f'Created product: {product.name}')
            else:
                self.stdout.write(f'Product already exists: {product.name}')

        self.stdout.write(
            self.style.SUCCESS('Successfully created sample data!')
        )
