# Automation Workflow — AI Website Agency

## Overview
This is a semi-automated system. Some parts run by themselves. Others need you to push a button or say yes. This document covers what, when, and how.

---

## Workflow Diagram

```
Lead Sources (automated)
    │
    ▼
Lead Database (CSV → Dashboard)
    │
    ▼
Email Sequence (automated drafts, manual send)
    │
    ▼
Call/WhatsApp Follow-up (manual — you)
    │
    ▼
Demo Site Built (you build using AI)
    │
    ▼
Close → Onboarding (email templates automate this)
    │
    ▼
Monthly Maintenance (automated monitoring)
    │
    ▼
Upsells (automated triggers)
```

---

## 1. Lead Generation (Semi-Automated)

**Automated:**
- Google Maps scraper script (see below) collects clinic/gym/cafe data
- Instagram manual search → paste into CSV

**Manual:**
- Walking by businesses and noting them
- Referrals from existing clients

**Automation Tool:**
```python
# google_maps_leads.py — Basic version (run locally)
# Scrapes Google Maps for businesses in a given area/industry
# Outputs CSV ready for your dashboard

# Requirements: pip install requests beautifulsoup4
# WARNING: Google Maps scraping may violate ToS. Use the Places API instead.
# Better approach: Use Google Places API (free tier: $200/month credit)

import requests
import csv
import json

def search_places(api_key, query, location):
    url = "https://maps.googleapis.com/maps/api/place/textsearch/json"
    params = {
        "query": query,
        "location": location,
        "radius": 5000,
        "key": api_key
    }
    response = requests.get(url, params=params)
    data = response.json()
    return data.get("results", [])

# Usage example (with your API key):
# results = search_places("YOUR_API_KEY", "clinics in Dubai Marina", "25.2048,55.2708")
# Then save to CSV
```

**Free Alternative:** Manually search Google Maps and Instagram → paste into CSV. Takes 15 minutes to find 20 leads.

---

## 2. Lead Capture & Storage (Automated)

**What runs automatically:**
- CSV file acts as your database
- dashboard.html reads and displays it (open in browser)
- Python script can auto-append new leads

**Tool:** GitHub Pages hosts your dashboard for free.

**Setup:**
1. Push `dashboard.html` and `leads.csv` to a GitHub repo
2. Enable GitHub Pages
3. Every time you update the CSV, the dashboard refreshes

---

## 3. Outreach (Semi-Automated)

**What's automated:**
- Email drafts using templates
- 3-email sequence reminders (you write in your calendar or use a simple tool)
- Tomorrow's follow-up list

**What needs human approval:**
- Sending the actual email (never automate sending — spam filters and legal)
- Personalizing the template with the lead's name and specific detail

**Tool:** Gmail (free) with Boomerang or Mixmax for scheduling. Or just use your calendar.

**Better Tool:** Mailcoach (self-hosted, ~$20/month) or Brevo (free up to 300 emails/day).

**Workflow:**
1. Open your dashboard → see "Pending Follow-ups"
2. Copy template → personalize → send
3. Update CSV status to "Contacted"

---

## 4. Demo Site Building (Manual — You)

**Not automated. This is your value add.**

However, you can speed it up with AI:
- Use Claude/GPT to generate site copy from client info
- Use the `demo-website-template.html` as a base and customize
- Use AI image generation (Bing Image Creator, free) for hero images

**Time per demo:** 1-2 hours first time, 30 minutes with practice.

---

## 5. Onboarding (Automated)

**What runs automatically:**
- Welcome email sequence (use the templates)
- Monthly check-in templates
- Invoice reminders

**Tool:** Brevo free plan (automated email sequences up to 300/day)

**Setup:**
1. Create a Brevo account
2. Set up 3 automated emails:
   - Day 1: Welcome + what to expect
   - Day 3: "Here's your draft" trigger
   - Day 7: "Your site is live"
   - Day 30: Monthly report template
3. Manually trigger each email when the stage is reached

---

## 6. Maintenance (Automated Monitoring)

**Free tools:**
- UptimeRobot (free): Monitors client sites, alerts you if down
- Google Analytics: Set up and get monthly reports emailed to you
- Google Search Console: Alerts for any site issues

**Automated reports:**
Use Google Analytics API + a free script to email you monthly stats per client.

---

## 7. Billing (Semi-Automated)

**Tool:** GoCardless (UAE-compatible) or Stripe
- Automated monthly invoices
- Automated payment collection
- Automated late payment reminders

**Setup:** Create Stripe account → create subscription products → send clients subscription links.

---

## 8. Upsells (Automated Triggers)

Based on client behavior, trigger upsell offers:
- "Your site has 500+ visitors this month → time for the Business plan"
- "You've been a client for 6 months → here's a loyalty upgrade offer"
- "Your competitor just got a site → here's how to stay ahead"

**Tool:** Manual for now (check dashboard → see client age → send upsell email)

---

## Daily/Weekly Workflow

### Daily (30 minutes)
1. Open dashboard — check for new leads
2. Send 3-5 personalized outreach emails
3. Respond to any WhatsApp messages from prospects
4. Update CSV with status changes

### Weekly (2 hours)
1. Follow up on "Contacted" leads (Day 3/7 emails)
2. Build 1-2 demo sites for interested prospects
3. Check on existing clients (quick WhatsApp check-in)
4. Review monthly stats for each client
5. Find 10 new leads (Google Maps + Instagram)

### Monthly (3 hours)
1. Send monthly reports to each client
2. Invoice review (ensure all clients paid)
3. Pipeline review: new leads → contacted → demo → client
4. Content updates for client sites
5. Plan next month's outreach

---

## Tool Stack (All Free/Low-Cost)

| Tool | Purpose | Cost |
|---|---|---|
| GitHub Pages | Host demo sites + dashboard | Free |
| Gmail | Email outreach | Free |
| Brevo | Email sequences | Free (300/day) |
| GoCardless/Stripe | Billing | 1-2% per transaction |
| UptimeRobot | Site monitoring | Free (50 monitors) |
| Google Analytics | Traffic stats | Free |
| Google Search Console | SEO monitoring | Free |
| Google Places API | Lead data | Free tier ($200 credit) |
| Claude/GPT | AI copywriting | Free/paid |
| Calendly | Booking calls | Free |
| WhatsApp Business | Client communication | Free |

---

## Risk Controls

1. **Never automate sending email** without review. Spam filters are aggressive.
2. **Never scrape aggressively.** Respect rate limits. Use official APIs.
3. **Always personalize.** Generic outreach converts at < 1%.
4. **Keep client data private.** Don't share CSV files publicly.
5. **Use disclaimers.** If you give any advice (digital presence, SEO), add "results may vary."
6. **Back up everything.** Keep CSV in Google Sheets or GitHub private repo.
7. **Don't make promises you can't keep.** 48-hour delivery means 48 hours of YOUR time, not calendar days if you're busy.
8. **A/B test outreach.** Track which templates work best.
