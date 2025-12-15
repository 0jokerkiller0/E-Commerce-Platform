# Deployment Guide - E-Commerce Multivendor Platform

This guide will help you deploy your Django e-commerce platform to the web.

## Deployment Options

### Option 1: Render (Recommended - Free Tier Available)

Render provides free hosting for web applications with automatic deployments from GitHub.

#### Steps to Deploy on Render:

1. **Sign up for Render**
   - Go to [https://render.com](https://render.com)
   - Sign up using your GitHub account

2. **Create a New Web Service**
   - Click "New +" → "Web Service"
   - Connect your GitHub repository: `https://github.com/0jokerkiller0/E-Commerce-Platform`
   - Give it a name (e.g., `ecommerce-multivendor`)

3. **Configure the Service**
   - **Environment**: `Python 3`
   - **Build Command**: `pip install -r requirements.txt && python manage.py collectstatic --noinput && python manage.py migrate`
   - **Start Command**: `gunicorn ecommerce_multivendor.wsgi:application`
   - **Instance Type**: Free

4. **Add Environment Variables**
   Click "Advanced" and add these environment variables:
   ```
   SECRET_KEY=your-super-secret-key-here-change-this
   DEBUG=False
   ALLOWED_HOSTS=your-app-name.onrender.com
   ```

5. **Deploy**
   - Click "Create Web Service"
   - Wait for the build to complete (5-10 minutes)
   - Your site will be live at: `https://your-app-name.onrender.com`

6. **Create Superuser** (After first deployment)
   - Go to Render Dashboard → Your Service → Shell
   - Run: `python manage.py createsuperuser`
   - Follow the prompts to create admin account

---

### Option 2: PythonAnywhere (Free Tier Available)

PythonAnywhere offers free web hosting specifically for Python applications.

#### Steps to Deploy on PythonAnywhere:

1. **Sign up for PythonAnywhere**
   - Go to [https://www.pythonanywhere.com](https://www.pythonanywhere.com)
   - Create a free account

2. **Open a Bash Console**
   - From Dashboard, go to "Consoles" → "Bash"

3. **Clone Your Repository**
   ```bash
   git clone https://github.com/0jokerkiller0/E-Commerce-Platform.git
   cd E-Commerce-Platform
   ```

4. **Create Virtual Environment**
   ```bash
   python3.10 -m venv venv
   source venv/bin/activate
   ```

5. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

6. **Configure Web App**
   - Go to "Web" tab → "Add a new web app"
   - Choose "Manual Configuration" → Python 3.10
   - Set source code directory: `/home/yourusername/E-Commerce-Platform`
   - Set working directory: `/home/yourusername/E-Commerce-Platform`

7. **Configure WSGI File**
   - Click on WSGI configuration file link
   - Replace content with:
   ```python
   import os
   import sys
   
   path = '/home/yourusername/E-Commerce-Platform'
   if path not in sys.path:
       sys.path.append(path)
   
   os.environ['DJANGO_SETTINGS_MODULE'] = 'ecommerce_multivendor.settings'
   
   from django.core.wsgi import get_wsgi_application
   application = get_wsgi_application()
   ```

8. **Configure Virtual Environment**
   - In Web tab, set virtual environment path: `/home/yourusername/E-Commerce-Platform/venv`

9. **Configure Static Files**
   - URL: `/static/`
   - Directory: `/home/yourusername/E-Commerce-Platform/staticfiles`

10. **Set Environment Variables**
    - Go to Web tab → "Environment variables"
    - Add:
      - `SECRET_KEY`: `your-secret-key`
      - `DEBUG`: `False`
      - `ALLOWED_HOSTS`: `yourusername.pythonanywhere.com`

11. **Run Migrations**
    ```bash
    python manage.py migrate
    python manage.py collectstatic --noinput
    python manage.py createsuperuser
    ```

12. **Reload Web App**
    - Click "Reload" button in Web tab
    - Visit: `https://yourusername.pythonanywhere.com`

---

### Option 3: Railway (Easy Deployment)

1. **Sign up**: [https://railway.app](https://railway.app)
2. **New Project** → "Deploy from GitHub repo"
3. **Select your repository**
4. **Add environment variables** (same as Render)
5. **Deploy**

---

## Important Production Configuration

### Security Checklist

Before going live, ensure:

- [ ] `DEBUG = False` in production
- [ ] `SECRET_KEY` is changed and kept secret
- [ ] `ALLOWED_HOSTS` is properly configured
- [ ] Database is backed up regularly
- [ ] HTTPS is enabled (most platforms do this automatically)
- [ ] Media files are properly secured

### Database

For production, consider upgrading from SQLite to PostgreSQL:
- Most platforms offer free PostgreSQL databases
- Update `DATABASES` setting in `settings.py`

### Static and Media Files

- Static files are served via WhiteNoise (already configured)
- For media files in production, consider using:
  - AWS S3
  - Cloudinary
  - DigitialOcean Spaces

---

## Post-Deployment

After deployment:

1. **Access Admin Panel**: `https://your-domain.com/admin`
2. **Create test users and vendors**
3. **Add products and categories**
4. **Test the complete order flow**
5. **Configure email backend** for real emails

---

## Troubleshooting

### Static files not loading
- Run: `python manage.py collectstatic`
- Check `STATIC_ROOT` and `STATIC_URL` settings

### Database errors
- Run migrations: `python manage.py migrate`
- Check database connection settings

### 500 Server Error
- Check logs in your hosting platform
- Ensure `DEBUG=False` is set
- Verify all environment variables are set

---

## Support

For deployment issues:
- **Render**: [Render Docs](https://render.com/docs)
- **PythonAnywhere**: [PythonAnywhere Help](https://help.pythonanywhere.com)
- **Django**: [Django Deployment Checklist](https://docs.djangoproject.com/en/6.0/howto/deployment/checklist/)

---

## Quick Deploy Commands

```bash
# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Collect static files
python manage.py collectstatic --noinput

# Create superuser
python manage.py createsuperuser

# Run server (development)
python manage.py runserver

# Run with Gunicorn (production)
gunicorn ecommerce_multivendor.wsgi:application
```
