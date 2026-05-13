
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

const SITESWIFT_LEADS = [
  {
    "name": "GFTeam Dubai",
    "handle": "gfteam",
    "url": "https://www.instagram.com/gfteam/"
  },
  {
    "name": "Wellfit Marina",
    "handle": "wellfit",
    "url": "https://www.instagram.com/wellfit/"
  },
  {
    "name": "Prime Fitness Dubai Marina",
    "handle": "primefitness",
    "url": "https://www.instagram.com/primefitness/"
  },
  {
    "name": "PRIME FITNESS MARINA 2",
    "handle": "primefitness2",
    "url": "https://www.instagram.com/primefitness2/"
  },
  {
    "name": "The Marina Gym-24 hours",
    "handle": "thegym24hours",
    "url": "https://www.instagram.com/thegym24hours/"
  },
  {
    "name": "SWT ARENA FITNESS",
    "handle": "swtarenafitness",
    "url": "https://www.instagram.com/swtarenafitness/"
  },
  {
    "name": "Abooz Cafe - JBR",
    "handle": "aboozcafe",
    "url": "https://www.instagram.com/aboozcafe/"
  },
  {
    "name": "Arabian Cave Cafe Letizia",
    "handle": "arabiancavecafeletizia",
    "url": "https://www.instagram.com/arabiancavecafeletizia/"
  },
  {
    "name": "Risen Cafe Marina",
    "handle": "risencafe",
    "url": "https://www.instagram.com/risencafe/"
  },
  {
    "name": "Nargileci Eleven Cafe",
    "handle": "nargilecielevencafe",
    "url": "https://www.instagram.com/nargilecielevencafe/"
  },
  {
    "name": "Brow Studio Dubai",
    "handle": "browstudio",
    "url": "https://www.instagram.com/browstudio/"
  },
  {
    "name": "Gladys Beauty Saloon - Marina",
    "handle": "gladysbeautysaloon",
    "url": "https://www.instagram.com/gladysbeautysaloon/"
  },
  {
    "name": "Eleven Signature Beauty Salon",
    "handle": "elevensignaturebeautysalon",
    "url": "https://www.instagram.com/elevensignaturebeautysalon/"
  },
  {
    "name": "Wide Star Beauty Salon",
    "handle": "widestarbeautysalon",
    "url": "https://www.instagram.com/widestarbeautysalon/"
  },
  {
    "name": "Kate White Ladies Beauty Salon",
    "handle": "katewhiteladiesbeautysalon",
    "url": "https://www.instagram.com/katewhiteladiesbeautysalon/"
  },
  {
    "name": "PERSONA Image Lab Dubai",
    "handle": "personaimagelab",
    "url": "https://www.instagram.com/personaimagelab/"
  },
  {
    "name": "Lifestyle Hair Care Clinic",
    "handle": "lifestylehaircareclinic",
    "url": "https://www.instagram.com/lifestylehaircareclinic/"
  },
  {
    "name": "The lost Restaurant and Specialty coffee",
    "handle": "thelostrestaurantandspecialtyc",
    "url": "https://www.instagram.com/thelostrestaurantandspecialtyc/"
  },
  {
    "name": "Cafe Society Dubai",
    "handle": "cafesociety",
    "url": "https://www.instagram.com/cafesociety/"
  },
  {
    "name": "Common Grounds JBR",
    "handle": "commongrounds",
    "url": "https://www.instagram.com/commongrounds/"
  },
  {
    "name": "Prime Physiotherapy Center",
    "handle": "primephysiotherapycenter",
    "url": "https://www.instagram.com/primephysiotherapycenter/"
  },
  {
    "name": "Al Manara Medical Fitness",
    "handle": "almanaramedicalfitness",
    "url": "https://www.instagram.com/almanaramedicalfitness/"
  }
];

function siteswift_dm_list() {
    console.log('📋 SiteSwift UAE - Leads for DM Outreach');
    console.log('=========================================');
    console.log(`Total: ${SITESWIFT_LEADS.length} leads`);
    console.log('');
    
    SITESWIFT_LEADS.forEach((lead, i) => {
        console.log(`${i + 1}. @${lead.handle} - ${lead.name}`);
    });
    
    console.log('');
    console.log('💡 Open leads in new tabs:');
    console.log('   SITESWIFT_LEADS.forEach(l => window.open(l.url, "_blank"));');
    console.log('   Then send DMs manually (IG rate limits ~10-15 DMs/day)');
}

// Auto-run on paste
siteswift_dm_list();
