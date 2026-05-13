"""
SiteSwift UAE - Instagram DM Outreach Toolkit
----------------------------------------------
For businesses in Dubai that are active on Instagram but don't have websites.
Instagram doesn't have a public DM API, so this tool:
 1. Discovers Instagram handles for leads in the CSV
 2. Generates DM message templates
 3. Provides a Chrome extension script for semi-automated DMs

You'll still need to send DMs manually (or use a third-party IG automation tool).
This tool makes the discovery and message crafting easy.
"""

import os
import csv
import re
import json
from datetime import datetime
from typing import List, Dict, Optional

LEADS_FILE = os.path.join(os.path.dirname(__file__), "lead-database-template.csv")


def generate_dm(company_name: str, industry: str) -> str:
    """
    Generate a personalized Instagram DM message.
    Short, casual, professional — the kind that actually gets replies on IG.
    """
    industry_emojis = {
        "gym": "💪",
        "salon": "💇",
        "cafe": "☕",
        "dental": "🦷",
        "physio": "🦵",
        "medical": "🏥",
        "beauty": "💄",
        "fitness": "🏋️",
        "restaurant": "🍽️",
        "general": "✨",
    }

    emoji = industry_emojis.get(industry.lower(), "✨")

    dm = f"""Hey! {emoji} Love your page — {company_name} looks great.

Quick question: do you have a website? I noticed you don't show up when I search for {industry} in our area, and I bet you're losing customers who look online first.

I build simple websites for Dubai businesses starting at AED 499/month — everything included, no tech skills needed. Happy to show you a quick demo if you're interested!

Let me know 😊
      
P.S. Not selling, just genuinely think you deserve to be found online.
"""
    return dm


def generate_all_dms() -> str:
    """Generate DM templates for all leads in the CSV."""
    if not os.path.exists(LEADS_FILE):
        return "No leads file found."

    output_parts = ["# SiteSwift UAE - Instagram DM Templates", f"# Generated: {datetime.now().strftime('%Y-%m-%d %H:%M')}", ""]

    with open(LEADS_FILE, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for i, lead in enumerate(reader, 1):
            company = lead.get("company_name", "Unknown")
            industry = lead.get("industry", "general")
            
            # Generate Instagram handle guess
            handle = guess_instagram_handle(company)
            
            output_parts.append(f"## {i}. {company}")
            output_parts.append(f"   Industry: {industry}")
            output_parts.append(f"   Suggested IG: {handle}")
            output_parts.append("")
            output_parts.append("```")
            output_parts.append(generate_dm(company, industry))
            output_parts.append("```")
            output_parts.append("")

    return "\n".join(output_parts)


def guess_instagram_handle(company_name: str) -> str:
    """Generate likely Instagram handles based on business name."""
    name = company_name.lower().strip()
    
    # Remove common suffixes
    for suffix in [" dubai", " - dubai", " marina", " - marina", " jbr", " - jbr"]:
        name = name.replace(suffix, "")
    
    # Clean up
    name = re.sub(r'[^a-z0-9&]', '', name)
    name = name[:30]  # IG max handle length
    
    variants = [
        name,
        name.replace("&", ""),
        name + "dxb",
        name + "dubai",
    ]
    
    return variants[0]


def export_instagram_search_urls():
    """Generate a list of Instagram search URLs for manual DM outreach."""
    if not os.path.exists(LEADS_FILE):
        return []

    urls = []
    with open(LEADS_FILE, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for lead in reader:
            company = lead["company_name"]
            handle = guess_instagram_handle(company)
            urls.append({
                "company": company,
                "handle": handle,
                "search_url": f"https://www.instagram.com/{handle}/",
                "web_search": f"https://www.google.com/search?q=instagram+{company.replace(' ', '+')}+dubai",
            })
    return urls


def create_chrome_extension_script():
    """
    Generate a JavaScript snippet you can paste into Chrome DevTools
    on Instagram.com to speed up the DM process.
    
    USE RESPONSIBLY — Instagram limits actions. Do 10-15 DMs per day max.
    """
    urls = export_instagram_search_urls()
    
    script = f"""
// ============================================
// SiteSwift UAE - Instagram DM Helper
// ============================================
// HOW TO USE:
// 1. Go to instagram.com and log in
// 2. Open DevTools (F12) 
// 3. Go to Console tab
// 4. Paste this script
// 5. Run: siteswift_dm_list()
//
// This just shows you the list. You send DMs manually.
// ============================================

const SITESWIFT_LEADS = {json.dumps([{ "name": u["company"], "handle": u["handle"], "url": u["search_url"] } for u in urls], indent=2)};

function siteswift_dm_list() {{
    console.log('📋 SiteSwift UAE - Leads for DM Outreach');
    console.log('=========================================');
    console.log(`Total: ${{SITESWIFT_LEADS.length}} leads`);
    console.log('');
    
    SITESWIFT_LEADS.forEach((lead, i) => {{
        console.log(`${{i + 1}}. @${{lead.handle}} - ${{lead.name}}`);
    }});
    
    console.log('');
    console.log('💡 Open leads in new tabs:');
    console.log('   SITESWIFT_LEADS.forEach(l => window.open(l.url, "_blank"));');
    console.log('   Then send DMs manually (IG rate limits ~10-15 DMs/day)');
}}

// Auto-run on paste
siteswift_dm_list();
"""
    ext_path = os.path.join(os.path.dirname(__file__), "instagram_dm_helper.js")
    with open(ext_path, "w", encoding="utf-8") as f:
        f.write(script)
    print(f"✅ Instagram helper script saved to: {ext_path}")
    print(f"   Open Instagram, paste this into DevTools console.")


def main():
    print("=" * 60)
    print("SiteSwift UAE - Instagram DM Outreach Toolkit")
    print("=" * 60)

    # Generate DM templates
    dms = generate_all_dms()
    dms_file = os.path.join(os.path.dirname(__file__), "instagram_dm_templates.md")
    with open(dms_file, "w", encoding="utf-8") as f:
        f.write(dms)
    print(f"✅ DM templates saved to: {dms_file}")

    # Create Chrome helper script
    create_chrome_extension_script()

    # Show preview
    print("\n📱 DM Preview (first lead):")
    print("-" * 40)
    print(generate_dm("GFTeam Dubai", "fitness"))


if __name__ == "__main__":
    main()
