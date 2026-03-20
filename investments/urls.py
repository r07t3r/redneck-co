from django.urls import path
from . import views

urlpatterns = [
    path('', views.investments_home, name='investments_home'),
    path('<int:pk>/', views.investment_detail, name='investment_detail'),
    path('consult/', views.consultation_request, name='consultation_request'),
    path('consult/<int:pk>/', views.consultation_request, name='consultation_request_product'),
]
