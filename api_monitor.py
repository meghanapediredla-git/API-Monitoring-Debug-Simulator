# ==========================================================
# PROJECT: API Monitoring & Debug Simulator
# AUTHOR: Meghana Pediredla
# DATE: Dec 2025 – Jan 2026
# DESCRIPTION:
#   Python tool that monitors multiple REST API endpoints,
#   logs their responses, detects repeated failures,
#   and simulates alerts — mimicking how real product
#   support or SRE teams debug API reliability issues.
# ==========================================================

# ---------- IMPORTS ----------
import requests                 # For sending HTTP requests
import time                     # For adding readable timestamps
from collections import defaultdict  # For tracking failure counts

# ---------- CONFIGURATION ----------
# List of APIs to monitor (some good, some intentionally failing)
api_endpoints = [
    "https://jsonplaceholder.typicode.com/posts",       # Expected 200 OK
    "https://jsonplaceholder.typicode.com/invalid",     # Expected 404 Not Found
    "https://httpbin.org/status/500"                    # Expected 500 Server Error
]

# File where logs are stored
log_file = "api_log.txt"

# Dictionary to count consecutive failures for each API
failures = defaultdict(int)

# ---------- FUNCTIONS ----------
def log_message(message):
    """Write a message to the log file using UTF-8 encoding."""
    with open(log_file, "a", encoding="utf-8") as file:
        file.write(message + "\n")

def send_alert(url, code):
    """Simulate alert generation when an API fails repeatedly."""
    alert = f"⚠️ ALERT: {url} failed repeatedly with status code {code}"
    print(alert)
    log_message(alert)

def check_api(url):
    """Send a GET request, log result, and track failure trends."""
    try:
        # Send request
        response = requests.get(url, timeout=5)
        code = response.status_code
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S")

        # Log response
        log_line = f"[{timestamp}] {url} -> Status: {code}"
        print(log_line)
        log_message(log_line)

        # Count and alert on failures
        if code in [400, 403, 404, 500]:
            failures[url] += 1
            if failures[url] >= 3:
                send_alert(url, code)
        else:
            failures[url] = 0  # reset if recovered

    except requests.exceptions.RequestException as e:
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
        error_line = f"[{timestamp}] {url} -> ERROR: {e}"
        print(error_line)
        log_message(error_line)

# ---------- MAIN LOOP ----------
print("\n🚀 Starting API Monitoring...")
for cycle in range(5):
    print(f"\n🔁 Cycle {cycle + 1}: Checking all APIs...")
    for api in api_endpoints:
        check_api(api)
    time.sleep(2)  # small pause between cycles

print("\n✅ Monitoring completed. Check 'api_log.txt' for logs.")
