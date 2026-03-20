from django.urls import path
from . import views

urlpatterns = [
    path('', views.insurance_home, name='insurance_home'),
    path('<int:pk>/', views.insurance_detail, name='insurance_detail'),
    path('quote/', views.quote_request, name='quote_request'),
    path('quote/<int:pk>/', views.quote_request, name='quote_request_product'),
]
