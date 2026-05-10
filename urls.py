from django.urls import path
from . import views

urlpatterns = [
    path('scan/', views.add_product),          # POST to save product
    path('scan/<str:qr_code>/', views.get_product),  # GET product by QR
]