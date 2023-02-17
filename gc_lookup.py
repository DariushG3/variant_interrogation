#!/usr/bin/env python3

import requests
import json
import time

variants = ["rs7329174", "rs3812036"]

def get_associations(variant):
    url = f"https://www.ebi.ac.uk/gwas/rest/api/singleNucleotidePolymorphisms/{variant}/associations/"
    response = requests.get(url)
    if response.status_code == 200:
        data = json.loads(response.text)["data"]
        if len(data) > 0:
            return {"variant": variant, "traits": [d["trait"] for d in data]}
        else:
            return {"variant": variant, "traits": []}
    else:
        return {"variant": variant, "traits": []}

results = list(map(get_associations, variants))

for result in results:
    if result["traits"]:
        print(f"Variant: {result['variant']}")
        print(f"Traits: {', '.join(result['traits'])}")
    else:
        print(f"No associated traits found for variant {result['variant']}")

    # Pause for a few seconds to avoid overloading the API
    time.sleep(3)
