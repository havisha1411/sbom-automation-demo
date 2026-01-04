import json
import sys

FAIL = 1
WARN = 0

SEVERITY_ORDER = ["LOW", "MEDIUM", "HIGH", "CRITICAL"]

def severity_rank(sev):
    return SEVERITY_ORDER.index(sev)

def enforce_policy(vex_path, mode="ci"):
    with open(vex_path, "r") as f:
        vex = json.load(f)

    failures = []
    warnings = []

    # --- Policy summary counter ---
    summary = {sev: 0 for sev in SEVERITY_ORDER}

    for vuln in vex.get("vulnerabilities", []):
        vid = vuln.get("id")
        severity = vuln.get("ratings", [{}])[0].get("severity", "LOW")
        analysis = vuln.get("analysis", {})
        state = analysis.get("state", "").lower()
        justification = analysis.get("justification", "").strip()

        summary[severity] += 1
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

    # --- POLICY SUMMARY ---
    print("\nPolicy Summary:")
    for sev in ["CRITICAL", "HIGH", "MEDIUM", "LOW"]:
        count = summary[sev]
        if count > 0:
            print(f" - {sev}: {count}")

    # --- OUTPUT ---
    if warnings:
        print("\nPolicy Warnings:")
        for w in warnings:
            print(f" - {w}")

    if failures:
        print("\nPolicy Violations:")
        for f in failures:
            print(f" - {f}")

        if mode == "ci":
            print("\nCI mode: Pipeline failed, policy violated")
            sys.exit(FAIL)
        else:
            print("\nDEV mode: violations logged, build continues")

    print("\nPolicy check completed (NTIA/CISA aligned)")

if __name__ == "__main__":
    enforce_policy("vex/vex.json")
