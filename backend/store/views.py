from django.shortcuts import render

def home_page(request):
    return render(request, 'home.html')

def about_us(request):
    return render(request, 'about-us.html')

def cart_variant(request):
    return render(request, 'cart-variant2.html')

def checkout(request):
    return render(request, 'checkout.html')

def contact_us(request):
    return render(request, 'contact-us.html')

def faqs(request):
    return render(request, 'faqs.html')

def login_page(request):
    return render(request, 'login.html')

def register_page(request):
    return render(request, 'register.html') 

def product_count_page(request):
    return render(request, 'product-visitor-sold-count.html')

def shop_grid(request):
    return render(request, 'shop-grid-3.html')

def wishlist(request):
    return render(request, 'wishlist.html')

def error_page(request):
    return render(request, '404.html')