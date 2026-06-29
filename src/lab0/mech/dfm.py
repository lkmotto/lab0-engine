from lab0.trust import Check, uncalibrated


def run_dfm_checks(stl_path):
    import trimesh

    mesh = trimesh.load(stl_path)

    is_watertight = bool(mesh.is_watertight)
    volume = float(mesh.volume) if is_watertight else 0.0

    # Basic DFM checks
    checks = {
        "watertight": Check(
            passed=is_watertight,
            detail="Mesh is a closed solid"
            if is_watertight
            else "Mesh has holes/open edges",
        ),
        "volume": Check(passed=bool(volume > 0), detail=f"Volume is {volume:.2f} mm^3"),
    }

    return uncalibrated("trimesh", {"dfm_checks": checks})
