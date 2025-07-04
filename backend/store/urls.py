from django.urls import path
from . import views

urlpatterns = [
    path('', views.error_page, name='home'),  # use 404.html as home
    path('404/', views.error_page, name='error_page'),
]


