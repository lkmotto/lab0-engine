from lab0.trust import Result, Check, uncalibrated

def run_structural_analysis(spec):
    # Very simplified analytic structural analysis for an L-bracket (cantilever beam approx)
    # Stress = (M * c) / I
    
    force = spec.get('load_n', 10.0)
    length = spec.get('length', 50.0)
    thickness = spec.get('thickness', 5.0)
    width = spec.get('width', 30.0)
    yield_strength = spec.get('material_yield_mpa', 40.0) # PLA default approx
    
    # M = F * d
    moment = force * length
    # c = t / 2
    c = thickness / 2.0
    # I = (w * t^3) / 12
    inertia = (width * thickness**3) / 12.0
    
    max_stress = (moment * c) / inertia if inertia > 0 else float('inf')
    safety_factor = yield_strength / max_stress if max_stress > 0 else 0
    
    passed = safety_factor > 1.5
    
    checks = {
        "bending_stress": Check(
            passed=passed,
            detail=f"Max stress {max_stress:.2f} MPa (Yield: {yield_strength} MPa, SF: {safety_factor:.2f})"
        )
    }
    
    return uncalibrated("analytic_beam_theory", {"structural_checks": checks})
