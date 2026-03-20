from django.contrib import admin
from .models import InsuranceProduct, InsuranceQuoteRequest


@admin.register(InsuranceProduct)
class InsuranceProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'product_type', 'min_coverage', 'max_coverage', 'is_active', 'is_featured', 'order']
    list_filter = ['product_type', 'is_active', 'is_featured']
    search_fields = ['name', 'description']
    list_editable = ['is_active', 'is_featured', 'order']


@admin.register(InsuranceQuoteRequest)
class InsuranceQuoteRequestAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'email', 'phone', 'coverage_amount', 'created_at', 'is_contacted']
    list_filter = ['health_status', 'tobacco_use', 'gender', 'is_contacted']
    search_fields = ['first_name', 'last_name', 'email', 'phone']
    list_editable = ['is_contacted']
    readonly_fields = ['created_at']
