# Automation Blueprint

## What This System Automates

This blueprint shows exactly what runs by itself, what needs you to push a button, and what is fully manual.

---

## Fully Automated (Runs Without You)

| Process | Tool | How |
|---|---|---|
| Website hosting + SSL | GitHub Pages | Site stays online 24/7. Zero maintenance. |
| Client site monitoring | UptimeRobot | Pings every 5 minutes. Emails you if down. |
| Analytics data collection | Google Analytics | Tracks visitors, pages, sources. Runs forever. |
| SEO indexing | Google Search Console | Crawls sites automatically. Alerts for issues. |
| Email sequence drafts | Templates (you trigger) | Content is pre-written. Ready to send. |
| Invoice collection | Stripe/GoCardless | Recurring billing. Auto-charges monthly. |
| Billing reminders | Stripe | Sends payment failure emails automatically. |
| Dashboard data display | dashboard.html | Reads your CSV and shows live stats. |

---

## Needs Your Approval To Execute

| Process | Why Human Needed | Your Action |
|---|---|---|
| Sending outreach emails | Spam prevention, personalization | Review → click send |
| Following up with leads | Context matters. Need to read the room. | Check thread → choose follow-up template |
| Building demo sites | Quality control. Your value add. | Collect info → AI-generate → review → share |
| Client onboarding | First impression. Needs warm handoff. | Send welcome → confirm preferences |
| Monthly client reports | Relationship building. Important touchpoint. | Generate report → send to client |
| Upsells | Timing matters. Push too early = lose client. | Check readiness → send offer |
| Lead list updates | Data quality. Avoid stale/duplicate leads. | Add new leads to CSV |
| Payment issues | Human touch for late payers. | Check → message client → resolve |
| Content updates | Client requests are specific. | Read request → update site |

---

## Purely Manual (No Automation)

| Task | Why It Stays Manual |
|---|---|
| Initial client discovery call | Building trust. Reading body language/tone. |
| Design decisions (colors, layout) | Client taste matters. Cannot automate aesthetics. |
| Client relationship management | People buy from people. Relationship = retention. |
| Walk-by lead discovery | Serendipity. You notice things algorithms miss. |
| Crisis resolution (site down, bug, etc.) | Needs immediate human judgment. |
| Strategic decisions (pricing changes, new services) | Business direction is your call. |

---

## Daily Workflow (30 min/day)

```
Morning (10 min):
  ┌─ Open dashboard → check new leads
  ├─ Review "Contacted" leads for follow-ups
  └─ Check UptimeRobot alerts (usually none)

Midday (15 min):
  ┌─ Send 3-5 personalized outreach emails
  ├─ Reply to WhatsApp inquiries
  └─ Update CSV with new lead statuses

Wrap-up (5 min):
  └─ Note tomorrow's follow-ups
```

---

## Weekly Workflow (2-3 hours/week)

```
Monday:
  ┌─ Find 10 new leads (Google Maps + Instagram, 15 min)
  ├─ Add to CSV
  └─ Send Monday batch outreach (5 emails)

Tuesday-Thursday:
  ┌─ Follow-ups from previous week
  ├─ Demo site builds (as needed)
  └─ Client check-ins

Friday:
  ┌─ Weekly stats review
  ├─ Pipeline update
  └─ Plan next week
```

---

## Monthly Workflow (3 hours/month)

```
Week 1:
  ┌─ Send monthly reports to all clients
  ├─ Check all invoices paid
  └─ Plan monthly content

Week 2-3:
  ┌─ Upsell outreach to qualified clients
  ├─ Review and update offer page copy
  └─ Update demo site template

Week 4:
  ┌─ Full pipeline review
  ├─ Revenue tracking
  ├─ What worked / what didn't
  └─ Set goals for next month
```

---

## Tools Needed

### Recommended Stack
| Tool | Purpose | Cost | Setup Time |
|---|---|---|---|
| GitHub (github.com) | Host sites + docs + dashboard | Free | 30 min |
| Gmail (google.com) | Email outreach | Free | Already have |
| Brevo (brevo.com) | Email sequences | Free tier | 1 hour |
| Stripe (stripe.com) | Payment processing | 2.9%+fee | 1 hour |
| UptimeRobot (uptimerobot.com) | Site monitoring | Free (50 monitors) | 15 min |
| Google Analytics (analytics.google.com) | Traffic tracking | Free | 30 min |
| Google Search Console (search.google.com) | SEO monitoring | Free | 15 min |
| Canva (canva.com) | Design assets (logos, graphics) | Free | Already have |
| Calendly (calendly.com) | Appointment booking | Free tier | 15 min |
| WhatsApp Business | Client communication | Free | Already have |

### Free Alternatives
| Paid Tool | Free Alternative | Limitation |
|---|---|---|
| Mailchimp ($13+/mo) | Brevo Free | 300 emails/day cap |
| HubSpot CRM | GitHub CSV + dashboard | No auto-email tracking |
| Google Workspace ($6/mo) | Free Gmail | Custom domain email not included |
| Wix ($16/mo) | GitHub Pages + demo template | No drag-and-drop editor |
| Salesforce ($25+/mo) | CSV + Python script | No pipeline automation |

---

## Risk Controls

### Spam Prevention
1. **Never send bulk.** Max 10 personalized emails/day from Gmail.
2. **Always use a real name and signature.** Spam filters flag anonymous senders.
3. **Warm up your email.** Start with 5 emails/day, increase by 2-3 per week.
4. **Track bounces.** If an email bounces, remove from list. Repeated bounces flag your domain.
5. **Don't buy email lists.** Ever. It's illegal in many places and instantly marks you as spam.
6. **Use a separate email for outreach.** Don't use your main personal email.
7. **One-click unsubscribe required.** By law in most countries (CAN-SPAM, GDPR if EU audience).

### Platform Ban Prevention
1. **Instagram DM outreach:** Keep it casual. No links in first message. Max 10 DMs/day.
2. **WhatsApp Business:** Don't mass message. Only contact people who opted in or you have a genuine business reason.
3. **Google Maps scraping:** Use the official Places API, not scrapers. Scraping can get your IP banned.

### Legal Safety
1. **Data privacy:** Don't share client data. Store CSV in a private GitHub repo.
2. **No medical advice.** You're selling websites. Don't give medical opinions.
3. **Contract terms:** Have a simple contract (see offer-page-copy for basics). No contract = no legal protection.
4. **VAT/Tax:** In UAE, you may need to register for VAT if revenue exceeds AED 375,000/year. Track your income.

### Client Management
1. **Set expectations.** 48-hour delivery in writing. Not "within 48 hours of every client request."
2. **Have a cancellation policy.** Month-to-month is fine. Give clients 14 days notice if you're canceling.
3. **Backup everything.** Before any update, back up the current live version.
4. **Scope creep.** Extra features beyond the plan = add-on charges. Be clear upfront.

---

## Revenue Tracking

### Simple System (Use a Google Sheet)
Create a sheet with columns:
- Client name
- Plan (Starter/Business/Premium)
- Monthly fee
- Sign-up date
- Payment status (Paid/Late/Canceled)
- Notes

### Automated System (Stripe Dashboard)
Stripe shows:
- Monthly recurring revenue (MRR)
- Active subscriptions
- Failed payments
- Customer lifetime value (LTV)

### Manual Tracking (For Tax)
Keep a simple log:
```
Month: May 2026
Revenue: AED XXXX
Expenses: AED XXX (domain renewals, AI API costs)
Profit: AED XXX
Clients: X active
Churn: X canceled
```

---

## How to Improve Conversion

### Track These Metrics
| Metric | Good | Great | How to Measure |
|---|---|---|---|
| Email open rate | 40%+ | 60%+ | Gmail tracking (or Brevo) |
| Reply rate | 10%+ | 25%+ | Manual count |
| Demo → Client conversion | 30%+ | 50%+ | Pipeline tracking |
| Monthly churn | <5% | <2% | Stripe dashboard |
| Average revenue per client | AED 499 | AED 799+ | Stripe dashboard |

### Optimization Playbook

**If open rates are low:**
- Change subject lines. Test personal vs professional.
- Send at different times (try 9am Sunday vs 9am Wednesday).
- Use the recipient's name in the subject line.

**If reply rates are low:**
- Shorten the email. 3 sentences max for first touch.
- Add a specific compliment ("Your Instagram has 5K followers — impressive").
- Ask a specific question ("What's the biggest challenge with your current site?").

**If demo → client conversion is low:**
- Improve the demo quality. Use their actual branding.
- Show them competitor sites for comparison.
- Offer a 14-day free trial instead of asking for commitment.
- Build urgency: "This price is for this quarter only."

**If churn is high:**
- Check in mid-month (not just on billing day).
- Add value beyond the website (monthly tips, industry insights).
- Ask for feedback before they cancel. Sometimes a price adjustment keeps them.

---

## First 30-Day Launch Plan

| Week | Goal | Tasks |
|---|---|---|
| Week 1 | Setup | Set up GitHub Pages, create email account, install tools, build first 5 demo sites (portfolio) |
| Week 2 | First clients | Find 50 leads, send 25 personalized emails, follow up with responses |
| Week 3 | Revenue | Convert 2-3 demos into clients, send invoices, build client sites |
| Week 4 | Optimize | Review what worked, improve templates, find 50 more leads, refine process |

---

## Scaling Beyond MVP

When you hit 10+ clients (AED 5K-8K/month MRR), consider:

1. **Hire a VA** for lead research ($200-300/month, Philippines/Pakistan)
2. **Use a proper CRM** like Pipedrive or HubSpot ($15-30/month)
3. **Build a proper template system** so demo sites take 15 minutes
4. **Outsource basic site builds** to a freelancer ($50/site), you handle sales and client management
5. **Launch the German medical pathway** as a second income stream
