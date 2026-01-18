from pathlib import Path
import yaml
import json

# Ensure reports directory exists
reports_dir = Path("reports")
reports_dir.mkdir(parents=True, exist_ok=True)

fixes = yaml.safe_load(open("remediation/fixes.yaml"))
report = []

bandit_report = reports_dir / "bandit.json"
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

dep_report = reports_dir / "deps.txt"
if dep_report.exists():
    for line in dep_report.read_text().splitlines():
        if "CVE" in line:
            report.append({
                "type": "Dependency",
                "issue": line.strip(),
                "solution": "Upgrade to secure version"
            })

# Write final security report
security_report = reports_dir / "security_report.md"
security_report.write_text(
    "# Security Report\n\n" +
    "\n".join(
        f"- **{r['type']}**: {r['issue']} → {r['solution']}"
        for r in report
    )
)

print("✅ Security report generated successfully")
