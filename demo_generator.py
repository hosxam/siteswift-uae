"""
SiteSwift UAE - Demo Site Generator
------------------------------------
Creates stunning, industry-specific demo websites for potential clients.
Generate a full, brandable landing page for any business type.
No external dependencies needed — outputs clean HTML.

Usage:
  python demo_generator.py
  python demo_generator.py --business "Elite Physio Center" --industry physiotherapy --output my-site.html

Industries supported: clinic, gym, cafe, salon, dental, physio, realestate, auto, spa, general
"""

import os
import argparse
from datetime import datetime

BUSINESS_NAME = "SiteSwift UAE"
CONTACT_EMAIL = "hossam.hassan20@outlook.com"
WHATSAPP = "971502495662"

# ============================================================
# INDUSTRY-SPECIFIC CONTENT
# ============================================================

INDUSTRY_DATA = {
    "clinic": {
        "tagline": "Your Health, Our Priority",
        "hero_subtitle": "Modern healthcare with a personal touch. Book your appointment online.",
        "features": ["Consult with experienced doctors", "State-of-the-art diagnostic equipment", "Same-day appointments available"],
        "color_scheme": ("#0284c7", "#0ea5e9"),  # Blue
        "icon": "🏥",
        "cta_text": "Book an Appointment",
        "competitor_example": "Dubai London Clinic — they have a website. Do you?",
    },
    "dental": {
        "tagline": "Your Smile, Our Mission",
        "hero_subtitle": "Advanced dental care in a comfortable environment. Book your checkup today.",
        "features": ["Teeth whitening & cosmetic dentistry", "Pain-free treatments", "Emergency dental care available"],
        "color_scheme": ("#0891b2", "#06b6d4"),  # Cyan
        "icon": "🦷",
        "cta_text": "Book a Checkup",
        "competitor_example": "Dubai Marina Dental Clinic — already online. Are you?",
    },
    "gym": {
        "tagline": "Transform Your Body, Transform Your Life",
        "hero_subtitle": "State-of-the-art equipment, expert trainers, and a motivating community.",
        "features": ["Personal training programs", "Group fitness classes (HIIT, Yoga, Pilates)", "Nutrition planning included"],
        "color_scheme": ("#dc2626", "#ef4444"),  # Red
        "icon": "💪",
        "cta_text": "Start Your Free Trial",
        "competitor_example": "Warehouse Gym — their site gets them 50+ leads a week. Yours could too.",
    },
    "cafe": {
        "tagline": "Good Vibes, Great Coffee",
        "hero_subtitle": "The neighborhood spot for fresh brews, delicious bites, and warm conversations.",
        "features": ["Specialty coffee & artisan drinks", "Freshly baked goods daily", "Free WiFi & cozy seating area"],
        "color_scheme": ("#a16207", "#eab308"),  # Amber/Gold
        "icon": "☕",
        "cta_text": "View Our Menu",
        "competitor_example": "% competition has a sleek online menu. Customers choose based on what they see online.",
    },
    "salon": {
        "tagline": "Look Your Best, Feel Your Best",
        "hero_subtitle": "Premium beauty services tailored to you. Book your appointment online.",
        "features": ["Expert stylists & colorists", "Nail art & spa treatments", "Bridal & event packages"],
        "color_scheme": ("#c026d3", "#d946ef"),  # Purple/Pink
        "icon": "💇",
        "cta_text": "Book Your Appointment",
        "competitor_example": "Chit Chat Salon in JLT has a full booking site. Don't lose customers to them.",
    },
    "physio": {
        "tagline": "Move Better, Live Better",
        "hero_subtitle": "Expert physiotherapy to get you back to what you love, pain-free.",
        "features": ["Sports injury rehabilitation", "Post-surgery recovery programs", "Manual therapy & dry needling"],
        "color_scheme": ("#059669", "#10b981"),  # Green
        "icon": "🦵",
        "cta_text": "Book a Consultation",
        "competitor_example": "Elite Physio Center has a professional site. Patients trust clinics they can research online.",
    },
    "auto": {
        "tagline": "Your Car Deserves the Best",
        "hero_subtitle": "Expert auto repair and maintenance with transparent pricing and fast turnaround.",
        "features": ["Diagnostics & engine repair", "AC service & electrical work", "Genuine parts & warranty"],
        "color_scheme": ("#1e40af", "#3b82f6"),  # Dark Blue
        "icon": "🔧",
        "cta_text": "Book a Service",
        "competitor_example": "AutoPro Dubai has an online booking system. Every day without one costs you customers.",
    },
    "spa": {
        "tagline": "Escape, Relax, Recharge",
        "hero_subtitle": "Luxury spa treatments in the heart of Dubai. Your oasis awaits.",
        "features": ["Massage therapy & body treatments", "Facials & skin care", "Couples packages available"],
        "color_scheme": ("#a21caf", "#d946ef"),  # Magenta
        "icon": "🧖",
        "cta_text": "Book a Treatment",
        "competitor_example": "",
    },
    "realestate": {
        "tagline": "Find Your Dream Property",
        "hero_subtitle": "Expert real estate agents helping you buy, sell, and rent in Dubai.",
        "features": ["Property listings with virtual tours", "Free market valuation", "Tenant & landlord services"],
        "color_scheme": ("#1d4ed8", "#2563eb"),  # Blue
        "icon": "🏠",
        "cta_text": "Browse Properties",
        "competitor_example": "",
    },
    "general": {
        "tagline": "Your Business, Online",
        "hero_subtitle": "A professional website for your business. Get found, get booked, get growing.",
        "features": ["Custom design for your brand", "Mobile-friendly & fast loading", "SEO optimized for local search"],
        "color_scheme": ("#2563eb", "#3b82f6"),
        "icon": "✨",
        "cta_text": "Get Your Website",
        "competitor_example": "",
    },
}

TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{business_name} — {tagline}</title>
    <style>
        * {{ margin: 0; padding: 0; box-sizing: border-box; }}
        
        body {{
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            line-height: 1.6;
            color: #1f2937;
        }}

        .hero {{
            background: linear-gradient(135deg, {color1}, {color2});
            color: white;
            padding: 80px 20px;
            text-align: center;
        }}

        .hero h1 {{ font-size: 3rem; margin-bottom: 10px; }}
        .hero .icon {{ font-size: 4rem; margin-bottom: 20px; }}
        .hero p {{ font-size: 1.2rem; max-width: 600px; margin: 0 auto 30px; opacity: 0.9; }}

        .cta-button {{
            display: inline-block;
            background: white;
            color: {color1};
            padding: 16px 40px;
            border-radius: 50px;
            font-size: 1.1rem;
            font-weight: 600;
            text-decoration: none;
            transition: transform 0.2s;
        }}

        .cta-button:hover {{ transform: translateY(-2px); box-shadow: 0 10px 25px rgba(0,0,0,0.15); }}

        .section {{
            padding: 80px 20px;
            max-width: 1200px;
            margin: 0 auto;
        }}

        .section h2 {{
            font-size: 2rem;
            margin-bottom: 40px;
            text-align: center;
        }}

        .features {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 30px;
            margin-top: 40px;
        }}

        .feature-card {{
            background: #f9fafb;
            padding: 30px;
            border-radius: 12px;
            text-align: center;
            border: 1px solid #e5e7eb;
        }}

        .feature-card h3 {{ margin-bottom: 10px; color: {color1}; }}

        .about {{
            background: #f3f4f6;
        }}

        .about-content {{
            max-width: 800px;
            margin: 0 auto;
            text-align: center;
        }}

        .contact {{
            text-align: center;
        }}

        .contact-info p {{ margin: 10px 0; font-size: 1.1rem; }}

        .footer {{
            background: #1f2937;
            color: white;
            text-align: center;
            padding: 30px;
            font-size: 0.9rem;
        }}

        .footer a {{ color: #93c5fd; text-decoration: none; }}

        @media (max-width: 768px) {{
            .hero h1 {{ font-size: 2rem; }}
            .hero p {{ font-size: 1rem; }}
            .features {{ grid-template-columns: 1fr; }}
        }}
    </style>
</head>
<body>
    <section class="hero">
        <div class="icon">{icon}</div>
        <h1>{business_name}</h1>
        <p>{tagline}</p>
        <p>{hero_subtitle}</p>
        <a href="wa.me/{whatsapp}" class="cta-button">{cta_text}</a>
    </section>

    <section class="section features-section">
        <h2>Why Choose {business_name}?</h2>
        <div class="features">
{feature_cards}
        </div>
    </section>

    <section class="section about">
        <h2>About {business_name}</h2>
        <div class="about-content">
            <p>We are a local Dubai business serving the {industry} community with dedication and quality. Our team believes in providing exceptional service that keeps our customers coming back.</p>
            {competitor_hook}
        </div>
    </section>

    <section class="section contact">
        <h2>Get in Touch</h2>
        <div class="contact-info">
            <p>📍 Dubai, UAE</p>
            <p>📞 <a href="tel:{whatsapp}" style="color: {color1};">{whatsapp}</a></p>
            <p>✉️ <a href="mailto:{email}" style="color: {color1};">{email}</a></p>
        </div>
        <br>
        <a href="wa.me/{whatsapp}" class="cta-button" style="background: {color1}; color: white;">{cta_text}</a>
    </section>

    <footer class="footer">
        <p>&copy; {year} {business_name}. All rights reserved.</p>
        <p style="margin-top: 5px;">Website by <a href="#">{agency_name}</a></p>
    </footer>
</body>
</html>"""


def generate_demo(business_name: str, industry: str = "general", output: str = None) -> str:
    """
    Generate a complete demo website HTML for a business.
    
    Args:
        business_name: The client's business name
        industry: Industry type (see INDUSTRY_DATA keys)
        output: Output file path. If None, returns the HTML string.
    
    Returns:
        The generated HTML as a string.
    """
    industry = industry.lower()
    if industry not in INDUSTRY_DATA:
        print(f"⚠️  Unknown industry '{industry}'. Using 'general' template.")
        print(f"   Available: {', '.join(INDUSTRY_DATA.keys())}")
        industry = "general"

    data = INDUSTRY_DATA[industry]
    color1, color2 = data["color_scheme"]

    # Build feature cards
    feature_cards = ""
    for feature in data["features"]:
        feature_cards += f'            <div class="feature-card"><h3>✨ {feature}</h3><p>We deliver this with excellence and care.</p></div>\n'

    # Competitor hook
    competitor_hook = ""
    if data.get("competitor_example"):
        competitor_hook = f'\n            <p style="margin-top: 20px; font-style: italic; color: #666;">💡 Did you know? {data["competitor_example"]}</p>'

    html = TEMPLATE.format(
        business_name=business_name,
        tagline=data["tagline"],
        hero_subtitle=data["hero_subtitle"],
        color1=color1,
        color2=color2,
        icon=data["icon"],
        cta_text=data["cta_text"],
        feature_cards=feature_cards,
        competitor_hook=competitor_hook,
        industry=industry,
        whatsapp=WHATSAPP,
        email=CONTACT_EMAIL,
        year=datetime.now().year,
        agency_name=BUSINESS_NAME,
    )

    if output:
        os.makedirs(os.path.dirname(output) or ".", exist_ok=True)
        with open(output, "w", encoding="utf-8") as f:
            f.write(html)
        print(f"✅ Demo generated: {output}")

    return html


def batch_generate():
    """Generate demos for all sample leads in the CSV database."""
    csv_path = os.path.join(os.path.dirname(__file__), "lead-database-template.csv")
    output_dir = os.path.join(os.path.dirname(__file__), "demo-sites")
    os.makedirs(output_dir, exist_ok=True)

    industry_map = {
        "fitness": "gym",
        "salon": "salon",
        "cafe": "cafe",
        "dental": "dental",
        "physio": "physio",
        "medical": "clinic",
        "restaurant": "cafe",
        "beauty": "salon",
    }

    generated = 0
    try:
        import csv
        with open(csv_path, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                name = row.get("company_name", "").strip()
                ind = row.get("industry", "general").lower()
                if not name:
                    continue
                mapped_ind = industry_map.get(ind, "general")
                safe_name = name.replace(" ", "-").replace("&", "and").replace("/", "-").lower()[:40]
                output = os.path.join(output_dir, f"{safe_name}.html")
                generate_demo(name, mapped_ind, output)
                generated += 1
    except FileNotFoundError:
        print(f"⚠️  No CSV found at {csv_path}. Generating sample demo instead.")
        generate_demo("Your Business Name", "general", os.path.join(output_dir, "sample.html"))
        generated = 1

    print(f"\n✅ Generated {generated} demo sites in: {output_dir}")
    print(f"   Open any .html file in your browser to preview.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="SiteSwift Demo Generator")
    parser.add_argument("--business", help="Business name for the demo")
    parser.add_argument("--industry", choices=list(INDUSTRY_DATA.keys()), default="general", help="Industry type")
    parser.add_argument("--output", help="Output file path")
    parser.add_argument("--batch", action="store_true", help="Generate for all leads in CSV")
    
    args = parser.parse_args()

    if args.batch:
        batch_generate()
    elif args.business:
        output = args.output or f"demo-{args.business.replace(' ', '-').lower()}.html"
        generate_demo(args.business, args.industry, output)
    else:
        # Interactive mode
        print("=" * 50)
        print("SiteSwift UAE - Demo Site Generator")
        print("=" * 50)
        name = input("Business name: ").strip()
        print("Industries:", ", ".join(INDUSTRY_DATA.keys()))
        ind = input(f"Industry (general): ").strip() or "general"
        generate_demo(name, ind, f"demo-{name.replace(' ', '-').lower()}.html")
