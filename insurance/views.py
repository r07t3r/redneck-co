from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import InsuranceProduct, InsuranceQuoteRequest
from .forms import InsuranceQuoteForm


def insurance_home(request):
    products = InsuranceProduct.objects.filter(is_active=True)
    featured = products.filter(is_featured=True)
    context = {
        'products': products,
        'featured': featured,
        'page_title': 'Life Insurance — Redneck.co',
    }
    return render(request, 'insurance/insurance_home.html', context)


def insurance_detail(request, pk):
    product = get_object_or_404(InsuranceProduct, pk=pk, is_active=True)
    context = {
        'product': product,
        'page_title': f'{product.name} — Redneck.co',
    }
    return render(request, 'insurance/insurance_detail.html', context)


def quote_request(request, pk=None):
    product = None
    if pk:
        product = get_object_or_404(InsuranceProduct, pk=pk, is_active=True)

    if request.method == 'POST':
        form = InsuranceQuoteForm(request.POST)
        if form.is_valid():
            quote = form.save(commit=False)
            if product:
                quote.product = product
            if request.user.is_authenticated:
                quote.user = request.user
            quote.save()
            messages.success(request, "Your quote request has been submitted. A Redneck.co advisor will be in touch shortly.")
            return redirect('insurance_home')
    else:
        form = InsuranceQuoteForm()

    context = {
        'form': form,
        'product': product,
        'page_title': 'Request a Quote — Redneck.co',
    }
    return render(request, 'insurance/quote_request.html', context)
