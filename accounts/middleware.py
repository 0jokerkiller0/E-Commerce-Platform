from django.shortcuts import redirect
from django.contrib import messages
from django.urls import reverse

class AdminAccessMiddleware:
    """
    Middleware to restrict admin panel access to users with user_type 'admin' or superuser status
    """
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Check if the request is for the admin panel
        if request.path.startswith('/admin/'):
            # Check if user is authenticated
            if request.user.is_authenticated:
                # Allow access if user is a superuser or has the correct user_type
                if not (request.user.is_superuser or request.user.user_type == 'admin'):
                    messages.error(request, 'You do not have permission to access the admin panel.')
                    return redirect('home')
            else:
                # Let Django's built-in authentication handle unauthenticated users
                pass
        
        response = self.get_response(request)
        return response