# Chef's Corner - Security Assessment

## Overview

This repository contains the results of a security assessment conducted on the Chef's Corner web application, a recipe sharing platform developed by a boutique restaurant group.

**Objective:** Determine if an attacker could access the proprietary "Secret Sauce" recipe.

**Assessment Type:** Black-Box Security Assessment (External Penetration Test)

**Date:** July 2026

**Assessor:** Stefan Krijt

---

## Key Findings

| Severity | Finding | CVSS |
|----------|---------|------|
| Critical | JWT Private Key Exposed in Public Repository | 9.1 |
| Critical | Encryption Key Exposed in Commit History | 9.1 |
| Critical | Hardcoded Admin Credentials | 9.1 |
| High | Hardcoded Server Seed in Source Code | 7.5 |
| Medium | Client-Side Server Seed Disclosure | 5.3 |
| Medium | Development Comments in Production | 5.3 |

**Proof of Concept:** The secret recipe was successfully extracted and is no longer confidential.

---

## Repository Contents

| File | Description |
|------|-------------|
| `Chefs_Corner_Security_Assessment_Report.pdf` | Full security assessment report (methodology, findings, PoC, recommendations) |
| `scripts/forge_jwt.py` | JWT forgery script using exposed private key |
| `scripts/decrypt_recipe.py` | Recipe decryption script using exposed encryption key |
| `scripts/recipe_id_calculator.js` | Recipe ID calculation script (SHA256) |
| `requirements.txt` | Python dependencies for scripts |

---

## Methodology

| Phase | Activity |
|-------|----------|
| 1. Reconnaissance | Manual exploration of the web application; discovered GitHub repository |
| 2. Source Code Analysis | Reviewed `app.py`, `keys/`, commit history, and `.gitignore` |
| 3. Vulnerability Identification | Identified cryptographic weaknesses, hardcoded secrets, and information disclosure |
| 4. Exploitation | Forged JWT token, extracted server seed, calculated recipe ID, decrypted recipe |
| 5. Reporting | Comprehensive documentation of findings with remediation recommendations |

---

## Attack Chain Summary

```
Reconnaissance (F-05 + F-06)
         ↓
JWT Private Key Exposed (F-01) ────────┐
         ↓                               │
Hardcoded Server Seed (F-04) ───────────┤
         ↓                               │
Hardcoded Admin Creds (F-03) ───────────┤
         ↓                               │
   JWT Forgery ──────────────────────────┤
         ↓                               │
   Extract Real Seed (F-01 + F-04) ──────┤
         ↓                               │
   Calculate Recipe ID (F-04) ───────────┤
         ↓                               │
   Retrieve Encrypted Recipe ────────────┤
         ↓                               │
Encryption Key Exposed (F-02) ───────────┘
         ↓
   Decrypt Recipe
         ↓
   FINAL: Secret Recipe Extracted
```

---

## Tools Used

| Tool | Purpose |
|------|---------|
| Firefox Developer Tools | Page inspection, debugging, source review |
| GitHub | Source code and commit history analysis |
| Python | JWT forgery, cryptographic decryption |
| curl | API testing and validation |

---

## Requirements

To run the scripts in this repository:

```bash
pip install -r requirements.txt
```

**requirements.txt:**
```
PyJWT==2.8.0
cryptography==41.0.7
```

---

## Important Disclaimers

### Educational Context

This repository documents a security assessment conducted on an **educational lab environment** as part of a school project. The assessment was performed with:

- Explicit authorization from the system owner
- Written consent to test and document findings
- Prior approval to share results for portfolio purposes

All findings, screenshots, and data contained in this report are from this controlled lab environment only. No live production systems were tested, and no real-world sensitive data was accessed.

### No Live Systems

The vulnerabilities identified in this report exist only in the designated educational lab environment. Do not attempt to test these techniques against systems without proper authorization.

### Professional Context

In real-world engagements, penetration test reports are **confidential** and should never be shared publicly. This exception exists solely because this was an authorized educational exercise.

---

## License

This repository contains both code and a report, each with separate licensing:

- **Scripts** (`*.py`, `*.js`): MIT License
- **Report** (`*.pdf`): All Rights Reserved / Educational Use Only

See the [LICENSE](LICENSE) file for full details.

---

## Disclaimer

> **WARNING:** The techniques documented in this repository are for educational purposes only. Unauthorized testing of systems is illegal. Only test systems you own or have explicit permission to test.

---

## Contact

**Author:** Stefan Krijt  
**Date:** July 2026  
**Purpose:** Educational Portfolio / School Project

---

*This repository is part of a school project and is shared for educational and portfolio purposes only.*
