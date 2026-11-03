import subprocess
import os

CHROME = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
ARTIFACT_DIR = r"C:\Users\siddi\.gemini\antigravity\brain\4dd10c7b-bb97-46d2-a619-344ea8415c35"

# We can capture light mode by loading page with a tiny wrapper or setting theme via script
script_light = """
const script = document.createElement('script');
script.textContent = "document.documentElement.setAttribute('data-theme', 'light');";
document.head.appendChild(script);
"""

# Let's also capture the case study body (wireframes, persona, outcome)
dest_body = os.path.join(ARTIFACT_DIR, "preview_uiux_case_study_body.png")
cmd_body = [
    CHROME,
    "--headless=new",
    "--disable-gpu",
    "--hide-scrollbars",
    "--window-size=1440,1200",
    f"--screenshot={dest_body}",
    "--virtual-time-budget=2000",
    "http://127.0.0.1:5500/case-study.html"
]
subprocess.run(cmd_body, timeout=20)
print("Captured case study body:", os.path.exists(dest_body))
