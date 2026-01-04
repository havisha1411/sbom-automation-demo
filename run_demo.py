# run_demo.py
"""
SBOM Compliance & Automation Demo - End-to-End Runner

This script runs the full demo:
1. Generate SBOM
2. Validate SBOM (NTIA minimal elements)
3. Generate VEX from vuln_input.json
4. Validate VEX against SBOM

Usage:
    python run_demo.py
"""

# run_demo.py
from scripts.generate_sbom import generate_sbom
from scripts.validate_ntia import validate_ntia
from scripts.generate_vex import generate_vex
from scripts.validate_vex import validate_vex
from scripts.policy_check import enforce_policy

def run_demo():
    print("\n=== SBOM Compliance & Automation Demo ===\n")

    # Step 1: Generate SBOM
    print("Step 1: Generating SBOM...")
    generate_sbom()
    print("SBOM generated at sbom/sbom.json\n")

    # Step 2: Validate SBOM (NTIA minimal elements)
    print("Step 2: Validating SBOM (NTIA minimal elements)...")
    validate_ntia("sbom/sbom.json")
    print("")  # just a blank line for spacing

    # Step 3: Generate VEX
    print("Step 3: Generating VEX from vuln_input.json...")
    generate_vex("vex/vuln_input.json", "vex/vex.json")
    print("VEX generated at vex/vex.json\n")

    # Step 4: Validate VEX against SBOM
    print("Step 4: Validating VEX against SBOM...")
    validate_vex("vex/vex.json", "sbom/sbom.json")
    print("")  # blank line for spacing

    print("\nStep 5: Enforcing security policy...")
    from scripts.policy_check import enforce_policy
    enforce_policy("vex/vex.json")

    print("All steps completed successfully!")

if __name__ == "__main__":
    run_demo()
