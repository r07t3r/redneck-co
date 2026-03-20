#!/usr/bin/env bash
# ============================================================
# Redneck.co — Setup Script
# Run this after installing requirements:
#   pip install -r requirements.txt
# ============================================================

set -e

echo "================================================"
echo "  REDNECK.CO — Django Setup"
echo "  Texas Built. American Strong."
echo "================================================"

echo ""
echo "[1/4] Running database migrations..."
python manage.py makemigrations core insurance investments
python manage.py migrate

echo ""
echo "[2/4] Collecting static files..."
python manage.py collectstatic --noinput 2>/dev/null || echo "  (skipped — run after deployment)"

echo ""
echo "[3/4] Loading sample data..."
python manage.py shell << 'EOF'
from core.models import Testimonial, TeamMember
from insurance.models import InsuranceProduct
from investments.models import InvestmentProduct

# --- Testimonials ---
if not Testimonial.objects.exists():
    Testimonial.objects.bulk_create([
        Testimonial(client_name="Robert 'Bobby' Callahan", client_location="San Antonio, TX",
            quote="Redneck.co didn't talk to me like I was a number. They sat down, explained everything clearly, and got me a whole life policy that actually fits my family's budget. Couldn't ask for better.", rating=5),
        Testimonial(client_name="Linda Hargrove", client_location="Houston, TX",
            quote="Rolled over my 401(k) after leaving my corporate job and these folks made it painless. My portfolio has grown 14% this year alone. They're the real deal.", rating=5),
        Testimonial(client_name="Mary Ellen Whitaker", client_location="Lubbock, TX",
            quote="When my husband passed, Redneck.co walked us through the entire claims process. They fought for us like family. I will recommend them to every Texan I know.", rating=5),
    ])
    print("  ✓ Testimonials created")

# --- Insurance Products ---
if not InsuranceProduct.objects.exists():
    InsuranceProduct.objects.bulk_create([
        InsuranceProduct(
            name="Texas Term Shield", product_type="term", order=1,
            tagline="Straightforward protection for the years that matter most",
            description="Pure death benefit protection for a set term — 10, 20, or 30 years. Our most affordable policy designed for working Texas families. Lock in your rate today and your premium will never increase.",
            min_coverage=100000, max_coverage=5000000, min_age=18, max_age=70,
            features="Guaranteed level premiums\nConvertible to permanent coverage\nAccelerated death benefit rider\nNo medical exam options available\nReturn of premium rider available",
            is_featured=True, is_active=True,
        ),
        InsuranceProduct(
            name="Lone Star Whole Life", product_type="whole", order=2,
            tagline="Lifelong protection with built-in cash value",
            description="Permanent coverage that builds tax-deferred cash value over time. A true Texas investment in your family's future. Your policy will be there for you no matter when you need it.",
            min_coverage=50000, max_coverage=2000000, min_age=18, max_age=80,
            features="Guaranteed death benefit\nTax-deferred cash value growth\nPolicy loan availability\nDividend participation eligibility\nGuaranteed insurability rider",
            is_active=True,
        ),
        InsuranceProduct(
            name="Texas Legacy Plan", product_type="final_expense", order=3,
            tagline="Protect your loved ones from end-of-life costs",
            description="Affordable whole life insurance designed for Texans 50–85. No medical exam required. Guaranteed acceptance for qualifying applicants. Give your family the gift of not having to worry.",
            min_coverage=5000, max_coverage=25000, min_age=50, max_age=85,
            features="No medical exam required\nGuaranteed acceptance ages 50–85\nFixed monthly premiums for life\nCovers funeral & burial costs\nImmediate death benefit",
            is_active=True,
        ),
        InsuranceProduct(
            name="Universal Shield Plus", product_type="universal", order=4,
            tagline="Flexible permanent coverage that adapts to your life",
            description="Universal life insurance gives you the flexibility to adjust your premiums and death benefit as your needs change. Perfect for Texans whose lives don't fit a cookie-cutter mold.",
            min_coverage=100000, max_coverage=5000000, min_age=18, max_age=75,
            features="Adjustable premiums and death benefit\nInterest-bearing cash value account\nMinimum guaranteed interest rate\nPartial withdrawal options\nLong-term care rider available",
            is_active=True,
        ),
    ])
    print("  ✓ Insurance products created")

# --- Investment Products ---
if not InvestmentProduct.objects.exists():
    InvestmentProduct.objects.bulk_create([
        InvestmentProduct(
            name="Texas Growth Portfolio", product_type="managed", order=1,
            tagline="Professionally managed, diversified equity growth",
            description="Our flagship managed portfolio allocates across U.S. equities, international stocks, and bonds — rebalanced quarterly by our Texas-based advisors. Built for long-term capital appreciation.",
            risk_level="moderate", min_investment=10000,
            expected_return_low=7.0, expected_return_high=11.0,
            features="Quarterly rebalancing\nTax-loss harvesting\nMonthly performance reports\n0.75% annual management fee\nFiduciary management",
            is_featured=True, is_active=True,
        ),
        InvestmentProduct(
            name="Lone Star Retirement IRA", product_type="retirement", order=2,
            tagline="Tax-advantaged retirement savings for every Texan",
            description="Traditional and Roth IRA options with expert portfolio management. We also handle 401(k) rollovers from former employers with zero transfer fees. Start building your Texas retirement today.",
            risk_level="conservative", min_investment=1000,
            expected_return_low=5.0, expected_return_high=8.0,
            features="Traditional & Roth IRA options\nFree 401(k) rollovers\nTax-deferred compounding\nAnnual contribution optimization\nRequired minimum distribution planning",
            is_active=True,
        ),
        InvestmentProduct(
            name="Texas Income Annuity", product_type="annuity", order=3,
            tagline="Guaranteed income for a secure Texas retirement",
            description="Fixed annuities provide guaranteed income you can't outlive. Ideal for Texans approaching retirement who want certainty over volatility. Sleep well knowing your income is guaranteed.",
            risk_level="conservative", min_investment=25000,
            expected_return_low=4.8, expected_return_high=6.2,
            features="Guaranteed monthly income\nPrincipal protection\nBeneficiary death benefit\nTax-deferred growth phase\nOptional inflation rider",
            is_active=True,
        ),
        InvestmentProduct(
            name="Lone Star ETF Builder", product_type="etf", order=4,
            tagline="Low-cost, diversified index investing for Texans",
            description="A disciplined ETF portfolio strategy built around low-cost index funds. We construct and monitor a diversified portfolio of ETFs tailored to your risk tolerance and time horizon.",
            risk_level="moderate", min_investment=5000,
            expected_return_low=6.5, expected_return_high=10.0,
            features="Ultra-low expense ratios\nAutomatic dividend reinvestment\nAnnual rebalancing\nFactor-based allocation\nEnvironmental & social screening available",
            is_active=True,
        ),
        InvestmentProduct(
            name="Texas Aggressive Growth", product_type="stocks", order=5,
            tagline="Maximum growth potential for long-horizon Texas investors",
            description="An equity-heavy portfolio concentrated in high-growth U.S. and international equities. For Texans with a long time horizon who can stomach short-term volatility for long-term gains.",
            risk_level="aggressive", min_investment=10000,
            expected_return_low=9.0, expected_return_high=15.0,
            features="Growth & momentum equity focus\nSector concentration opportunities\nQuarterly tactical adjustments\nMonthly rebalancing\nDedicated growth advisor",
            is_active=True,
        ),
    ])
    print("  ✓ Investment products created")

print("  ✓ Sample data loaded successfully")
EOF

echo ""
echo "[4/4] Creating superuser..."
echo "  Run: python manage.py createsuperuser"
echo "  (or use: DJANGO_SUPERUSER_PASSWORD=admin python manage.py createsuperuser --noinput --username=admin --email=admin@redneck.co)"

echo ""
echo "================================================"
echo "  SETUP COMPLETE!"
echo ""
echo "  To run the development server:"
echo "    python manage.py runserver"
echo ""
echo "  Visit:"
echo "    http://127.0.0.1:8000/         → Homepage"
echo "    http://127.0.0.1:8000/admin/   → Admin Panel"
echo "    http://127.0.0.1:8000/insurance/  → Life Insurance"
echo "    http://127.0.0.1:8000/investments/ → Investments"
echo "================================================"
