import yaml
import sys
import json
from lab0.report import generate_report

def main():
    if len(sys.argv) < 2:
        print("Usage: lab0 run <spec.yaml>")
        sys.exit(1)
        
    yaml_file = sys.argv[-1]
    with open(yaml_file, 'r') as f:
        spec = yaml.safe_load(f)
        
    domain = spec.get('domain')
    results = {}
    
    if domain == 'mech':
        from lab0.mech.generate import part_to_cad, export_cad
        from lab0.mech.dfm import run_dfm_checks
        from lab0.mech.structural import run_structural_analysis
        
        part = part_to_cad(spec)
        export_cad(part, 'output.stl', 'output.step')
        
        results['dfm'] = run_dfm_checks('output.stl')
        results['structural'] = run_structural_analysis(spec)
        
    elif domain == 'elec':
        from lab0.elec.generate import init_circuit
        from lab0.elec.simulate import run_simulation
        
        circuit = init_circuit(spec)
        results['sim'] = run_simulation(circuit, spec)
        
    elif domain == 'bio':
        if 'smiles' in spec:
            from lab0.bio.molecule import analyze_molecule
            from lab0.bio.literature import fetch_literature
            results['molecule'] = analyze_molecule(spec)
            results['literature'] = fetch_literature(spec)
        elif 'model' in spec:
            from lab0.bio.pathway import analyze_pathway
            results['pathway'] = analyze_pathway(spec)
            
    generate_report(domain, spec.get('name'), results)

if __name__ == '__main__':
    main()
