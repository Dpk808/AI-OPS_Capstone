
# AutoSec-Fix

Automated DevSecOps pipeline that detects:
- Code misconfigurations
- Dependency vulnerabilities
- Generates remediation suggestions

## How it works
1. Push code to GitHub
2. GitHub Actions runs scans
3. Fix suggestions generated
4. Security report produced

## Tools
- Bandit
- pip-audit
- GitHub Actions
