from django.contrib import admin
from .models import InvestmentProduct, InvestmentConsultationRequest


@admin.register(InvestmentProduct)
class InvestmentProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'product_type', 'risk_level', 'min_investment', 'is_active', 'is_featured', 'order']
    list_filter = ['product_type', 'risk_level', 'is_active', 'is_featured']
    search_fields = ['name', 'description']
    list_editable = ['is_active', 'is_featured', 'order']


@admin.register(InvestmentConsultationRequest)
class InvestmentConsultationRequestAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'email', 'investment_goal', 'initial_investment', 'created_at', 'is_contacted']
    list_filter = ['investment_goal', 'time_horizon', 'risk_tolerance', 'is_contacted']
    search_fields = ['first_name', 'last_name', 'email']
    list_editable = ['is_contacted']
    readonly_fields = ['created_at']
