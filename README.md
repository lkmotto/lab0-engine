# lab0: AI-Native Multi-Domain Engineering Engine

`lab0` is a headless, programmable design and simulation engine spanning three domains: **Mechanical, Electronics, and Biomedical**. 

It is designed specifically for AI agents (like Factory) to parametrically generate designs, run free in-silico validations, and rapidly iterate *before* dispatching to physical fabrication or wet labs.

## The Vision

The core thesis is that **verifying original designs requires comparing a prediction against physical ground truth**, and ground truth has to be measured by hardware.

We divide the architecture into tiers:

*   **Tier-0 (In-Silico / Free):** Software-only generation and simulation. Fast, free, but untrusted. *This is what `lab0` implements today.*
*   **Tier-1 (The $5k Bench):** Automated physical testing (e.g., API-controlled oscilloscopes, DMMs, 3D metrology scanners, motorized force test stands, liquid handling robots). The AI controls the *perception*, the human does the *manipulation/docking*.
*   **Tier-2+ (Lab-Grade/Full Autonomy):** Expensive handling automation, CMMs, EMC chambers.

### The Calibration Seam
The fundamental architectural decision in `lab0` is the **Calibration Seam**. Every simulation result includes a `CalibrationProvenance` object:
```json
{
  "model": "ngspice",
  "calibrated": false,
  "trust": "LOW"
}
```
Currently, all predictions are tagged with a blunt banner: `UNCALIBRATED, predictions only` or `IN SILICO, NOT WET-LAB VALIDATED`. 

The goal is to feed real physical measurements from the Tier-1 bench back into `materials.py`, closing the loop and shifting the trust level from `LOW` to `HIGH` based on earned physical data.

## Supported Domains (Tier-0)

### 1. Mechanical
*   **Generate:** Translates parametric specs into STEP and STL files via `cadquery`.
*   **Validate:** Validates mesh printability, volume, and watertightness via `trimesh`.
*   **Simulate:** Basic analytical structural analysis (stress vs yield, safety factor).

### 2. Electronics
*   **Generate:** Translates circuit specs into SPICE netlists using `PySpice`.
*   **Simulate:** Runs AC sweeps, transient, and operating point simulations via `ngspice` (in subprocess mode) to verify design targets (e.g., cutoff frequency).

### 3. Biomedical
*   **Molecule:** Evaluates target molecules via `RDKit` (Lipinski's Rule of 5, QED).
*   **Pathway:** Flux Balance Analysis (FBA) of metabolic pathways via `COBRApy` (e.g., *E. coli* core model).
*   **Literature:** Consolidates target evidence via PubMed E-utilities.

## Future Roadmap
1.  **Fab Dispatch Wrappers:** Integrate Slant 3D (credentials added to Doppler), JLCPCB, and DNA synthesis APIs for automated quoting and ordering of verified designs.
2.  **Auth Grabber Project:** Revisit autonomous credential acquisition for foreign sites to support expanding fabrication networks without manual API key management.
3.  **Bench Integration:** Integrate SCPI/USB instrument feedback into the material models.
