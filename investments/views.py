from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import InvestmentProduct, InvestmentConsultationRequest
from .forms import InvestmentConsultationForm


def investments_home(request):
    products = InvestmentProduct.objects.filter(is_active=True)
    featured = products.filter(is_featured=True)
    context = {
        'products': products,
        'featured': featured,
        'page_title': 'Investment Services — Redneck.co',
    }
    return render(request, 'investments/investments_home.html', context)


def investment_detail(request, pk):
    product = get_object_or_404(InvestmentProduct, pk=pk, is_active=True)
    context = {
        'product': product,
        'page_title': f'{product.name} — Redneck.co',
    }
    return render(request, 'investments/investment_detail.html', context)


def consultation_request(request, pk=None):
    product = None
    if pk:
        product = get_object_or_404(InvestmentProduct, pk=pk, is_active=True)

    if request.method == 'POST':
        form = InvestmentConsultationForm(request.POST)
        if form.is_valid():
            consultation = form.save(commit=False)
            if product:
                consultation.product = product
            if request.user.is_authenticated:
                consultation.user = request.user
            consultation.save()
            messages.success(request, "Your consultation request has been received. A Redneck.co advisor will reach out within one business day.")
            return redirect('investments_home')
    else:
        form = InvestmentConsultationForm()

    context = {
        'form': form,
        'product': product,
        'page_title': 'Request a Consultation — Redneck.co',
    }
    return render(request, 'investments/consultation_request.html', context)
