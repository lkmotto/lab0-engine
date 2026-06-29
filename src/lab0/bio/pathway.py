from lab0.trust import uncalibrated, Check


def analyze_pathway(spec):
    from cobra.io import load_model

    model_name = spec.get("model", "textbook")  # e.g. ecoli core
    try:
        model = load_model(model_name)
        solution = model.optimize()

        growth_rate = solution.objective_value
        passed = growth_rate > 0.1

        checks = {
            "fba_growth": Check(
                passed=passed,
                detail=f"Optimal growth rate: {growth_rate:.3f} mmol/(gDW h)",
            )
        }

    except Exception as e:
        checks = {"error": Check(passed=False, detail=str(e))}

    return uncalibrated("cobrapy_fba", {"pathway_checks": checks})
