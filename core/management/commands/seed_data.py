"""
Management command: python manage.py seed_data

Seeds the database with default insurance products, investment products,
testimonials, and team members. Safe to run multiple times (idempotent).
"""
from django.core.management.base import BaseCommand
from core.models import Testimonial, TeamMember
from insurance.models import InsuranceProduct
from investments.models import InvestmentProduct


class Command(BaseCommand):
    help = 'Seed the database with default Redneck.co sample data'

    def add_arguments(self, parser):
        parser.add_argument(
            '--force',
            action='store_true',
            help='Delete existing data and re-seed from scratch',
        )

    def handle(self, *args, **options):
        force = options['force']
        self.stdout.write(self.style.SUCCESS('🤠 Seeding Redneck.co database...\n'))

        # ── Testimonials ──────────────────────────────────────────────────────
        if force:
            Testimonial.objects.all().delete()

        if not Testimonial.objects.exists():
            Testimonial.objects.bulk_create([
                Testimonial(
                    client_name="Robert 'Bobby' Callahan",
                    client_location="San Antonio, TX",
                    quote="Redneck.co didn't talk to me like I was a number. They sat down, explained everything clearly, and got me a whole life policy that actually fits my family's budget. Couldn't ask for better.",
                    rating=5, is_active=True,
                ),
                Testimonial(
                    client_name="Linda Hargrove",
                    client_location="Houston, TX",
                    quote="Rolled over my 401(k) after leaving my corporate job and these folks made it painless. My portfolio has grown significantly this year. They're the real deal.",
                    rating=5, is_active=True,
                ),
                Testimonial(
                    client_name="Mary Ellen Whitaker",
                    client_location="Lubbock, TX",
                    quote="When my husband passed, Redneck.co walked us through the entire claims process. They fought for us like family. I will recommend them to every Texan I know.",
                    rating=5, is_active=True,
                ),
            ])
            self.stdout.write(self.style.SUCCESS('  ✓ Testimonials created'))
        else:
            self.stdout.write('  · Testimonials already exist — skipping')

        # ── Team Members ──────────────────────────────────────────────────────
        if force:
            TeamMember.objects.all().delete()

        if not TeamMember.objects.exists():
            TeamMember.objects.bulk_create([
                TeamMember(name="Clay 'Buck' Harmon", title="Founder & CEO", order=1, is_active=True,
                    bio="A fourth-generation Texan from Abilene, Buck founded Redneck.co after 15 years at a national insurance firm. He saw too many Texans paying too much for too little. He fixed that."),
                TeamMember(name="Sandra 'Sandy' Reeves", title="VP, Life Insurance", order=2, is_active=True,
                    bio="With 20 years in life insurance underwriting, Sandy knows every clause, rider, and exclusion in the business. She makes sure every Redneck.co client gets maximum value for their dollar."),
                TeamMember(name="Dale Hutchinson, CFA", title="Chief Investment Officer", order=3, is_active=True,
                    bio="Dale's managed Texas family portfolios through three recessions and came out ahead every time. His disciplined, long-horizon approach has earned Redneck.co its investment reputation."),
                TeamMember(name="Rosa Martinez", title="Senior Financial Advisor", order=4, is_active=True,
                    bio="Raised in San Antonio, Rosa is bilingual and serves Texas's growing Hispanic community with the same no-nonsense advice that defines Redneck.co."),
                TeamMember(name="Travis 'Trav' Coleman", title="Retirement Specialist", order=5, is_active=True,
                    bio="Trav spent 10 years as a ranch hand before getting his CFP. He understands what retirement means for a working Texan — and he builds plans that respect that reality."),
                TeamMember(name="Janet Olusegun", title="Estate Planning Advisor", order=6, is_active=True,
                    bio="Janet is a former estate attorney turned advisor. She helps Texas families navigate the complex intersection of insurance, investments, and generational wealth transfer."),
            ])
            self.stdout.write(self.style.SUCCESS('  ✓ Team members created'))
        else:
            self.stdout.write('  · Team members already exist — skipping')

        # ── Insurance Products ─────────────────────────────────────────────────
        if force:
            InsuranceProduct.objects.all().delete()

        if not InsuranceProduct.objects.exists():
            InsuranceProduct.objects.bulk_create([
                InsuranceProduct(
                    name="Texas Term Shield", product_type="term", order=1,
                    tagline="Straightforward protection for the years that matter most",
                    description="Pure death benefit protection for a set term — 10, 20, or 30 years. Our most affordable policy designed for working Texas families. Lock in your rate today and your premium will never increase for the length of your term.",
                    min_coverage=100000, max_coverage=5000000, min_age=18, max_age=70,
                    features="Guaranteed level premiums\nConvertible to permanent coverage\nAccelerated death benefit rider\nNo medical exam options available\nReturn of premium rider available",
                    is_featured=True, is_active=True,
                ),
                InsuranceProduct(
                    name="Lone Star Whole Life", product_type="whole", order=2,
                    tagline="Lifelong protection with built-in cash value",
                    description="Permanent coverage that builds tax-deferred cash value over time. A true Texas investment in your family's future. Your policy will be there for you no matter when you need it — and it builds real wealth along the way.",
                    min_coverage=50000, max_coverage=2000000, min_age=18, max_age=80,
                    features="Guaranteed death benefit\nTax-deferred cash value growth\nPolicy loan availability\nDividend participation eligibility\nGuaranteed insurability rider",
                    is_active=True,
                ),
                InsuranceProduct(
                    name="Texas Legacy Plan", product_type="final_expense", order=3,
                    tagline="Protect your loved ones from end-of-life costs",
                    description="Affordable whole life insurance designed for Texans 50–85. No medical exam required. Guaranteed acceptance for qualifying applicants. Give your family the gift of financial peace when they need it most.",
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
            self.stdout.write(self.style.SUCCESS('  ✓ Insurance products created'))
        else:
            self.stdout.write('  · Insurance products already exist — skipping')

        # ── Investment Products ────────────────────────────────────────────────
        if force:
            InvestmentProduct.objects.all().delete()

        if not InvestmentProduct.objects.exists():
            InvestmentProduct.objects.bulk_create([
                InvestmentProduct(
                    name="Texas Growth Portfolio", product_type="managed", order=1,
                    tagline="Professionally managed, diversified equity growth",
                    description="Our flagship managed portfolio allocates across U.S. equities, international stocks, and bonds — rebalanced quarterly by our Texas-based advisors. Built for long-term capital appreciation with active risk management.",
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
                    description="Fixed annuities provide guaranteed income you can't outlive. Ideal for Texans approaching retirement who want certainty over volatility. Sleep well knowing your income is locked in.",
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
                    features="Ultra-low expense ratios\nAutomatic dividend reinvestment\nAnnual rebalancing\nFactor-based allocation\nESG screening available",
                    is_active=True,
                ),
                InvestmentProduct(
                    name="Texas Aggressive Growth", product_type="stocks", order=5,
                    tagline="Maximum growth potential for long-horizon Texas investors",
                    description="An equity-heavy portfolio concentrated in high-growth U.S. and international equities. For Texans with a long time horizon who can stomach short-term volatility for long-term gains.",
                    risk_level="aggressive", min_investment=10000,
                    expected_return_low=9.0, expected_return_high=15.0,
                    features="Growth & momentum equity focus\nSector concentration opportunities\nMonthly rebalancing\nDedicated growth advisor\nQuarterly strategy calls",
                    is_active=True,
                ),
            ])
            self.stdout.write(self.style.SUCCESS('  ✓ Investment products created'))
        else:
            self.stdout.write('  · Investment products already exist — skipping')

        self.stdout.write('')
        self.stdout.write(self.style.SUCCESS('🦅 Seed complete! Redneck.co is ready to roll.'))
