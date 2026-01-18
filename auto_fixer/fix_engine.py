from pathlib import Path
import yaml
import json

# Ensure reports directory exists
reports_dir = Path("reports")
reports_dir.mkdir(parents=True, exist_ok=True)

# Load remediation rules
fixes = yaml.safe_load(open("remediation/fixes.yaml"))
report_items = []

# --- Bandit ---
bandit_report = reports_dir / "bandit.json"
if bandit_report.exists():
    data = json.load(open(bandit_report))
    for issue in data.get("results", []):
        test_id = issue.get("test_id")
        fix = fixes.get(test_id, {}).get("fix", "Review and fix manually")
        report_items.append({
            "type": "Code",
            "file": issue.get("filename"),
            "line": issue.get("line_number"),
            "issue": issue.get("issue_text"),
            "fix": fix
        })

# --- Dependencies ---
dep_report = reports_dir / "deps.txt"
if dep_report.exists():
    for line in dep_report.read_text().splitlines():
        if "CVE" in line:
            report_items.append({
                "type": "Dependency",
                "file": "-",
                "line": "-",
                "issue": line.strip(),
                "fix": "Upgrade to a secure version"
            })

# Write human-readable Markdown report
report_path = reports_dir / "full_security_report.md"
with report_path.open("w") as f:
    f.write("# Full Security Report\n\n")
    for item in report_items:
        f.write(f"### {item['type']} Issue\n")
        f.write(f"- **File:** {item['file']}\n")
        f.write(f"- **Line:** {item['line']}\n")
        f.write(f"- **Issue:** {item['issue']}\n")
        f.write(f"- **Suggested Fix:** {item['fix']}\n\n")

print("✅ Full human-readable security report generated at reports/full_security_report.md")
