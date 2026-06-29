def part_to_cad(spec):
    import cadquery as cq

    # Very basic L-bracket generation based on spec dimensions
    # Assuming spec is a PartSpec dictionary
    length = spec.get("length", 50.0)
    width = spec.get("width", 30.0)
    thickness = spec.get("thickness", 5.0)

    # Create an L-bracket
    bracket = (
        cq.Workplane("front")
        .polyline(
            [
                (0, 0),
                (length, 0),
                (length, thickness),
                (thickness, thickness),
                (thickness, width),
                (0, width),
            ]
        )
        .close()
        .extrude(width)
    )

    # Add a hole if specified
    if "hole_dia" in spec:
        bracket = bracket.faces(">Z").workplane().hole(spec["hole_dia"])

    return bracket


def export_cad(part, stl_path, step_path):
    import cadquery as cq

    cq.exporters.export(part, stl_path)
    cq.exporters.export(part, step_path)
