# SBOM Compliance & Automation Demo

[![CI](https://github.com/havisha1411/sbom-automation-demo/actions/workflows/sbom-compliance.yml/badge.svg)](https://github.com/havisha1411/sbom-automation-demo/actions/workflows/sbom-compliance.yml)
![CycloneDX](https://img.shields.io/badge/SBOM-CycloneDX_v1.4-blue)
![Python](https://img.shields.io/badge/Python-3.11-blue)
![License](https://img.shields.io/badge/License-MIT-green)


## 🧩 Overview

Public GitHub project demonstrating **SBOM generation, NTIA validation, VEX handling, and Python-based automation**, integrated with CI/CD workflows on an open-source application.

### Core Features

| Feature | Description |
|---------|------------|
| **SBOM Generation** | Python automation using `cyclonedx-bom` (CycloneDX v1.4) |
| **NTIA Validation** | Ensures SBOM includes `name`, `version`, `supplier`, `purl` |
| **VEX Handling** | Automates creation & validation of VEX statements from JSON input |
| **Automation / CI/CD** | Single `run_demo.py` script executes all steps |


## 🏗 Architecture

![SBOM Automation Architecture](docs/sbom_architecture.png)

> Workflow: Source code → SBOM generation → NTIA validation → vuln_input.json → VEX generation → VEX validation → CI/CD pipeline.


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
python run_demo.py
```

**Outputs:**

- `sbom/sbom.json` → Generated SBOM  
- `vex/vex.json` → Generated VEX


## 📝 VEX Support

- Reads vulnerabilities from `vex/vuln_input.json`  
- Generates VEX statements mapping vulnerabilities to SBOM components  
- Validates that VEX references exist in the SBOM  
- Demonstrates automated vulnerability response workflow even without a live vulnerability scanner.


## 📜 Regulatory Context

- Aligns with **EU Cyber Resilience Act (CRA)** practices  
- Not a legal compliance tool, but demonstrates **technical readiness**:  
  - SBOM availability  
  - Vulnerability disclosure transparency  
  - Clear vulnerability impact communication


## 🛠 Tools & Libraries

- CycloneDX Python Library – SBOM generation  
- Python 3.11+  
- Standard libraries: `json`, `datetime`


## ✅ Compliance Checks

- SBOM generation (CycloneDX v1.4)  
- NTIA minimal element validation (`name`, `version`, `supplier`, `purl`)  
- VEX generation & validation


## 💡 Notes

- Components include **dependencies only**, not the application itself  
- VEX is **simulated** using JSON input list of known vulnerabilities  
- Designed to be **CI/CD friendly** for automated SBOM and VEX compliance checks


## 🔜 Next Steps

- Integrate with real-world vulnerability feeds (e.g., **NVD**, **PyPI advisories**)  
- Expand SBOM validations for **licensing and supply chain risks**  
- Extend VEX mapping to multiple dependencies and ecosystems


## 📄 License

**MIT** – © 2026 Keerthana Raghavendra / havisha1411

