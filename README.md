# SBOM Compliance & Automation Demo

[![CI](https://github.com/havisha1411/sbom-automation-demo/actions/workflows/sbom-compliance.yml/badge.svg)](https://github.com/havisha1411/sbom-automation-demo/actions/workflows/sbom-compliance.yml)
![CycloneDX](https://img.shields.io/badge/SBOM-CycloneDX_v1.4-blue)
![Python](https://img.shields.io/badge/Python-3.11-blue)
![License](https://img.shields.io/badge/License-MIT-green)

---

## 🧭 Why This Project

This project was built to **demonstrate practical SBOM generation, validation, and vulnerability context handling** using real-world standards such as **CycloneDX**, **NTIA minimum SBOM elements**, and **VEX**, in a way that fits naturally into CI/CD workflows.

The focus is **not** on building a full security or compliance product, but on showing **how SBOM, VEX, and policy checks can be automated incrementally** in engineering teams — especially in regulated or compliance-aware environments.

---

## 📌 Project Scope (Important)

This repository is a **reference implementation and learning demo** intended to showcase:

- SBOM generation
- NTIA minimum elements validation
- VEX structure and validation
- Simple, policy-based decision logic

It is **not intended to replace enterprise SCA, SBOM, or vulnerability management tools**.  
The goal is to demonstrate **correct structure, automation patterns, and engineering thinking**, not to provide a production-ready security product.

---

## 🧩 Overview

This repository demonstrates a **Python-based SBOM and VEX automation workflow**, including:

- SBOM generation (CycloneDX v1.4)
- Validation against **NTIA minimum required elements**
- VEX creation and validation using structured input
- Simple policy enforcement based on severity and vulnerability state
- CI/CD-friendly execution via a single entry point

The project is intentionally **modular, readable, and scoped**, reflecting how such automation is typically introduced in real systems.

---

## ✨ Core Capabilities

| Capability | What It Demonstrates |
|-----------|---------------------|
| **SBOM Generation** | Automated creation of CycloneDX v1.4 SBOM using Python |
| **NTIA Validation** | Ensures SBOM contains required minimum elements (`name`, `version`, `supplier`, `purl`) |
| **VEX Handling** | Generation and validation of VEX statements from structured JSON input |
| **Policy Enforcement** | Severity × state decision logic aligned with NTIA/CISA guidance |
| **CI / DEV Modes** | Fail-fast behavior in CI, log-only behavior in development |
| **Automation Ready** | Single script (`run_demo.py`) suitable for CI/CD execution |

---

## 🏗 Architecture & Workflow

This project models a **realistic SBOM + VEX automation flow** commonly used in CI pipelines.

### High-Level Flow

```
Source Code / Dependencies
        ↓
SBOM Generation (CycloneDX)
        ↓
NTIA Minimum Elements Validation
        ↓
VEX Processing & Validation
        ↓
Policy Enforcement
        ↓
CI Pass / Warn / Fail
```

> This flow reflects how teams typically adopt SBOM and VEX checks step-by-step rather than all at once.

---

## 🚀 Getting Started

```bash
git clone https://github.com/havisha1411/sbom-automation-demo.git
cd sbom-automation-demo
```

### Set Up Virtual Environment

```bash
python -m venv .venv

# Windows
.venv\Scripts\activate

# Linux / macOS
source .venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run the Demo

```bash
# CI mode (fails on policy violations)
python run_demo.py

# DEV mode (logs violations but continues)
python run_demo.py --mode dev
```

---

## 📤 Example Output (Summary)

- CycloneDX SBOM generated successfully
- NTIA minimum required elements: **validated**
- VEX statements: **structurally valid**
- Policy result:
  - **PASS / WARN / FAIL** based on severity and vulnerability state

Console output provides a clear validation and policy summary suitable for CI logs.

---

## 📝 VEX Support (Clarified Scope)

- Vulnerabilities are provided via structured JSON input  
- VEX statements are generated and validated against SBOM components  
- Demonstrates:
  - Correct component referencing
  - Severity and vulnerability state handling
  - Policy-driven decision making

> This project **does not integrate live vulnerability feeds** and instead focuses on demonstrating correct structure, validation, and automation patterns.

---

## 📜 Regulatory & Industry Context

This project reflects **technical readiness patterns** relevant to:

- NTIA SBOM guidance  
- CycloneDX specification  
- EU Cyber Resilience Act (CRA) expectations (conceptual alignment)

It is **not a compliance product**, but demonstrates:
- SBOM availability
- Vulnerability context communication (VEX)
- Automated enforcement mechanisms suitable for CI/CD

---

## 🛠 Tools & Technologies

- **Python 3.11+**
- **CycloneDX Python Library**
- Standard libraries (`json`, `argparse`, `datetime`)
- GitHub Actions (CI demonstration)

---

## ✅ What This Project Intentionally Does / Does Not Do

**✔ Does**
- Generate and validate SBOMs
- Enforce NTIA-aligned minimum checks
- Demonstrate VEX structure and policy logic
- Run cleanly in CI/CD contexts

**✖ Does Not**
- Act as a full compliance or security scanning tool
- Integrate live CVE feeds
- Replace enterprise vulnerability management systems

This scope is intentional and documented.

---

## 🔜 Possible Extensions

- Integrate live vulnerability sources (NVD, PyPI advisories)
- Expand SBOM validation (licenses, suppliers, integrity)
- Generate machine-readable compliance reports
- Add unit tests for validation logic

---

## 📄 License

MIT License  
© 2026 Keerthana Raghavendra (havisha1411)