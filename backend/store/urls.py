from django.urls import path
from . import views

urlpatterns = [
    path('404/', views.error_page, name='error_page'),
]
