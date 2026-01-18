
import subprocess

subprocess.run(
    ["pip-audit", "-r", "app/requirements.txt", "-o", "reports/deps.txt"],
    check=False
)

print("Dependency scan completed")
