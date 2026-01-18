
import json
import subprocess

result = subprocess.run(
    ["bandit", "-r", "app", "-f", "json", "-o", "reports/bandit.json"],
    capture_output=True
)

print("Bandit scan completed")
