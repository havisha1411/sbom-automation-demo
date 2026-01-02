
from cyclonedx.model.bom import Bom 
from cyclonedx.model.component import Component, ComponentType
from cyclonedx.model.contact import OrganizationalEntity
from cyclonedx.model.dependency import Dependency
from cyclonedx.model.tool import Tool
from cyclonedx.output import make_outputter, OutputFormat, SchemaVersion
from packageurl import PackageURL  # <-- new import


def generate_sbom():
    bom = Bom()

    # -------------------------
    # Metadata → Tools
    # -------------------------
    sbom_tool = Tool(
        name="cyclonedx-bom",
        version="7.2.1",
        vendor="CycloneDX"
    )
    bom.metadata.tools._tools.add(sbom_tool)

    # -------------------------
    # Metadata → Application
    # -------------------------
    app_supplier = OrganizationalEntity(name="Internal Engineering Team")

    app = Component(
        name="sample-python-app",
        version="1.0.0",
        type=ComponentType.APPLICATION,
        supplier=app_supplier,
        purl=PackageURL.from_string("pkg:generic/sample-python-app@1.0.0")  # <-- wrap in PackageURL
    )

    bom.metadata.component = app

    # -------------------------
    # Dependency (library only)
    # -------------------------
    dep_supplier = OrganizationalEntity(name="Python Packaging Authority")

    dep = Component(
        name="requests",
        version="2.31.0",
        type=ComponentType.LIBRARY,
        supplier=dep_supplier,
        purl=PackageURL.from_string("pkg:pypi/requests@2.31.0")  # <-- wrap in PackageURL
    )

    bom.components.add(dep)

    # -------------------------
    # Dependency graph
    # -------------------------
    app_dep = Dependency(ref=app.bom_ref)
    dep_dep = Dependency(ref=dep.bom_ref)

    app_dep.dependencies.add(dep_dep)
    bom.dependencies.add(app_dep)

    # -------------------------
    # Output SBOM
    # -------------------------
    outputter = make_outputter(
        bom=bom,
        output_format=OutputFormat.JSON,
        schema_version=SchemaVersion.V1_4
    )

    with open("sbom/sbom.json", "w") as f:
        f.write(outputter.output_as_string())

    print("SBOM generated successfully")


if __name__ == "__main__":
    generate_sbom()
