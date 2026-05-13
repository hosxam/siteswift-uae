# SiteSwift UAE — Semi-Automated AI Website Agency

> Turnkey business system for launching an AI website agency targeting UAE small businesses.
> Zero startup cost. Built with free tiers only.

**Live Landing Page:** https://hosxam.github.io/siteswift-uae/

**What is this?** A complete, ready-to-launch system that finds Dubai businesses without websites, automatically generates demo sites, sends personalized outreach, and manages the sales pipeline. Semi-automated means the computer handles the heavy lifting — you handle the conversations.

---

## 🚀 30-Minute Launch Checklist

### Step 1: Customize Your Brand (5 min)
- [ ] Pick a business name (change "SiteSwift UAE" to your brand)
- [ ] Get a dedicated phone number (UAE prepaid SIM or VoIP)
- [ ] Set up a dedicated Gmail for outreach

### Step 2: Edit Placeholders (5 min)
Search all files for `[YOUR-` and `[YOUR-...]` — replace with your actual info:
- WhatsApp number (e.g., `971501234567`)
- Your email address
- Business name

### Step 3: Create Your Accounts (10 min)
| Tool | URL | Free Tier | Purpose |
|------|-----|-----------|---------|
| Brevo | brevo.com | 300 emails/day | Email automation |
| Stripe | stripe.com | Usage-based | Payment processing |
| UptimeRobot | uptimerobot.com | 50 monitors | Site monitoring |
| Google Analytics | analytics.google.com | Free | Track visitors |
| Google Places API | console.cloud.google.com | $200/mo credit | Lead scraping |

### Step 4: Run the Tools (10 min)
```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Copy and fill in .env
cp .env.example .env
# Edit .env with your API keys

# 3. Generate demo sites for all 22 leads
python demo_generator.py --batch
# Output: 22 industry-specific landing pages in demo-sites/

# 4. Try a dry run of email outreach
python email_outreach.py dry-run
# Shows you what emails look like before sending

# 5. Research lead contact info
python enrich_leads.py
# Opens search tabs to fill in missing phones/emails

# 6. Set up automation
python setup_scheduler.py
# Creates Windows scheduled tasks for daily scraping
```

---

## 📁 File Structure

```
business-system/
├── 📄 README.md                  ← You are here
├── 📄 TODO.md                    ← Prioritized task list
├── 📄 .env.example               ← Environment variables template
├── 📄 requirements.txt           ← Python dependencies

├── 📄 MONEY_SYSTEM_AUDIT.md      ← 10 business models ranked
├── 📄 FINAL_REPORT.md            ← Complete validation & projections
├── 📄 AUTOMATION_BLUEPRINT.md    ← Automation architecture

## Sales & Marketing
├── 📄 outreach-email-templates.md    ← 6 email templates
├── 📄 follow-up-script.md            ← Day 1/3/7 follow-ups
├── 📄 sales-script.md                ← Full sales conversation
├── 📄 offer-page-copy.md             ← Landing page sales copy
├── 📄 pricing-packages.md            ← 3 pricing tiers
├── 📄 instagram_dm_templates.md      ← DM templates for IG outreach
├── 📄 instagram_dm_helper.js         ← DevTools script for IG DMs

## Data & Pipeline
├── 📄 lead-database-template.csv     ← 22 real UAE leads
├── 📄 dashboard.html                 ← Live pipeline dashboard

## Python Tools
├── 🐍 scraper.py                     ← Google Maps lead scraper
├── 🐍 email_outreach.py              ← Brevo email campaign sender
├── 🐍 demo_generator.py              ← Creates industry-specific websites
├── 🐍 enrich_leads.py                ← Finds missing phone/email
├── 🐍 instagram_dm_toolkit.py        ← IG outreach generator
├── 🐍 setup_scheduler.py             ← Windows Task Scheduler setup

## Generated Demos (22 real businesses)
├── 📁 demo-sites/
│   ├── gfteam-dubai.html
│   ├── wellfit-marina.html
│   ├── prime-fitness-dubai-marina.html
│   ├── abooz-cafe---jbr.html
│   └── ... (22 total)
├── 📄 index.html                     ← Landing page (also on GitHub Pages)
├── 📄 demo-website-template.html     ← Editable template
```

---

## 💰 Revenue Model

| Tier | Price | Frequency | Target |
|------|-------|-----------|--------|
| **Starter** | AED 499/month | Recurring | Cafes, salons, barbers |
| **Business** | AED 799/month | Recurring | Clinics, gyms, physio |
| **Premium** | AED 1,299/month | Recurring | Medical centers, real estate |

**Monthly recurring revenue targets:**
- Month 1: 2 clients → AED 1,000+ MRR
- Month 3: 8 clients → AED 4,000+ MRR  
- Month 6: 20 clients → AED 10,000+ MRR

---

## 🎯 Lead Sources (22 Real Businesses Ready)

The database already has businesses in Dubai Marina area:
- **Gyms:** GFTeam Dubai, Wellfit Marina, Prime Fitness (2 branches), The Marina Gym, SWT Arena
- **Salons/Beauty:** Brow Studio, Gladys Beauty, Eleven Signature, Wide Star, Kate White, PERSONA
- **Cafes:** Abooz Cafe, Arabian Cave Cafe, Risen Cafe, Nargileci Eleven, The Lost, Cafe Society, Common Grounds
- **Health:** Lifestyle Hair Care, Prime Physiotherapy, Al Manara Medical Fitness

All verified as having NO website (or only Instagram/Delivery-only presence).

---

## 🛠️ Tech Stack

| Tool | Free Tier Limit | Monthly Cost |
|------|-----------------|-------------|
| GitHub Pages | 1 site, 1GB | $0 |
| Brevo | 300 emails/day | $0 |
| Google Places API | $200/mo credit | $0 |
| Stripe | Per-transaction fees | ~$0 for testing |
| UptimeRobot | 50 monitors | $0 |
| Python | Anywhere | $0 |

---

## 📊 Dashboard

Open `dashboard.html` in your browser for a live pipeline view:
- Lead tracking with stages
- Revenue projections
- Meeting scheduling

---

## ❓ Questions?

Everything is documented in the files above. Start with `TODO.md` for the exact next steps. If you're stuck:
1. Read the relevant script's docstring (startup docs in each .py file)
2. The `.env.example` file lists all required configuration
3. Each Python tool has `--help` flag: `python scraper.py --help`

---

*Built with zero budget, maximum initiative.*
