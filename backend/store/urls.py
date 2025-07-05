from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='home'),
    path('404/', views.error_page, name='error_page'),
    path('about-us/', views.about_us, name='about_us'),
    path('cart/', views.cart_variant, name='cart_variant'),
    path('checkout/', views.checkout, name='checkout'),
    path('contact/', views.contact_us, name='contact_us'),
    path('faqs/', views.faqs, name='faqs'),
    path('login/', views.login_page, name='login'),
    path('register/', views.register_page, name='register'),
    path('product-count/', views.product_count_page, name='product_count'),
    path('shop/', views.shop_grid, name='shop_grid'),
    path('wishlist/', views.wishlist, name='wishlist'),
]