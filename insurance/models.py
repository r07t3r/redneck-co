from django.db import models
from django.contrib.auth.models import User


class InsuranceProduct(models.Model):
    PRODUCT_TYPE_CHOICES = [
        ('term', 'Term Life Insurance'),
        ('whole', 'Whole Life Insurance'),
        ('universal', 'Universal Life Insurance'),
        ('variable', 'Variable Life Insurance'),
        ('final_expense', 'Final Expense Insurance'),
    ]

    name = models.CharField(max_length=150)
    product_type = models.CharField(max_length=30, choices=PRODUCT_TYPE_CHOICES)
    tagline = models.CharField(max_length=200)
    description = models.TextField()
    min_coverage = models.DecimalField(max_digits=12, decimal_places=2, default=50000)
    max_coverage = models.DecimalField(max_digits=12, decimal_places=2, default=1000000)
    min_age = models.PositiveSmallIntegerField(default=18)
    max_age = models.PositiveSmallIntegerField(default=80)
    features = models.TextField(help_text='One feature per line')
    is_active = models.BooleanField(default=True)
    is_featured = models.BooleanField(default=False)
    order = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['order', 'name']

    def __str__(self):
        return f"{self.name} ({self.get_product_type_display()})"

    def get_features_list(self):
        return [f.strip() for f in self.features.split('\n') if f.strip()]


class InsuranceQuoteRequest(models.Model):
    GENDER_CHOICES = [('M', 'Male'), ('F', 'Female'), ('O', 'Other')]
    HEALTH_CHOICES = [
        ('excellent', 'Excellent'),
        ('good', 'Good'),
        ('fair', 'Fair'),
        ('poor', 'Poor'),
    ]
    TOBACCO_CHOICES = [
        ('never', 'Never'),
        ('former', 'Former Smoker'),
        ('current', 'Current Smoker'),
    ]

    product = models.ForeignKey(InsuranceProduct, on_delete=models.SET_NULL, null=True, blank=True)
    first_name = models.CharField(max_length=80)
    last_name = models.CharField(max_length=80)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    health_status = models.CharField(max_length=20, choices=HEALTH_CHOICES)
    tobacco_use = models.CharField(max_length=10, choices=TOBACCO_CHOICES, default='never')
    coverage_amount = models.DecimalField(max_digits=12, decimal_places=2)
    additional_notes = models.TextField(blank=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_contacted = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.first_name} {self.last_name} — Quote Request ({self.created_at.strftime('%b %d, %Y')})"
