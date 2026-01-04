import json
import sys

FAIL = 1
WARN = 0

SEVERITY_ORDER = ["LOW", "MEDIUM", "HIGH", "CRITICAL"]

def severity_rank(sev):
    return SEVERITY_ORDER.index(sev)

def enforce_policy(vex_path):
    with open(vex_path, "r") as f:
        vex = json.load(f)

    failures = []
    warnings = []

    for vuln in vex.get("vulnerabilities", []):
        vid = vuln.get("id")
        severity = vuln.get("ratings", [{}])[0].get("severity", "LOW")
        analysis = vuln.get("analysis", {})
        state = analysis.get("state", "").lower()
        justification = analysis.get("justification", "").strip()

        sev_rank = severity_rank(severity)

        # --- NTIA / CISA POLICY LOGIC ---

        if state == "affected":
            if sev_rank >= severity_rank("MEDIUM"):
                failures.append(f"{vid} | {severity} | affected")
            else:
                warnings.append(f"{vid} | {severity} | affected (LOW allowed)")

            if not justification:
                failures.append(f"{vid} | missing justification")

        elif state == "under_investigation":
            if sev_rank >= severity_rank("MEDIUM"):
                failures.append(f"{vid} | {severity} | under investigation")
            else:
                warnings.append(f"{vid} | {severity} | under investigation")

        elif state in ("not_affected", "fixed"):
            continue

        else:
            failures.append(f"{vid} | unknown VEX state: {state}")

    # --- OUTPUT ---
    if warnings:
        print("⚠️ Policy Warnings:")
        for w in warnings:
            print(f" - {w}")

    if failures:
        print("❌ Policy Violations:")
        for f in failures:
            print(f" - {f}")
        sys.exit(FAIL)

    print("✅ Policy check passed (NTIA/CISA aligned)")

if __name__ == "__main__":
    enforce_policy("vex/vex.json")
