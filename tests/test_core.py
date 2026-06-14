import pytest
from lab0.trust import Check, uncalibrated

def test_trust_uncalibrated():
    res = uncalibrated("test_model", {"a": 1})
    assert not res.provenance.calibrated
    assert res.provenance.model_name == "test_model"

def test_check_dataclass():
    c = Check(passed=True, detail="ok")
    assert c.passed
