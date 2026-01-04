# SBOM Compliance & Automation Demo


[![CI](https://github.com/havisha1411/sbom-automation-demo/actions/workflows/sbom-compliance.yml/badge.svg)](https://github.com/havisha1411/sbom-automation-demo/actions/workflows/sbom-compliance.yml)
![CycloneDX](https://img.shields.io/badge/SBOM-CycloneDX_v1.4-blue)
![Python](https://img.shields.io/badge/Python-3.11-blue)
![License](https://img.shields.io/badge/License-MIT-green)



## 🧩 Overview

Public GitHub project demonstrating **SBOM generation, NTIA validation, VEX handling, Python-based automation, and policy enforcement**, integrated with CI/CD workflows on an open-source application.


### Core Features

| Feature | Description |
|---------|------------|
| **SBOM Generation** | Python automation using `cyclonedx-bom` (CycloneDX v1.4) |
| **NTIA Validation** | Ensures SBOM includes `name`, `version`, `supplier`, `purl` |
| **VEX Handling** | Automates creation & validation of VEX statements from JSON input |
| **Policy Enforcement** | Applies NTIA/CISA-aligned policy based on severity & state (CI & DEV modes) |
| **Automation / CI/CD** | Single `run_demo.py` script executes all steps, CI/CD pipeline ready |



## 🏗 Architecture

This project demonstrates a **practical SBOM + VEX automation workflow** designed for CI/CD environments.

### High-Level Flow

1. **SBOM Generation**
   - Generates a CycloneDX v1.4 SBOM from Python dependencies
   - Ensures consistent, machine-readable component inventory

2. **NTIA Validation**
   - Validates presence of NTIA minimum required fields  
     (`name`, `version`, `supplier`, `purl`)
   - Fails early if SBOM is incomplete

3. **VEX Generation**
   - Reads vulnerability data from `vex/vuln_input.json`
   - Produces CycloneDX VEX statements mapped to SBOM components

4. **VEX Validation**
   - Ensures all VEX entries reference valid SBOM components
   - Prevents orphaned or incorrect vulnerability claims

5. **Policy Enforcement**
   - Applies severity × state decision matrix (NTIA / CISA aligned)
   - Supports **CI mode** (fail pipeline) and **DEV mode** (log-only)
   - Outputs a clear policy summary (pass / warn / fail)

6. **CI/CD Integration**
   - Entire workflow executed via a single entry point: `run_demo.py`
   - GitHub Actions pipeline enforces policies automatically on every run

> The architecture is a simple and modular way to reflect how SBOM, VEX, and policy checks are typically introduced incrementally in real-world engineering teams.




## 🔧 Getting Started

```bash
git clone https://github.com/havisha1411/sbom-automation-demo.git
cd sbom-automation-demo
```

### Virtual Environment

```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
# Linux / Mac
source .venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Demo

```bash
# Default CI mode
python run_demo.py

# DEV mode (warnings logged but build continues)
python run_demo.py --mode dev
```

**Outputs:**

- `sbom/sbom.json` → Generated SBOM  
- `vex/vex.json` → Generated VEX  
- Policy enforcement output printed in console (violations & summary)



## 📝 VEX Support

- Reads vulnerabilities from `vex/vuln_input.json`  
- Generates VEX statements mapping vulnerabilities to SBOM components  
- Validates that VEX references exist in the SBOM  
- Policy enforcement aligns with NTIA/CISA recommendations:  
  - Severity + state matrix applied (LOW allowed in certain cases, MEDIUM+ must be flagged)  
  - Missing justification or unknown states are flagged  
  - Policy summary shows count by severity  
- Supports **CI mode** (pipeline fails on violations) and **DEV mode** (violations logged but build continues)  
- Demonstrates automated vulnerability response workflow even without a live vulnerability scanner.


## 📜 Regulatory Context

- Aligns with **EU Cyber Resilience Act (CRA)** practices  
- Not a legal compliance tool, but demonstrates **technical readiness**:  
  - SBOM availability  
  - Vulnerability disclosure transparency  
  - Clear vulnerability impact communication  
- Can be adapted for Swiss/EU organizational guidelines


## 🛠 Tools & Libraries

- CycloneDX Python Library – SBOM generation  
- Python 3.11+  
- Standard libraries: `json`, `datetime`



## ✅ Compliance Checks

- SBOM generation (CycloneDX v1.4)  
- NTIA minimal element validation (`name`, `version`, `supplier`, `purl`)  
- VEX generation & validation  
- Policy enforcement with **severity + state matrix**, CI/DEV modes, and summary output


## 💡 Notes

- Components include **dependencies only**, not the application itself  
- VEX is **simulated** using JSON input list of known vulnerabilities  
- Designed to be **CI/CD friendly** for automated SBOM, VEX, and policy compliance checks  
- Policy summary improves visibility of security posture for reviewers


## 🔜 Next Steps

- Integrate with real-world vulnerability feeds (e.g., **NVD**, **PyPI advisories**)  
- Expand SBOM validations for **licensing and supply chain risks**  
- Extend VEX mapping to multiple dependencies and ecosystems  
- Add automated report generation for policy violations (CSV/JSON) for auditing



## 📄 License

**MIT** – © 2026 Keerthana Raghavendra / havisha1411

