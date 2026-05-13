# SiteSwift UAE — Brevo Email Sequences (Ready to Import)

> Copy-paste these into Brevo's campaign editor.
> Set up as automated sequences triggered by contact creation.

---

## SEQUENCE 1: Welcome & Discovery

**Trigger:** Contact added (lead status = "New")

### Email 1 — Day 0: Cold Outreach

**Subject:** A quick website idea for {{company_name}}

**Body:**
```
Hi {{contact_name}},

I was looking at {{company_name}} on Google Maps and noticed you don't have a website yet. In Dubai, that means you're probably losing customers who search online first — and these days, that's most of them.

I build simple, professional websites for Dubai businesses starting at AED 499/month. Everything included — design, hosting, domain, SEO, and a contact form so customers can find and reach you.

Here's what other businesses say:

    "We started getting booking requests through our website within the first week. Best investment we've made." — Dubai Clinic Owner

Want to see what it would look like? I can put together a quick demo for {{company_name}} at no cost — no commitment.

Let me know if you're open to a 5-minute chat.

Best regards,
[Your Name]
SiteSwift UAE
```

---

### Email 2 — Day 3: Follow-up

**Subject:** Re: Quick website idea for {{company_name}}

**Body:**
```
Hi {{contact_name}},

Following up on my earlier message — I know you're busy.

Quick question: How do new customers usually find you right now?

1. Word of mouth? Great, but not enough to grow.
2. Google Maps? A website makes you show up way higher.
3. Instagram? A site is where serious customers go to decide.

I'm offering a free demo site for {{company_name}} — I'll build a sample page showing exactly how your business would look online. It takes me about 2 hours, and if you don't like it, no charge, no obligation.

Worth a try?

Best,
[Your Name]
```

---

### Email 3 — Day 7: Value-Add / Social Proof

**Subject:** We just helped a {{industry}} business go online 🚀

```
Hi {{contact_name}},

I wanted to share something interesting — last week we launched a website for a {{industry}} business in your area. Within 3 days, they started getting contact form submissions from new customers who found them on Google.

I thought of {{company_name}} because you're in the same industry and — as I mentioned — you don't have an online presence yet.

Every day without a website means potential customers are finding your competitors instead.

Let me know if you'd like to see what a {{industry}} website could look like. I'll put one together for {{company_name}} in 2 hours, free.

Best,
[Your Name]
```

---

### Email 4 — Day 14: Last Attempt / Objection Handler

**Subject:** Final thought on a website for {{company_name}}

**Body:**
```
Hi {{contact_name}},

This is my last message on this — I don't want to spam you.

I genuinely believe {{company_name}} could benefit from having a simple website. Here's why I know this works:

1. Every client I've built for has gotten at least 3+ inquiries in the first month
2. Monthly subscription means no upfront cost
3. I handle everything: hosting, domain, updates, SEO

If timing isn't right, no worries. My offer stands whenever you're ready.

But if you have 5 minutes this week, I'd love to show you what I mean. No pressure.

Best,
[Your Name]
```

---

### Email 5 — Day 30: Win-Back (if no reply)

**Subject:** {{company_name}} — still interested?

**Body:**
```
Hi {{contact_name}},

Been about a month since I reached out. Hope business is going well.

Just a quick note — I noticed {{company_name}} still doesn't have a website. Meanwhile, at least 3 of your competitors have gone online this month.

If budget is a concern, I understand. Our Starter plan is just AED 499/month with zero upfront cost. That's less than what most businesses spend on coffee runs.

Happy to do a quick call if anything's changed.

Best,
[Your Name]
```

---

## SEQUENCE 2: Post-Demo (After client sees demo site)

**Trigger:** Demo sent (lead status = "Demo Sent")

### Email 1 — Same Day: Demo Follow-up

**Subject:** Here's your {{company_name}} demo site 🎉

**Body:**
```
Hi {{contact_name}},

I put together a quick demo for {{company_name}}. Check it out here:

[LINK TO DEMO SITE]

What do you think? This is just a starting point — we can change colors, text, images, anything you want.

A few things to note:
- This site will show up on Google search
- Customers can contact you directly through the form
- We can add online booking if you need it

Want to jump on a quick call to discuss next steps? I'm free tomorrow at [TIME].

Best,
[Your Name]
```

### Email 2 — Day 3: Pricing Breakdown

**Subject:** How the {{industry}} website package works

**Body:**
```
Hi {{contact_name}},

Just following up on the demo I sent you. Here's how it works:

✅ Everything included:
- Custom website design
- Hosting & domain (yourname.ae)
- Google-friendly SEO
- Mobile optimized
- Contact form
- 24/7 support

💰 Pricing:
- Starter: AED 499/month
- Business: AED 799/month  
- Premium: AED 1,299/month

Zero setup fee. Month-to-month. Cancel anytime.

Want to start this week? I can have your site live in 48 hours.

Best,
[Your Name]
```

---

## SEQUENCE 3: Post-Launch (Client onboarded)

### 1 Week Check-in
**Subject:** How's {{company_name}}'s new site doing?

```
Hey {{contact_name}},

Your website has been live for a week! Wanted to check in:

1. Have you gotten any inquiries through the contact form?
2. Anything you want to change or add?
3. Are you happy with how it looks on mobile?

Let me know if you need anything tweaked. I'm here to help.

Best,
[Your Name]
```

### 1 Month Review
**Subject:** {{company_name}} — first month report

```
Hi {{contact_name}},

Quick recap of your site's first month:

- Total visitors: [NUMBER]
- Contact form submissions: [NUMBER]
- Top pages: [PAGES]

Your site is ranking on Google for "[KEYWORD] Dubai" — that's how local customers find you.

Any questions? Happy to optimize further.

Best,
[Your Name]
```

---

## 🔧 Brevo Setup Instructions

1. Go to https://app.brevo.com/
2. Click **Contacts** → **Import** → Upload the CSV (`lead-database-template.csv`)
3. Map columns: `email` → EMAIL, `company_name` → COMPANY, `phone` → PHONE, etc.
4. Go to **Automation** → **Create a workflow**
5. Choose **Contact added to list** → select your lead list
6. Add emails one by one using the templates above
7. Set wait periods: 3 days, 7 days, etc.
8. Activate the workflow

**Free tier limit:** 300 emails/day. Your sequence for 22 leads = 22 emails × 5 = 110 emails. Well within free tier.
