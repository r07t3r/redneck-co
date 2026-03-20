from django.db import models
from django.contrib.auth.models import User


class InvestmentProduct(models.Model):
    RISK_LEVEL_CHOICES = [
        ('conservative', 'Conservative'),
        ('moderate', 'Moderate'),
        ('aggressive', 'Aggressive Growth'),
    ]
    PRODUCT_TYPE_CHOICES = [
        ('mutual_fund', 'Mutual Fund'),
        ('etf', 'ETF Portfolio'),
        ('retirement', 'Retirement Account (IRA/401k)'),
        ('annuity', 'Fixed Annuity'),
        ('bonds', 'Bond Portfolio'),
        ('stocks', 'Equity Portfolio'),
        ('real_estate', 'Real Estate Investment'),
        ('managed', 'Managed Portfolio'),
    ]

    name = models.CharField(max_length=150)
    product_type = models.CharField(max_length=30, choices=PRODUCT_TYPE_CHOICES)
    tagline = models.CharField(max_length=200)
    description = models.TextField()
    risk_level = models.CharField(max_length=20, choices=RISK_LEVEL_CHOICES)
    min_investment = models.DecimalField(max_digits=12, decimal_places=2, default=1000)
    expected_return_low = models.DecimalField(max_digits=5, decimal_places=2, help_text='Annual % return (low estimate)')
    expected_return_high = models.DecimalField(max_digits=5, decimal_places=2, help_text='Annual % return (high estimate)')
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


class InvestmentConsultationRequest(models.Model):
    INVESTMENT_GOAL_CHOICES = [
        ('retirement', 'Retirement Planning'),
        ('wealth', 'Wealth Building'),
        ('income', 'Passive Income'),
        ('college', 'College Funding'),
        ('estate', 'Estate Planning'),
        ('other', 'Other'),
    ]
    TIME_HORIZON_CHOICES = [
        ('short', 'Short-term (1–3 years)'),
        ('medium', 'Medium-term (3–10 years)'),
        ('long', 'Long-term (10+ years)'),
    ]

    product = models.ForeignKey(InvestmentProduct, on_delete=models.SET_NULL, null=True, blank=True)
    first_name = models.CharField(max_length=80)
    last_name = models.CharField(max_length=80)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    investment_goal = models.CharField(max_length=20, choices=INVESTMENT_GOAL_CHOICES)
    time_horizon = models.CharField(max_length=10, choices=TIME_HORIZON_CHOICES)
    initial_investment = models.DecimalField(max_digits=12, decimal_places=2)
    risk_tolerance = models.CharField(max_length=20, choices=InvestmentProduct.RISK_LEVEL_CHOICES)
    additional_notes = models.TextField(blank=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_contacted = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.first_name} {self.last_name} — Consultation ({self.created_at.strftime('%b %d, %Y')})"
