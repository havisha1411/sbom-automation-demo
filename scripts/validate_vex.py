import json
import sys

# Minimum required fields in VEX for each component
REQUIRED_FIELDS = ["bom-ref", "status"]

def load_json(path):
    """Load a JSON file from a given path."""
    with open(path, "r") as f:
        return json.load(f)

def validate_components_in_vex(vex_components, sbom_components):
    """
    Ensure each component in the VEX exists in SBOM and has required fields.
    Returns a list of errors if any.
    """
    sbom_refs = {comp.get("bom-ref") for comp in sbom_components}
    errors = []

    for comp in vex_components:
        # Check for required fields
        for field in REQUIRED_FIELDS:
            if field not in comp or not comp[field]:
                errors.append(f"- Component '{comp.get('bom-ref', 'unknown')}' missing '{field}'")

        # Check if VEX component exists in SBOM
        if comp.get("bom-ref") not in sbom_refs:
            errors.append(f"- Component '{comp.get('bom-ref', 'unknown')}' not found in SBOM")

    return errors

def validate_vex(vex_path, sbom_path):
    """Validate VEX file against the SBOM."""
    vex = load_json(vex_path)
    sbom = load_json(sbom_path)

    vex_components = vex.get("components", [])
    sbom_components = sbom.get("components", [])

    errors = validate_components_in_vex(vex_components, sbom_components)

    if errors:
        print("VEX validation failed:")
        for err in errors:
            print(err)
        sys.exit(1)

    print("VEX validation passed.")

if __name__ == "__main__":
    validate_vex("vex/vex.json", "sbom/sbom.json")
