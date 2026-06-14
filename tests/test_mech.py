import pytest
from lab0.mech.structural import run_structural_analysis

def test_structural():
    spec = {'load_n': 10, 'length': 50, 'thickness': 5, 'width': 30, 'material_yield_mpa': 40}
    res = run_structural_analysis(spec)
    checks = res.data['structural_checks']
    assert 'bending_stress' in checks
