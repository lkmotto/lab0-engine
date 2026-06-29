from lab0.trust import uncalibrated, Check


def fetch_literature(spec):
    import requests

    target = spec.get("target", "")

    if not target:
        return uncalibrated("pubmed", {"error": "No target specified"})

    # Simple PubMed E-utilities search
    url = f"https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=pubmed&term={target}&retmode=json&retmax=5"
    try:
        resp = requests.get(url)
        data = resp.json()
        count = int(data.get("esearchresult", {}).get("count", 0))

        checks = {
            "literature_found": Check(
                passed=count > 0, detail=f"Found {count} PubMed articles for '{target}'"
            )
        }
    except Exception as e:
        checks = {"error": Check(passed=False, detail=str(e))}

    return uncalibrated("pubmed_eutils", {"literature_checks": checks})
