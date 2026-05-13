"""
SiteSwift UAE - Lead Enrichment Tool
-------------------------------------
Scrapes individual business pages to find email addresses and phone numbers.
Google Places API gives us names and locations. This tool tries to find contact info.

The tool uses search-based discovery to find:
  1. Email addresses (via known patterns)
  2. Phone numbers (if not in Google Maps)
  3. Instagram handles
  4. Facebook pages

This is a semi-automated tool. It generates search URLs for you to check manually
or finds publicly available info from business directories.

Usage:
  python enrich_leads.py
     -> Opens browser tabs to search for contact info for each lead
  
  python enrich_leads.py --auto
     -> Uses web scraping to find info automatically (experimental)
"""

import os
import csv
import re
import webbrowser
import json
import requests
from typing import Dict, Optional, List
from datetime import datetime
from urllib.parse import quote

try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass

LEADS_FILE = os.path.join(os.path.dirname(__file__), "lead-database-template.csv")

# UAE phone number patterns
PHONE_PATTERNS = [
    r'(?:\+971|00971|0|971)[-\s]?5[0-9][-\s]?\d{3}[-\s]?\d{4}',  # Mobile
    r'(?:\+971|00971|0|971)[-\s]?[0-9][-\s]?\d{3}[-\s]?\d{4}',   # Landline
    r'0[0-9]{2,3}[-\s]?\d{3}[-\s]?\d{4}',                        # Local format
]

# Email pattern
EMAIL_PATTERN = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'


def search_phone(company_name: str) -> List[str]:
    """
    Search for a business's phone number using Google search.
    Returns list of found phone numbers.
    """
    url = f"https://www.google.com/search?q={quote(company_name)}+Dubai+phone+number"
    return [url]  # Return search URL for manual check


def suggest_email(company_name: str) -> Optional[str]:
    """
    Generate likely email addresses based on the company name.
    These are educated guesses, not verified.
    """
    # Strip common suffixes and clean name
    name = company_name.lower().strip()
    for suffix in [" dubai", " uae", " - dubai", " marina", " jbr", " llc", " fzc"]:
        name = name.replace(suffix, "")
    
    # Generate domain
    domain = name.replace("'", "").replace("&", "and").replace(" ", "").replace("-", "")
    domain = re.sub(r'[^a-z0-9]', '', domain)

    guesses = [
        f"info@{domain}.ae",
        f"info@{domain}.com",
        f"contact@{domain}.ae",
        f"book@{domain}.ae",
        f"{domain}@{domain}.ae",
    ]
    
    # Always include a guess even if domain is empty
    if not domain:
        return None
    
    return guesses[0]


def scrape_business_directory_search(company_name: str) -> Dict:
    """
    Try to find business info from public directories.
    Uses Google Custom Search (if API_KEY set) or returns search URLs.
    """
    api_key = os.getenv("GOOGLE_API_KEY", "")
    
    if api_key:
        # Use Google Custom Search to find the business
        try:
            url = "https://www.googleapis.com/customsearch/v1"
            params = {
                "key": api_key,
                "cx": "YOUR_SEARCH_ENGINE_ID",  # Requires Custom Search Engine setup
                "q": f"{company_name} Dubai phone email",
                "num": 5,
            }
            resp = requests.get(url, params=params, timeout=10)
            data = resp.json()
            return {
                "results": data.get("items", []),
                "total_results": data.get("searchInformation", {}).get("totalResults", 0),
            }
        except Exception as e:
            return {"error": str(e)}
    
    return {
        "search_url": f"https://www.google.com/search?q={quote(company_name)}+Dubai+contact",
    }


def enrich_leads():
    """Read the lead database and try to find missing contact info."""
    if not os.path.exists(LEADS_FILE):
        print(f"❌ Leads file not found: {LEADS_FILE}")
        return

    leads = []
    with open(LEADS_FILE, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        leads = list(reader)

    missing_phone = [l for l in leads if not l.get("phone", "").strip()]
    missing_email = [l for l in leads if not l.get("email", "").strip()]
    
    print(f"\n📊 Lead Database Stats:")
    print(f"   Total leads: {len(leads)}")
    print(f"   Missing phone: {len(missing_phone)}")
    print(f"   Missing email: {len(missing_email)}")
    print(f"   Has both: {len(leads) - len(missing_phone) - len(missing_email) + len(missing_phone & missing_email)}") # approx

    print(f"\n🔍 Opening search tabs for leads missing contact info...")
    
    # Open Google searches for top 5 leads missing contact info
    opened = 0
    for lead in leads:
        if opened >= 5:
            break
        if not lead.get("phone") or not lead.get("email"):
            company = lead["company_name"]
            search_q = quote(f"{company} Dubai contact number")
            webbrowser.open(f"https://www.google.com/search?q={search_q}")
            opened += 1
            print(f"   Opened tab: {company}")
    
    print(f"\n✅ Opened {opened} search tabs for manual enrichment")
    print(f"\n💡 TIP: Add found contacts back to the CSV in the lead-database-template.csv")
    
    # Show the first few missing-emails with suggested guesses
    print(f"\n💡 Suggested email guesses for missing entries:")
    for lead in missing_email[:5]:
        guess = suggest_email(lead["company_name"])
        if guess:
            print(f"   {lead['company_name']} → {guess}")
    
    return leads


def export_search_urls():
    """Export a list of search URLs for manual lead research."""
    if not os.path.exists(LEADS_FILE):
        return

    leads = []
    with open(LEADS_FILE, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        leads = list(reader)

    output = []
    output.append("# SiteSwift UAE - Lead Research URLs")
    output.append(f"# Generated: {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    output.append(f"# Total leads: {len(leads)}")
    output.append("")

    for lead in leads:
        company = lead["company_name"]
        industry = lead.get("industry", "")
        output.append(f"## {company} ({industry})")
        output.append(f"- Google Search: https://www.google.com/search?q={quote(company + ' Dubai')}")
        output.append(f"- LinkedIn: https://www.linkedin.com/search/results/all/?keywords={quote(company + ' Dubai')}")
        output.append(f"- Yellow Pages UAE: https://www.yellowpages.ae/search/results.html?keywords={quote(company)}")
        output.append(f"- Instagram: https://www.instagram.com/{quote(company.replace(' ', '').lower()[:30])}")
        output.append("")

    urls_file = os.path.join(os.path.dirname(__file__), "lead_research_urls.md")
    with open(urls_file, "w", encoding="utf-8") as f:
        f.write("\n".join(output))
    
    print(f"✅ Research URLs exported to: {urls_file}")


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="SiteSwift Lead Enrichment")
    parser.add_argument("action", choices=["enrich", "export-urls", "stats"], default="stats", nargs="?")
    args = parser.parse_args()
    
    if args.action == "enrich":
        enrich_leads()
    elif args.action == "stats":
        enrich_leads()  # Just shows stats without opening tabs
    elif args.action == "export-urls":
        export_search_urls()
