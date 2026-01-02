import json
import sys


REQUIRED_TOP_LEVEL_FIELDS = ["bomFormat", "specVersion", "vulnerabilities"]

REQUIRED_VULN_FIELDS = ["id", "affects", "analysis"]
REQUIRED_ANALYSIS_FIELDS = ["state", "justification"]


def load_vex(path):
    with open(path, "r") as f:
        return json.load(f)


def validate_top_level(vex):
    missing = [f for f in REQUIRED_TOP_LEVEL_FIELDS if f not in vex]
    return missing


def validate_vulnerabilities(vulnerabilities):
    errors = []

    for v in vulnerabilities:
        for field in REQUIRED_VULN_FIELDS:
            if field not in v:
                errors.append(f"Vulnerability missing '{field}'")

        analysis = v.get("analysis", {})
        for field in REQUIRED_ANALYSIS_FIELDS:
            if field not in analysis:
                errors.append(
                    f"Vulnerability {v.get('id', 'unknown')} missing analysis.{field}"
                )

        affects = v.get("affects", [])
        if not affects:
            errors.append(
                f"Vulnerability {v.get('id', 'unknown')} has no affected components"
            )

        for a in affects:
            if "ref" not in a:
                errors.append(
                    f"Vulnerability {v.get('id', 'unknown')} affected component missing ref"
                )

    return errors


def validate_vex(vex_path):
    vex = load_vex(vex_path)

    errors = []

    errors.extend(validate_top_level(vex))

    vulnerabilities = vex.get("vulnerabilities", [])
    if not vulnerabilities:
        errors.append("No vulnerabilities found in VEX")

    errors.extend(validate_vulnerabilities(vulnerabilities))

    if errors:
        print("VEX validation failed:")
        for e in errors:
            print(f"- {e}")
        sys.exit(1)

    print("VEX validation passed successfully")


if __name__ == "__main__":
    validate_vex("vex/vex.json")
