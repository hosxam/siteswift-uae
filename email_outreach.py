"""
SiteSwift UAE - Email Outreach Automation
-----------------------------------------
Sends personalized outreach emails using Brevo (Sendinblue) API.
Uses free tier: 300 emails/day.

Setup:
  1. Create Brevo account at https://www.brevo.com/
  2. Get API key from Settings > API Keys
  3. Set BREVO_API_KEY in .env
  4. Run: python email_outreach.py
"""

import os
import csv
import json
import time
import requests
import random
from datetime import datetime
from typing import Optional

try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass

BREVO_API_KEY = os.getenv("BREVO_API_KEY", "")
SENDER_EMAIL = os.getenv("OUTREACH_EMAIL", "hossam.hassan20@outlook.com")
SENDER_NAME = os.getenv("BUSINESS_NAME", "Hossam | SiteSwift UAE")

LEADS_FILE = os.path.join(os.path.dirname(__file__), "lead-database-template.csv")
HISTORY_FILE = os.path.join(os.path.dirname(__file__), "email_sent_history.csv")

# ============================================================
# EMAIL TEMPLATES
# ============================================================

TEMPLATES = {
    "cold_outreach": {
        "subject": "A quick website idea for {company_name}",
        "html": """<!DOCTYPE html>
<html>
<body style="font-family: Arial, sans-serif; max-width: 600px; margin: 0 auto; padding: 20px; line-height: 1.6;">
    <p>Hi {contact_name or 'there'},</p>
    
    <p>I was looking at {company_name} on Google Maps and noticed you don't have a website yet. In Dubai, that means you're probably losing customers who search online first — and these days, that's most of them.</p>
    
    <p>I build simple, professional websites for Dubai businesses starting at AED 499/month. <strong>Everything included</strong> — design, hosting, domain, SEO, and a contact form so customers can find and reach you.</p>
    
    <p>Here's what other businesses say:</p>
    <blockquote style="border-left: 3px solid #2563eb; padding-left: 15px; margin: 15px 0; color: #666;">
        "We started getting booking requests through the website within the first week. Best investment we've made." — <em>Small Business Client, Dubai</em>
    </blockquote>
    
    <p>Want to see what it would look like? I can put together a quick demo for {company_name} at no cost — no commitment.</p>
    
    <p>Let me know if you're open to a 5-minute chat this week.</p>
    
    <p>Best regards,<br>
    {sender_name}<br>
    {sender_email}</p>
    
    <hr style="border: none; border-top: 1px solid #eee;">
    <p style="font-size: 12px; color: #999;">
        You're receiving this because {company_name} appeared in Dubai-area business listings.
        If you're not the right person to talk to, I'd appreciate it if you could point me to the owner.
    </p>
</body>
</html>""",
    },
    "follow_up_day3": {
        "subject": "Re: Quick website idea for {company_name}",
        "html": """<!DOCTYPE html>
<html>
<body style="font-family: Arial, sans-serif; max-width: 600px; margin: 0 auto; padding: 20px; line-height: 1.6;">
    <p>Hi {contact_name or 'there'},</p>
    
    <p>Following up on my earlier message — I know you're busy running {company_name}.</p>
    
    <p>Quick question: How do new customers usually find you right now?</p>
    
    <ul>
        <li><strong>Word of mouth?</strong> Great, but not enough to grow.</li>
        <li><strong>Google Maps?</strong> A website makes you show up way higher.</li>
        <li><strong>Instagram?</strong> A site is where serious customers go to decide.</li>
    </ul>
    
    <p>I'm offering a free demo site for {company_name} — I'll build a sample page showing exactly how your business would look online. It takes me about 2 hours, and if you don't like it, no charge, no obligation.</p>
    
    <p>Worth a try?</p>
    
    <p>Best,<br>
    {sender_name}</p>
</body>
</html>""",
    },
    "value_add": {
        "subject": "We just launched {company_name}'s competitor online 🚀",
        "html": """<!DOCTYPE html>
<html>
<body style="font-family: Arial, sans-serif; max-width: 600px; margin: 0 auto; padding: 20px; line-height: 1.6;">
    <p>Hi {contact_name or 'there'},</p>
    
    <p>I thought you should know — we just launched a website for a {industry_lower} in your area. They're now showing up on Google when people search for "{industry_lower} Dubai".</p>
    
    <p>Meanwhile, {company_name} doesn't have a web presence yet. Every day without one means potential customers are finding your competitors instead.</p>
    
    <p>Don't lose ground. I can get {company_name} online before the end of the week. Monthly pricing starts at AED 499.</p>
    
    <p>Want me to put something together this afternoon?</p>
    
    <p>Best,<br>
    {sender_name}</p>
</body>
</html>""",
    },
}


def send_brevo_email(to_email: str, to_name: str, subject: str, html_content: str) -> Optional[int]:
    """Send an email via Brevo API. Returns message ID on success, None on failure."""
    if not BREVO_API_KEY:
        print("❌ No BREVO_API_KEY set!")
        return None

    url = "https://api.brevo.com/v3/smtp/email"
    headers = {
        "api-key": BREVO_API_KEY,
        "Content-Type": "application/json",
    }

    payload = {
        "sender": {"email": SENDER_EMAIL, "name": SENDER_NAME},
        "to": [{"email": to_email, "name": to_name or to_email}],
        "subject": subject,
        "htmlContent": html_content,
    }

    try:
        resp = requests.post(url, json=payload, headers=headers, timeout=15)
        if resp.status_code in (200, 201):
            result = resp.json()
            print(f"  ✅ Sent to {to_name or to_email}: {subject[:50]}...")
            return result.get("messageId")
        else:
            print(f"  ❌ Error {resp.status_code}: {resp.text}")
            return None
    except Exception as e:
        print(f"  ❌ Connection error: {e}")
        return None


def load_leads(status_filter: str = "New") -> list:
    """Load leads from CSV, filtered by status."""
    leads = []
    try:
        with open(LEADS_FILE, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                if row.get("status", "") == status_filter:
                    leads.append(row)
    except FileNotFoundError:
        print(f"❌ Leads file not found: {LEADS_FILE}")
    return leads


def log_sent(lead: dict, template_name: str, message_id: str):
    """Log a sent email to history file."""
    headers = ["timestamp", "company_name", "contact_name", "email", "template", "message_id", "status"]
    file_exists = os.path.isfile(HISTORY_FILE)

    with open(HISTORY_FILE, "a", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=headers)
        if not file_exists:
            writer.writeheader()
        writer.writerow({
            "timestamp": datetime.now().isoformat(),
            "company_name": lead.get("company_name", ""),
            "contact_name": lead.get("contact_name", ""),
            "email": lead.get("email", ""),
            "template": template_name,
            "message_id": message_id or "",
            "status": "sent" if message_id else "failed",
        })


def personalize(template_type: str, lead: dict) -> tuple:
    """
    Personalize an email template for a given lead.
    Returns (subject, html_body).
    """
    template = TEMPLATES.get(template_type)
    if not template:
        raise ValueError(f"Unknown template: {template_type}")

    industry = lead.get("industry", "business")
    name = lead.get("contact_name", "").strip()
    company = lead.get("company_name", "your business")

    replacements = {
        "{company_name}": company,
        "{contact_name}": name or "there",
        "{industry_lower}": industry.lower(),
        "{sender_name}": SENDER_NAME,
        "{sender_email}": SENDER_EMAIL,
    }

    subject = template["subject"]
    html = template["html"]

    for placeholder, value in replacements.items():
        subject = subject.replace(placeholder, value)
        html = html.replace(placeholder, value)

    return subject, html


def send_campaign(template_type: str = "cold_outreach", dry_run: bool = False):
    """
    Send an email campaign to all 'New' leads.
    
    Args:
        template_type: Which template to use
        dry_run: If True, shows what would be sent without actually sending
    """
    leads = load_leads("New")
    if not leads:
        print("📭 No 'New' leads found in the database.")
        return

    print(f"\n📧 Sending '{template_type}' campaign to {len(leads)} leads")
    print("=" * 60)

    # Limit to daily free tier (300/day)
    max_sends = min(len(leads), 300)
    sent_count = 0

    for lead in leads[:max_sends]:
        if not lead.get("email"):
            print(f"  ⏭️  {lead['company_name']}: No email address — skipping")
            continue

        subject, html = personalize(template_type, lead)

        if dry_run:
            print(f"\n  📋 TO: {lead['company_name']} <{lead['email']}>")
            print(f"     SUBJECT: {subject}")
            print(f"     --- preview (first 200 chars) ---")
            print(f"     {html[:200].strip()}...")
            message_id = "dry_run"
        else:
            message_id = send_brevo_email(
                to_email=lead["email"],
                to_name=lead.get("contact_name", ""),
                subject=subject,
                html_content=html,
            )

        log_sent(lead, template_type, message_id)
        sent_count += 1

        # Rate limit: 10 emails per second for Brevo free tier
        if not dry_run:
            time.sleep(0.5)

    print(f"\n{'=' * 60}")
    print(f"✅ Campaign complete: {sent_count} emails {'(dry run)' if dry_run else 'sent'}")
    print(f"{'=' * 60}")


def main():
    import argparse
    parser = argparse.ArgumentParser(description="SiteSwift UAE Email Outreach")
    parser.add_argument("action", choices=["send", "dry-run", "stats"], default="dry-run", nargs="?")
    parser.add_argument("--template", choices=list(TEMPLATES.keys()), default="cold_outreach")
    
    args = parser.parse_args()

    if args.action == "stats":
        print_stats()
    elif args.action in ("send", "dry-run"):
        send_campaign(args.template, dry_run=(args.action == "dry-run"))


def print_stats():
    """Show email stats."""
    sent = 0
    failed = 0
    try:
        with open(HISTORY_FILE, "r") as f:
            reader = csv.DictReader(f)
            for row in reader:
                if row.get("status") == "sent":
                    sent += 1
                else:
                    failed += 1
    except FileNotFoundError:
        pass
    
    print(f"📊 Email Stats: {sent} sent, {failed} failed")


if __name__ == "__main__":
    main()
