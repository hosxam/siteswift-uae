# SiteSwift UAE — Launch TODO

> ⚡ Estimated time to first client: **2-4 weeks**

---

## 🔴 RIGHT NOW (Today — 2 hours)

### Brand Setup
- [ ] Pick your business name (or keep "SiteSwift UAE")
- [ ] Create a dedicated Gmail: `siteswift.uae@gmail.com` or yourchoice@gmail.com
- [ ] Get a dedicated UAE number (Etisalat pay-as-you-go SIM = AED 50)

### Account Setup (3 accounts, 15 min each)
- [ ] **Brevo** — Go to https://www.brevo.com/ → Free Account → Verify email → API Keys
- [ ] **Stripe** — Go to https://stripe.com/en-ae → Create account → Add 3 products (Starter/Business/Premium) with recurring billing
- [ ] **Google Places API** — Go to https://console.cloud.google.com/ → New Project → Enable Places API → Create Credentials (API Key)

### Deploy
- [ ] Edit `index.html` — replace `[YOUR-EMAIL]` and `[YOUR-WHATSAPP-NUMBER]` with your real info
- [ ] Push to GitHub → auto-deploys to https://hosxam.github.io/siteswift-uae/

---

## 🟡 THIS WEEK

### Tech Setup
- [ ] **Install Python deps:** `pip install -r requirements.txt`
- [ ] **Copy .env:** `cp .env.example .env` and fill in all values
- [ ] **Generate portfolio:** `python demo_generator.py --batch` → opens 22 demo sites
- [ ] **Install UptimeRobot:** Add your GitHub Pages URL as a monitor
- [ ] **Set up Google Analytics:** Add your G-ID to the landing page

### Outreach
- [ ] **Research contact info:** Run `python enrich_leads.py` → opens search tabs for phone/email
- [ ] **Find 5 real phone numbers** from Google Maps direct listings (click each lead on maps.google.com)
- [ ] **Send 5 personalized emails** using `outreach-email-templates.md` — NOT copy-paste, personalize each
- [ ] **Send 5 Instagram DMs** using templates in `instagram_dm_templates.md`
- [ ] **Log all outreach** in the CSV (update `status` column)

### Sales Ready
- [ ] Read `sales-script.md` — practice it once out loud
- [ ] Create a free Calendly account: https://calendly.com
- [ ] Set up Calendly link for "15 min discovery call"

---

## 🟢 WEEK 2

### First Sales
- [ ] Follow up with everyone from Week 1 (use `follow-up-script.md`)
- [ ] Book first discovery call
- [ ] Send first proposal using `pricing-packages.md`
- [ ] Close first client 🎉

### Automation
- [ ] Configure Brevo sequences:
  - Day 0: Welcome email
  - Day 3: Follow-up email  
  - Day 7: Value-add email
  - Day 14: "Last chance" email
- [ ] Run `python setup_scheduler.py` to auto-scrape daily
- [ ] Add 20 more leads to the database (search "restaurants Dubai no website" etc.)

### Pipeline
- [ ] Update `dashboard.html` with your stats card values
- [ ] Track every interaction in the CSV

---

## 🔵 MONTH 1

### Growth
- [ ] Target 2 clients minimum (AED 1,000+ MRR)
- [ ] Collect 3 testimonials
- [ ] Build case studies from first clients
- [ ] Update landing page with testimonials
- [ ] Add portfolio section with real client sites

### Scale
- [ ] Hire a VA for lead research (AED 500-1000/mo)
- [ ] Set up referral program: "Refer a business, get 1 month free"
- [ ] Expand to DIFC, JLT, Barsha areas
- [ ] Build "Website Audit" free tool → captures leads automatically

---

## 🟣 MONTH 3 TARGETS

- [ ] 8 clients → AED 4,000+ MRR
- [ ] Automate 80% of outreach with Brevo sequences
- [ ] Start Instagram ads for lead generation (AED 200/mo budget)
- [ ] Partner with a freelancer for overflow work
- [ ] Launch SEO add-on service (AED 299/mo per client)

---

## 📈 MONTH 6 TARGETS

- [ ] 20 clients → AED 10,000+ MRR
- [ ] Consider hiring a salesperson (commission-only to start)
- [ ] Launch the German medical pathway digital products as secondary income
- [ ] Evaluate: should you scale or keep it semi-automated?

---

## 💡 PRO TIPS

**Don't build perfect websites.** Build "good enough" and launch fast. You can always iterate.

**Price is not the problem.** The problem is trust. A 5-minute call where you show a demo site does more than 50 emails.

**Instagram DMs > Email for UAE small businesses.** They check IG 10x more than email. Send short DMs.

**Use the "no website" angle.** It's not an insult — it's a fact. "I noticed you don't have a website" is the strongest opener.

**Collect testimonials from Day 1.** Future clients decide based on social proof, not features.

**Monthly recurring revenue is the goal.** One sale = money every month. Worth more than a one-time project.
