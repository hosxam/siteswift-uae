"""
SiteSwift UAE - Lead Scraper for Google Maps
----------------------------------------------
Searches Google Maps for businesses WITHOUT websites using the Google Places API.
This is a free-tier compatible tool. It uses Google Places API Newbie credits ($200/mo free).

Usage:
  1. Get a Google Places API key from https://console.cloud.google.com/
  2. Set the key in .env (GOOGLE_API_KEY)
  3. Run: python scraper.py

The script checks each business for a website and flags those without one as hot leads.
"""

import os
import csv
import json
import time
import requests
from datetime import datetime
from typing import List, Dict, Optional

# Try loading .env
try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass  # No dotenv installed, that's fine

API_KEY = os.getenv("GOOGLE_API_KEY", "")
OUTPUT_FILE = os.path.join(os.path.dirname(__file__), "lead-database-template.csv")

# Industries to search — each one will be a separate search query
INDUSTRIES = [
    "gyms in Dubai Marina",
    "beauty salons in Dubai Marina", 
    "cafes in Dubai Marina",
    "dentists in Dubai Marina",
    "physiotherapy in Dubai Marina",
    "personal trainers in Dubai Marina",
    "barber shops in Dubai Marina",
    "restaurants no website Dubai",
    "yoga studios in Dubai Marina",
    "car repair Dubai Marina",
    "cleaning services Dubai Marina",
    "real estate offices Dubai Marina",
    "photography studios Dubai Marina",
    "tailors in Dubai Marina",
    "furniture repair Dubai Marina",
    "pet grooming Dubai Marina",
    "tutoring centers Dubai Marina",
    "laundry services Dubai Marina",
    "spa in Dubai Marina",
    "opticians in Dubai Marina",
]


def places_text_search(query: str, api_key: str) -> List[Dict]:
    """Search Google Places API using a text query. Returns places with basic info."""
    url = "https://maps.googleapis.com/maps/api/place/textsearch/json"
    results = []
    page_token = None

    for page in range(3):  # Max 3 pages (60 results) per query
        params = {
            "query": query,
            "key": api_key,
            "region": "ae",
            "language": "en",
        }
        if page_token:
            params["pagetoken"] = page_token

        resp = requests.get(url, params=params, timeout=15)
        data = resp.json()

        if data.get("status") != "OK":
            print(f"  API error: {data.get('status')} - {data.get('error_message', '')}")
            break

        results.extend(data.get("results", []))
        page_token = data.get("next_page_token")
        if not page_token:
            break
        time.sleep(2)  # Required: Google needs 2s delay before pagetoken works

    return results


def get_place_details(place_id: str, api_key: str) -> Optional[Dict]:
    """Fetch full details for a single place to check for website and phone."""
    url = "https://maps.googleapis.com/maps/api/place/details/json"
    params = {
        "place_id": place_id,
        "fields": "name,formatted_phone_number,international_phone_number,website,formatted_address,rating,user_ratings_total,opening_hours,types,price_level",
        "key": api_key,
    }

    try:
        resp = requests.get(url, params=params, timeout=10)
        data = resp.json()
        if data.get("status") == "OK":
            return data.get("result")
    except Exception as e:
        print(f"  Error fetching details: {e}")
    return None


def score_lead(details: Dict, industry: str) -> int:
    """
    Score a lead from 0-100 based on how likely they need a website.
    Higher = better lead.
    """
    score = 50  # Baseline

    name = details.get("name", "")
    rating = details.get("rating", 0)
    ratings_count = details.get("user_ratings_total", 0)
    has_website = bool(details.get("website"))
    has_phone = bool(details.get("international_phone_number") or details.get("formatted_phone_number"))

    # Major signal: no website = needs one
    if not has_website:
        score += 30
    else:
        score -= 20

    # Has good ratings but no site => invested in business but missing online presence
    if rating >= 4.0 and not has_website:
        score += 10
    if ratings_count > 20 and not has_website:
        score += 5

    # Has a phone number (reachable)
    if has_phone:
        score += 5

    # Avoid chains/franchises (they usually have websites)
    chain_keywords = ["branch", "by ", "official", "fitness first", "gold's gym"]
    name_lower = name.lower()
    for kw in chain_keywords:
        if kw in name_lower:
            score -= 15
            break

    # Small biz indicators: no price level = more likely small
    if "price_level" not in details:
        score += 5

    return min(max(score, 0), 100)


def scrape_all():
    """Main scraper: searches all industries, checks websites, writes CSV."""
    if not API_KEY:
        print("❌ No GOOGLE_API_KEY found! Set it in .env or export it.")
        print("   Get one at: https://console.cloud.google.com/apis/credentials")
        return

    print("=" * 60)
    print("SiteSwift UAE - Lead Scraper")
    print(f"Starting at: {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    print("=" * 60)

    all_leads = []
    api_calls = 0

    for industry in INDUSTRIES:
        print(f"\n🔍 Searching: {industry}")
        try:
            places = places_text_search(f"{industry} UAE", API_KEY)
            api_calls += 1
            print(f"   Found {len(places)} places")

            for place in places:
                place_id = place.get("place_id")
                if not place_id:
                    continue

                details = get_place_details(place_id, API_KEY)
                api_calls += 1

                if not details:
                    continue

                score = score_lead(details, industry)
                has_website = bool(details.get("website"))
                website_status = "Has website" if has_website else "🔥 No website"

                if not has_website:
                    lead = {
                        "company_name": details.get("name", "Unknown"),
                        "industry": industry.split(" in ")[0].strip(),
                        "contact_name": "",
                        "email": "",
                        "phone": details.get("international_phone_number", details.get("formatted_phone_number", "")),
                        "website_status": website_status,
                        "lead_source": "Google Maps",
                        "date_added": datetime.now().strftime("%Y-%m-%d"),
                        "status": "New",
                        "notes": f"Rating: {details.get('rating', 'N/A')} ({details.get('user_ratings_total', 0)} reviews). Score: {score}/100.",
                        "score": score,
                        "address": details.get("formatted_address", ""),
                    }
                    all_leads.append(lead)

                # Small delay to avoid rate limiting
                time.sleep(0.2)

        except Exception as e:
            print(f"   ❌ Error searching {industry}: {e}")

        # Rate limit: max 5 queries per second
        time.sleep(1)

    # Sort by score (highest first)
    all_leads.sort(key=lambda x: x.get("score", 0), reverse=True)

    # Write CSV
    fieldnames = [
        "company_name", "industry", "contact_name", "email", "phone",
        "website_status", "lead_source", "date_added", "status", "notes",
        "score", "address",
    ]

    with open(OUTPUT_FILE, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(all_leads)

    print("\n" + "=" * 60)
    print(f"✅ Done! Scraped {len(all_leads)} leads without websites.")
    print(f"   API calls made: {api_calls}")
    print(f"   Output: {OUTPUT_FILE}")
    print("=" * 60)


if __name__ == "__main__":
    scrape_all()
