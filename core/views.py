from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from .models import ContactInquiry, TeamMember, Testimonial
from .forms import ContactForm
from insurance.models import InsuranceProduct
from investments.models import InvestmentProduct


def home(request):
    testimonials = Testimonial.objects.filter(is_active=True)[:3]
    context = {
        'testimonials': testimonials,
        'page_title': 'Redneck.co — Texas Built. American Strong.',
    }
    return render(request, 'core/home.html', context)


def about(request):
    team = TeamMember.objects.filter(is_active=True)
    context = {
        'team': team,
        'page_title': 'About Us — Redneck.co',
    }
    return render(request, 'core/about.html', context)


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            inquiry = form.save()
            messages.success(request, "Thank you for reaching out. A Redneck.co advisor will contact you within one business day.")
            return redirect('contact')
    else:
        form = ContactForm()

    context = {
        'form': form,
        'page_title': 'Contact Us — Redneck.co',
    }
    return render(request, 'core/contact.html', context)


def dashboard(request):
    if not request.user.is_authenticated:
        return redirect('login')
    context = {
        'page_title': 'My Dashboard — Redneck.co',
    }
    return render(request, 'core/dashboard.html', context)


def services(request):
    insurance_products = InsuranceProduct.objects.filter(is_active=True)
    investment_products = InvestmentProduct.objects.filter(is_active=True)
    context = {
        'insurance_products': insurance_products,
        'investment_products': investment_products,
        'page_title': 'Our Services — Redneck.co',
    }
    return render(request, 'core/services.html', context)
