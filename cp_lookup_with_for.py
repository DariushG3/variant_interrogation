#!/usr/bin/env python3

import requests
import json
import time


#------------------------------------------------------#
#------------------------------------------------------#

base_url = "https://www.ebi.ac.uk/gwas/rest/api/"

studies = "studies/"
pmidSearch = "search/findByPubmedId?pubmedId="
studyAssociations = "associations?projection=associationsByStudySummary"

snps = "singleNucleotidePolymorphisms/"
rsidSearch = "search/findByRsId?rsId="
snpAssociations = "associations?projection=associationsBySnpSummary"

efoTraits = "efoTraits/"
uriSearch = "search/findByEfoUri?uri="
efoAssociations = "associations?projection=associationsByEfoTraitSummary"
#------------------------------------------------------#
#------------------------------------------------------#

# link of the study
api_url = "https://www.ebi.ac.uk/gwas/rest/api/associations/16510553"


#feature_name = packages_json[0]['name']
#api_url = f'https://www.ebi.ac.uk/gwas/rest/api/associations/{feature_name}.json'

# retreive and association
#interrogation = requests.get(api_url).json()

#gwas_catalog = json.loads(interrogation.content)

#print(interrogation)

#output = csv.writer(open("myresults.csv", "w"), lineterminator = '\n')
#for item in interrogation["history"]["observations"]:
#    output.writerow([item['associations'], item['efoTrait']])

#api_str = json.dumps(interrogation, indent = 2)

#with open("myresults.json", "w") as output:
#    output.write(api_str)
#------------------------------------------------------#
#------------------------------------------------------#

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

#------------------------------------------------------#
# Loop through each variant and query the GWAS catalog
for variant in variants:
    url = "https://www.ebi.ac.uk/gwas/summary-statistics-api/variant/" + variant + "/associations"
    response = requests.get(url)
    
    # Check if the request was successful
    if response.status_code == 200:
        #data = json.loads(response.text)["data"]
        response_dict = response.json()
        if "data" in response_dict:
            data = response_dict["data"]

            # Check if any associations were found
            if len(data) > 0:
                print("Variant:", variant)
                print("Traits:", ", ".join([d["trait"] for d in data]))
            else:
                print("No associated traits found for variant", variant)
    else:
        print("Error: Unable to retrieve data for variant", variant)

    # Pause for a few seconds to avoid overloading the API
    time.sleep(3)
#----------------#
#------------------------------------------------------#