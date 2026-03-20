# 🦅 Redneck.co — Django Investment & Insurance Platform

**Texas Built. American Strong.**

A full-stack Django website for Redneck.co — a Texas-based life insurance and investment services firm headquartered in Austin, TX. Built with an Avant Hall-inspired minimalist design using American Navy, Red, and Gold colors with an eagle motif.

---

## 📋 Project Overview

| Feature | Details |
|---|---|
| **Framework** | Django 4.2+ |
| **Database** | SQLite (dev) / PostgreSQL (prod) |
| **Design** | Avant Hall-inspired, American minimalism |
| **Colors** | Navy `#0A1628`, Red `#B22234`, Gold `#C9A84C` |
| **Fonts** | Playfair Display (serif) + Barlow (sans) |
| **Location** | Austin, Texas |

---

## 🗂️ Project Structure

```
redneck_co/
├── redneck/               # Django project config
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── core/                  # Main app: homepage, about, contact, dashboard
│   ├── models.py          # ContactInquiry, TeamMember, Testimonial
│   ├── views.py
│   ├── forms.py
│   ├── urls.py
│   └── templates/core/
│       ├── home.html
│       ├── about.html
│       ├── contact.html
│       ├── services.html
│       └── dashboard.html
│
├── insurance/             # Life insurance app
│   ├── models.py          # InsuranceProduct, InsuranceQuoteRequest
│   ├── views.py
│   ├── forms.py
│   ├── urls.py
│   └── templates/insurance/
│       ├── insurance_home.html
│       ├── insurance_detail.html
│       └── quote_request.html
│
├── investments/           # Investment services app
│   ├── models.py          # InvestmentProduct, InvestmentConsultationRequest
│   ├── views.py
│   ├── forms.py
│   ├── urls.py
│   └── templates/investments/
│       ├── investments_home.html
│       ├── investment_detail.html
│       └── consultation_request.html
│
├── templates/             # Global templates
│   ├── base.html          # Master layout with navbar + footer
│   └── registration/
│       └── login.html
│
├── static/
│   ├── css/main.css       # Full stylesheet (1000+ lines)
│   └── js/main.js         # Interactive JS
│
├── requirements.txt
├── manage.py
└── setup.sh               # Quick setup script
```

---

## 🚀 Quick Start

### 1. Install Requirements

```bash
pip install -r requirements.txt
```

### 2. Run Setup Script

```bash
chmod +x setup.sh
./setup.sh
```

This will:
- Run all Django migrations
- Load sample insurance & investment products
- Load testimonials & team members

### 3. Create Admin User

```bash
python manage.py createsuperuser
```

### 4. Start Development Server

```bash
python manage.py runserver
```

Visit **http://127.0.0.1:8000** — you're live!

---

## 🌐 Pages & URLs

| URL | Page |
|---|---|
| `/` | Homepage (Hero, Services, Stats, Testimonials, CTA) |
| `/about/` | About Us (Mission, Team, Stats) |
| `/services/` | All Services Overview |
| `/contact/` | Contact Form + Office Info |
| `/dashboard/` | Authenticated User Dashboard |
| `/insurance/` | Life Insurance Products |
| `/insurance/<id>/` | Insurance Product Detail |
| `/insurance/quote/` | Quote Request Form |
| `/insurance/quote/<id>/` | Quote for Specific Product |
| `/investments/` | Investment Products |
| `/investments/<id>/` | Investment Product Detail |
| `/investments/consult/` | Consultation Request |
| `/investments/consult/<id>/` | Consult for Specific Product |
| `/auth/login/` | Login |
| `/auth/logout/` | Logout |
| `/admin/` | Django Admin Panel |

---

## 🗃️ Database Models

### Core App

**ContactInquiry**
- `name`, `email`, `phone`
- `subject` (Life Insurance, Investments, Retirement, Estate, General)
- `message`, `created_at`, `is_read`

**TeamMember**
- `name`, `title`, `bio`, `photo`
- `linkedin_url`, `order`, `is_active`

**Testimonial**
- `client_name`, `client_location`
- `quote`, `rating`, `is_active`

### Insurance App

**InsuranceProduct**
- `name`, `product_type` (term/whole/universal/variable/final_expense)
- `tagline`, `description`, `features` (newline-separated)
- `min_coverage`, `max_coverage`, `min_age`, `max_age`
- `is_active`, `is_featured`, `order`

**InsuranceQuoteRequest**
- `first_name`, `last_name`, `email`, `phone`
- `date_of_birth`, `gender`, `health_status`, `tobacco_use`
- `coverage_amount`, `additional_notes`
- `product` (FK), `user` (FK), `is_contacted`

### Investments App

**InvestmentProduct**
- `name`, `product_type`, `risk_level` (conservative/moderate/aggressive)
- `tagline`, `description`, `features`
- `min_investment`, `expected_return_low`, `expected_return_high`
- `is_active`, `is_featured`, `order`

**InvestmentConsultationRequest**
- `first_name`, `last_name`, `email`, `phone`
- `investment_goal`, `time_horizon`, `initial_investment`, `risk_tolerance`
- `additional_notes`, `product` (FK), `user` (FK), `is_contacted`

---

## 🎨 Design System

### Color Palette

```css
--navy:      #0A1628   /* Primary dark background */
--navy-mid:  #112240   /* Card backgrounds */
--red:       #B22234   /* American flag red — CTAs, accents */
--gold:      #C9A84C   /* American eagle gold — highlights */
--white:     #F9F7F2   /* Warm white */
--off-white: #EDE9E0   /* Subtle section backgrounds */
```

### Typography

- **Display/Headings:** Playfair Display (Google Fonts)
- **Body:** Barlow (Google Fonts)
- **Labels/Nav:** Barlow Condensed (Google Fonts)

### Key CSS Classes

```css
.btn-primary   /* Red CTA button */
.btn-gold      /* Gold accent button */
.btn-outline   /* Ghost button */
.btn-navy      /* Dark navy button */

.section-label /* Uppercase eyebrow label with line */
.divider       /* Red-to-gold gradient horizontal rule */

.card          /* Light card with hover shadow */
.card--dark    /* Navy dark card */

.product-card  /* Insurance/investment product card */
.risk-badge    /* Conservative/Moderate/Aggressive pill */

.reveal        /* Scroll-triggered fade-up animation */
.animate-fadeup /* One-time entrance animation */
```

---

## ⚙️ Configuration

### Email (settings.py)

For production, replace the console email backend:

```python
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.yourmailserver.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'hello@redneck.co'
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_PASSWORD')
```

### Production Deployment

1. Set `DEBUG = False`
2. Set `SECRET_KEY` from environment variable
3. Configure `ALLOWED_HOSTS`
4. Switch to PostgreSQL
5. Add `whitenoise` to middleware for static files
6. Use `gunicorn redneck.wsgi` as your WSGI server

---

## 🛡️ Admin Panel

Access at `/admin/` with your superuser credentials.

**Manage from admin:**
- View and respond to Contact Inquiries
- Mark Insurance Quote Requests as contacted
- Mark Investment Consultation Requests as contacted
- Add/edit Team Members
- Add/edit Testimonials
- Add/edit Insurance Products
- Add/edit Investment Products

---

## 📜 License & Compliance

- Licensed insurance content includes appropriate disclosures
- FINRA/SIPC compliance language included in footer and forms
- Texas Department of Insurance licensing badge displayed
- Investment risk disclosures included on all investment pages

---

*Built with Texas pride. 🤠🦅*
