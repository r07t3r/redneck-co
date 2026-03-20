from django.db import models
from django.contrib.auth.models import User


class ContactInquiry(models.Model):
    SUBJECT_CHOICES = [
        ('life_insurance', 'Life Insurance'),
        ('investments', 'Investment Services'),
        ('retirement', 'Retirement Planning'),
        ('estate', 'Estate Planning'),
        ('general', 'General Inquiry'),
    ]

    name = models.CharField(max_length=150)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True)
    subject = models.CharField(max_length=50, choices=SUBJECT_CHOICES, default='general')
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Contact Inquiry'
        verbose_name_plural = 'Contact Inquiries'

    def __str__(self):
        return f"{self.name} — {self.get_subject_display()} ({self.created_at.strftime('%b %d, %Y')})"


class TeamMember(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    bio = models.TextField()
    photo = models.ImageField(upload_to='team/', blank=True, null=True)
    linkedin_url = models.URLField(blank=True)
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['order', 'name']

    def __str__(self):
        return f"{self.name} — {self.title}"


class Testimonial(models.Model):
    client_name = models.CharField(max_length=100)
    client_location = models.CharField(max_length=100, default='Texas')
    quote = models.TextField()
    rating = models.PositiveSmallIntegerField(default=5)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.client_name} — {self.client_location}"
