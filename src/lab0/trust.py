from dataclasses import dataclass
from enum import Enum
from typing import Any, Dict, Optional


class TrustLevel(Enum):
    NONE = 0
    LOW = 1
    MEDIUM = 2
    HIGH = 3


@dataclass
class CalibrationProvenance:
    model_name: str
    calibrated: bool
    trust_level: TrustLevel
    basis: Optional[str] = None


@dataclass
class Check:
    passed: bool
    detail: str


@dataclass
class Result:
    provenance: CalibrationProvenance
    data: Dict[str, Any]


def uncalibrated(
    model_name: str, data: Dict[str, Any], trust: TrustLevel = TrustLevel.LOW
) -> Result:
    return Result(
        provenance=CalibrationProvenance(
            model_name=model_name,
            calibrated=False,
            trust_level=trust,
            basis="In silico prediction without physical ground truth",
        ),
        data=data,
    )
