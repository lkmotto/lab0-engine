from lab0.trust import uncalibrated, Check


def analyze_molecule(spec):
    from rdkit import Chem
    from rdkit.Chem import Descriptors, QED

    smiles = spec.get("smiles", "")
    mol = Chem.MolFromSmiles(smiles)
    if not mol:
        return uncalibrated("rdkit", {"error": "Invalid SMILES"})

    mw = Descriptors.MolWt(mol)
    logp = Descriptors.MolLogP(mol)
    hbd = Descriptors.NumHDonors(mol)
    hba = Descriptors.NumHAcceptors(mol)
    qed_score = QED.qed(mol)

    # Lipinski's Rule of 5
    ro5_passed = (mw <= 500) and (logp <= 5) and (hbd <= 5) and (hba <= 10)

    checks = {
        "lipinski_ro5": Check(
            passed=ro5_passed,
            detail=f"MW:{mw:.1f}, LogP:{logp:.2f}, HBD:{hbd}, HBA:{hba}",
        ),
        "qed": Check(passed=qed_score > 0.5, detail=f"QED Score: {qed_score:.3f}"),
    }

    return uncalibrated("rdkit", {"molecule_checks": checks})
