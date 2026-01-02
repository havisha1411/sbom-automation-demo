import json
import sys
from packageurl import PackageURL

# NTIA minimal required fields
REQUIRED_COMPONENT_FIELDS = ["name", "version", "type", "supplier", "purl"]
REQUIRED_METADATA_FIELDS = ["name", "version", "type", "supplier"]
REQUIRED_TOOL_FIELDS = ["name", "version"]


def load_sbom(path):
    with open(path, "r") as f:
        return json.load(f)


def validate_component(component):
    """Check if all required fields are present in a component dict."""
    missing = []

    # Name, version, type
    for field in ["name", "version", "type"]:
        if field not in component or not component[field]:
            missing.append(field)

    # Supplier → check if 'name' is present inside supplier object
    supplier = component.get("supplier")
    if not supplier or "name" not in supplier or not supplier["name"]:
        missing.append("supplier.name")

    # purl is only required for library dependencies (skip application)
    if component.get("type") == "library":
        purl = component.get("purl")
        if not purl or not isinstance(purl, dict) and not isinstance(purl, str):
            missing.append("purl")
        else:
            # If JSON contains dict, check type & name fields (PackageURL fields)
            if isinstance(purl, dict):
                if "type" not in purl or not purl["type"]:
                    missing.append("purl.type")
                if "name" not in purl or not purl["name"]:
                    missing.append("purl.name")

    return missing


def validate_metadata(metadata):
    """Check metadata.component minimal fields."""
    missing = []
    app = metadata.get("component", {})

    # Name, version, type
    for field in ["name", "version", "type"]:
        if field not in app or not app[field]:
            missing.append(field)

    # Supplier
    supplier = app.get("supplier")
    if not supplier or "name" not in supplier or not supplier["name"]:
        missing.append("supplier.name")

    return missing


def validate_tools(metadata):
    """Check tools in metadata."""
    missing_tools = []
    tools = metadata.get("tools", [])  # tools is a list in JSON
    for tool in tools:
        tool_missing = []
        for field in ["name", "version"]:
            if field not in tool or not tool[field]:
                tool_missing.append(field)
        if tool_missing:
            missing_tools.append((tool.get("name", "unknown"), tool_missing))
    return missing_tools



def validate_ntia(sbom_path):
    sbom = load_sbom(sbom_path)
    metadata = sbom.get("metadata", {})
    components = sbom.get("components", [])

    #Validate components
    missing_fields = []
    for comp in components:
        comp_missing = validate_component(comp)
        if comp_missing:
            missing_fields.append((comp.get("name", "unknown"), comp_missing))

    #Validate metadata.component
    meta_missing = validate_metadata(metadata)
    if meta_missing:
        missing_fields.append(("metadata.component", meta_missing))

    #Validate tools
    missing_tools = validate_tools(metadata)

    # -------------------------
    # Print results
    # -------------------------
    if missing_fields or missing_tools:
        print("NTIA validation failed:\n")
        for comp_name, fields in missing_fields:
            print(f"- Component '{comp_name}' missing fields: {fields}")
        for tool_name, fields in missing_tools:
            print(f"- Tool '{tool_name}' missing fields: {fields}")
        sys.exit(1)

    print("NTIA validation passed.")


if __name__ == "__main__":
    validate_ntia("sbom/sbom.json")
