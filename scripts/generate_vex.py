import json
from datetime import datetime, timezone
from uuid import uuid4


def load_vulnerabilities(path):
    with open(path, "r") as f:
        return json.load(f)["vulnerabilities"]


def generate_vex(vuln_input_path, output_path):
    vulnerabilities = load_vulnerabilities(vuln_input_path)

    vex_document = {
        "bomFormat": "CycloneDX",
        "specVersion": "1.4",
        "version": 1,
        "serialNumber": f"urn:uuid:{uuid4()}",
        "$schema": "http://cyclonedx.org/schema/bom-1.4.schema.json",
        "metadata": {
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "tools": [
                {
                    "vendor": "CycloneDX",
                    "name": "sbom-automation-demo",
                    "version": "1.0"
                }
            ]
        },
        "vulnerabilities": []
    }

    for v in vulnerabilities:
        vex_entry = {
            "id": v["cve"],
            "source": {
                "name": "NVD",
                "url": "https://nvd.nist.gov"
            },
            "ratings": [
                {
                    "severity": v["severity"].upper(),
                    "method": "CVSSv3"
                }
            ],
            "affects": [
                {
                    "ref": f"pkg:pypi/{v['package']}@{v['installed_version']}"
                }
            ],
            "analysis": {
                "state": v["status"],
                "justification": v["justification"],
                "detail": f"Fixed in version {v['fixed_version']}"
            }
        }

        vex_document["vulnerabilities"].append(vex_entry)

    with open(output_path, "w") as f:
        json.dump(vex_document, f, indent=2)

    print(f"VEX generated successfully at {output_path}")


if __name__ == "__main__":
    generate_vex("vex/vuln_input.json", "vex/vex.json")
