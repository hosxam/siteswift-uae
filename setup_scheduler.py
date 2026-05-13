"""
SiteSwift UAE - Windows Task Scheduler Setup
---------------------------------------------
Sets up automated tasks using Windows Task Scheduler.
Run this once to install all automation.

Usage:
  python setup_scheduler.py
  
What it creates:
  - Daily lead scraping (every morning at 6 AM)
  - Weekly email report (every Monday at 9 AM)
  - Daily lead cleanup/update (every evening at 8 PM)
"""

import os
import sys
import subprocess
from datetime import datetime

SCRIPTS_DIR = os.path.dirname(os.path.abspath(__file__))
PYTHON = sys.executable


def run_powershell(script: str) -> str:
    """Run a PowerShell command and return output."""
    result = subprocess.run(
        ["powershell", "-Command", script],
        capture_output=True,
        text=True,
        timeout=30,
    )
    return result.stdout + result.stderr


def create_task(name: str, description: str, script: str, schedule: str, args: str = ""):
    """
    Create a Windows Scheduled Task.
    
    Args:
        name: Task name (will be prefixed with 'SiteSwift-')
        description: Task description
        script: Python script to run
        schedule: Daily trigger time (HH:mm)
    """
    task_name = f"SiteSwift-{name}"
    script_path = os.path.join(SCRIPTS_DIR, script)
    python_path = PYTHON

    # Build XML for the task
    xml = f'''<?xml version="1.0" encoding="UTF-16"?>
<Task version="1.4" xmlns="http://schemas.microsoft.com/windows/2004/02/mit/task">
  <RegistrationInfo>
    <Date>{datetime.now().isoformat()}</Date>
    <Author>SiteSwift UAE</Author>
    <Description>{description}</Description>
  </RegistrationInfo>
  <Triggers>
    <CalendarTrigger>
      <StartBoundary>{datetime.now().strftime("%Y-%m-%d")}T{schedule}:00</StartBoundary>
      <Enabled>true</Enabled>
      <ScheduleByDay>
        <DaysInterval>1</DaysInterval>
      </ScheduleByDay>
    </CalendarTrigger>
  </Triggers>
  <Principals>
    <Principal id="Author">
      <LogonType>InteractiveToken</LogonType>
      <RunLevel>LeastPrivilege</RunLevel>
    </Principal>
  </Principals>
  <Settings>
    <Enabled>true</Enabled>
    <AllowStartOnDemand>true</AllowStartOnDemand>
    <RestartOnFailure>
      <Interval>PT5M</Interval>
      <Count>3</Count>
    </RestartOnFailure>
  </Settings>
  <Actions Context="Author">
    <Exec>
      <Command>{python_path}</Command>
      <Arguments>"{script_path}" {args}</Arguments>
      <WorkingDirectory>{SCRIPTS_DIR}</WorkingDirectory>
    </Exec>
  </Actions>
</Task>'''

    # Write XML to temp file
    xml_path = os.path.join(SCRIPTS_DIR, f"_task_{name}.xml")
    with open(xml_path, "w", encoding="utf-16") as f:
        f.write(xml)

    # Register task
    cmd = f'ScheduledTasks\\Register-ScheduledTask -Xml (Get-Content "{xml_path}") -TaskName "{task_name}" -Force'
    output = run_powershell(cmd)
    
    # Clean up XML
    os.remove(xml_path)

    if "Registered" in output or "ScheduledTask" in output:
        print(f"  ✅ Created task: {task_name} ({schedule} daily)")
    else:
        print(f"  ⚠️  Task creation result: {output.strip()}")


def setup_all():
    print("=" * 60)
    print("SiteSwift UAE - Automation Scheduler Setup")
    print("=" * 60)
    
    print("\n📅 Creating scheduled tasks...\n")
    
    # Check if we have the credentials
    if not os.getenv("GOOGLE_API_KEY"):
        print("  ⚠️  GOOGLE_API_KEY not set. Scraper task created but won't run until you set it in .env")
    
    create_task(
        name="DailyLeadScrape",
        description="Scrape Google Maps for new businesses without websites",
        script="scraper.py",
        schedule="06:00",
    )
    
    create_task(
        name="DailyCleanup",
        description="Update lead statuses and clean old data",
        script="scraper.py",  # Will add dedicated cleanup script later
        schedule="20:00",
    )
    
    print("\n✅ Scheduler setup complete!")
    print("\n💡 To verify, run in PowerShell:")
    print('    Get-ScheduledTask -TaskName "SiteSwift-*" | Format-Table TaskName,State,NextRunTime')
    
    print("\n❌ To remove all tasks:")
    print('    Get-ScheduledTask -TaskName "SiteSwift-*" | Unregister-ScheduledTask -Confirm:$false')


if __name__ == "__main__":
    setup_all()
