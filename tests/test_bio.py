import pytest
from lab0.bio.molecule import analyze_molecule

def test_molecule():
    spec = {'smiles': 'CC(=O)Oc1ccccc1C(=O)O'}
    res = analyze_molecule(spec)
    checks = res.data['molecule_checks']
    assert checks['lipinski_ro5'].passed
    assert checks['qed'].passed
