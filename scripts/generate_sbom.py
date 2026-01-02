from cyclonedx.model.bom import Bom
from cyclonedx.model.component import Component, ComponentType
from cyclonedx.output import make_outputter, OutputFormat, SchemaVersion

def generate_sbom():
    # Create BOM object
    bom = Bom()

    # Create components
    app = Component(name="sample-python-app", version="1.0.0", type=ComponentType.APPLICATION)
    dep = Component(name="requests", version="2.31.0", type=ComponentType.LIBRARY)

    # Add components to BOM (directly to the set)
    bom.components.add(app)
    bom.components.add(dep)

    # Generate JSON SBOM (CycloneDX v1.4)
    outputter = make_outputter(bom=bom, output_format=OutputFormat.JSON, schema_version=SchemaVersion.V1_4)
    sbom_json = outputter.output_as_string()

    # Save SBOM to file
    with open("sbom/sbom.json", "w") as f:
        f.write(sbom_json)

    print("SBOM generated successfully at sbom/sbom.json")

if __name__ == "__main__":
    generate_sbom()
