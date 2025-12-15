# E-Commerce Multivendor Platform

A comprehensive multivendor e-commerce platform built with Django and Python.

## Features

### User Management
- Custom user model with multiple user types (Customer, Vendor, Admin)
- User authentication and authorization
- User profiles with additional information

### Vendor Management
- Vendor registration and approval system
- Vendor store management
- Vendor reviews and ratings
- Commission-based payment system
- Bank details for payment processing

### Product Management
- Product categories with hierarchical structure
- Product listings with multiple images
- Product reviews and ratings
- Wishlist functionality
- Stock management
- SEO optimization fields

### Shopping Cart
- Session-based and user-based cart
- Cart management (add, update, remove items)
- Cart persistence across sessions

### Order Management
- Complete order processing workflow
- Multiple payment methods (COD, Card, UPI, Wallet, Net Banking)
- Order tracking system
- Order status management
- Shipping and billing address management

### Payment System
- Multiple payment gateways support
- Payment status tracking
- Transaction history

## Installation

1. Clone the repository or navigate to the project directory

2. Create a virtual environment (recommended):
```bash
python -m venv venv
venv\Scripts\activate  # On Windows
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run migrations:
```bash
python manage.py makemigrations
python manage.py migrate
```

5. Create a superuser:
```bash
python manage.py createsuperuser
```

6. Run the development server:
```bash
python manage.py runserver
```

7. Access the application:
- Frontend: http://localhost:8000/
- Admin Panel: http://localhost:8000/admin/

## Project Structure

```
ecommerce_multivendor/
├── accounts/           # User management app
├── vendors/            # Vendor management app
├── products/           # Product management app
├── cart/               # Shopping cart app
├── orders/             # Order management app
├── ecommerce_multivendor/  # Main project settings
├── templates/          # HTML templates
├── static/             # Static files (CSS, JS, images)
├── media/              # User uploaded files
└── manage.py           # Django management script
```

## Models Overview

### Accounts
- **User**: Custom user model with user_type field

### Vendors
- **Vendor**: Vendor profile with store information
- **VendorReview**: Customer reviews for vendors

### Products
- **Category**: Product categories (hierarchical)
- **Product**: Product details with pricing and inventory
- **ProductImage**: Multiple images per product
- **ProductReview**: Customer product reviews
- **Wishlist**: User wishlist items

### Cart
- **Cart**: Shopping cart
- **CartItem**: Items in cart

### Orders
- **Order**: Customer orders
- **OrderItem**: Items in an order
- **OrderTracking**: Order status tracking
- **Payment**: Payment transactions

## Admin Panel

The Django admin panel provides comprehensive management for:
- User accounts
- Vendor applications and approvals
- Products and categories
- Orders and payments
- Reviews and ratings

## Configuration

Key settings in `settings.py`:
- `AUTH_USER_MODEL = 'accounts.User'` - Custom user model
- Media and static files configuration
- Database settings (SQLite by default)
- Email backend configuration

## Development

To add new features:
1. Create models in respective apps
2. Run `python manage.py makemigrations`
3. Run `python manage.py migrate`
4. Register models in admin.py
5. Create views and templates
6. Update URLs

## Security Notes

- Change `SECRET_KEY` in production
- Set `DEBUG = False` in production
- Configure proper email backend
- Set up HTTPS
- Configure allowed hosts
- Use environment variables for sensitive data

## Future Enhancements

- Frontend templates and UI
- Payment gateway integration (Razorpay, Stripe)
- Email notifications
- SMS notifications
- Advanced search and filters
- Analytics dashboard for vendors
- Coupon and discount system
- Product comparison
- Live chat support
- Mobile app API

## Technologies Used

- Python 3.13+
- Django 6.0
- SQLite (Development)
- Django REST Framework
- Crispy Forms
- Bootstrap 4

## License

This project is for educational purposes.

## Support

For issues and questions, please refer to the Django documentation:
- https://docs.djangoproject.com/
