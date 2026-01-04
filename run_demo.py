# run_demo.py
"""
SBOM Compliance & Automation Demo - End-to-End Runner

This script runs the full demo:
1. Generate SBOM
2. Validate SBOM (NTIA minimal elements)
3. Generate VEX from vuln_input.json
4. Validate VEX against SBOM
5. Enforce security policy (dev / ci mode)

Usage:
    python run_demo.py --mode dev
    python run_demo.py --mode ci
"""

import argparse

from scripts.generate_sbom import generate_sbom
from scripts.validate_ntia import validate_ntia
from scripts.generate_vex import generate_vex
from scripts.validate_vex import validate_vex
from scripts.policy_check import enforce_policy


def run_demo():
    parser = argparse.ArgumentParser(description="SBOM Compliance Automation Demo")
    parser.add_argument(
        "--mode",
        choices=["dev", "ci"],
        default="ci",
        help="Policy enforcement mode (default: ci)"
    )
    args = parser.parse_args()

    print("\n=== SBOM Compliance & Automation Demo ===")
    print(f"Running in {args.mode.upper()} mode\n")

    # Step 1: Generate SBOM
    print("Step 1: Generating SBOM...")
    generate_sbom()
    print("SBOM generated at sbom/sbom.json\n")

    # Step 2: Validate SBOM (NTIA minimal elements)
    print("Step 2: Validating SBOM (NTIA minimal elements)...")
    validate_ntia("sbom/sbom.json")
    print("")

    # Step 3: Generate VEX
    print("Step 3: Generating VEX from vuln_input.json...")
    generate_vex("vex/vuln_input.json", "vex/vex.json")
    print("VEX generated at vex/vex.json\n")

    # Step 4: Validate VEX against SBOM
    print("Step 4: Validating VEX against SBOM...")
    validate_vex("vex/vex.json", "sbom/sbom.json")
    print("")

    # Step 5: Enforce security policy
    print("Step 5: Enforcing security policy...")
    enforce_policy("vex/vex.json", mode=args.mode)

    print("\nAll steps completed successfully!")


if __name__ == "__main__":
    run_demo()
