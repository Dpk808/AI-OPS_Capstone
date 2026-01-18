
import yaml
import json
from pathlib import Path

fixes = yaml.safe_load(open("remediation/fixes.yaml"))
report = []

bandit_report = Path("reports/bandit.json")
if bandit_report.exists():
    data = json.load(open(bandit_report))
    for issue in data.get("results", []):
        code = issue.get("test_id")
        if code in fixes:
            report.append({
                "type": "Code",
                "issue": fixes[code]["issue"],
                "solution": fixes[code]["fix"]
            })

dep_report = Path("reports/deps.txt")
if dep_report.exists():
    for line in dep_report.read_text().splitlines():
        if "CVE" in line:
            report.append({
                "type": "Dependency",
                "issue": line,
                "solution": "Upgrade to secure version"
            })

Path("reports/security_report.md").write_text(
    "# Security Report\n\n" +
    "\n".join(f"- **{r['type']}**: {r['issue']} → {r['solution']}" for r in report)
)

print("Security report generated")
