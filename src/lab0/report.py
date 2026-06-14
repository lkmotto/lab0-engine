import json

def generate_report(domain, name, results):
    banners = {
        "mech": "UNCALIBRATED, predictions only",
        "elec": "UNCALIBRATED, predictions only",
        "bio": "IN SILICO, NOT WET-LAB VALIDATED"
    }
    
    print(f"\n{'='*50}")
    print(f"LAB0 REPORT: {name} ({domain.upper()})")
    print(f"TRUST STATUS: {banners.get(domain, 'UNKNOWN')}")
    print(f"{'='*50}")
    
    out_dict = {}
    all_passed = True
    
    for stage, res in results.items():
        print(f"\n--- {stage.upper()} ---")
        out_dict[stage] = {
            "provenance": {
                "model": res.provenance.model_name,
                "calibrated": res.provenance.calibrated,
                "trust": res.provenance.trust_level.name
            },
            "data": {}
        }
        
        for check_name, check_data in res.data.items():
            if isinstance(check_data, dict):
                for sub_name, sub_check in check_data.items():
                    status = "PASS" if sub_check.passed else "FAIL"
                    if not sub_check.passed: all_passed = False
                    print(f"[{status}] {sub_name}: {sub_check.detail}")
                    out_dict[stage]["data"][sub_name] = {"passed": sub_check.passed, "detail": sub_check.detail}
            else:
                 out_dict[stage]["data"][check_name] = check_data

    print(f"\nOVERALL STATUS: {'PASS' if all_passed else 'FAIL'}")
    
    with open('results.json', 'w') as f:
        json.dump(out_dict, f, indent=2)
    
    print("Results saved to results.json\n")
