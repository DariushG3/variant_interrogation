#!/usr/bin/env python3

import requests
import json
import csv

print("...")

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
#------------------------------------------------------------------------#

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

#CGPT3 suggestion

import requests
import time
import pandas as pd
import json
from pandas import json_normalize

# Define your list of variants of interest
variants = ["rs7329174", "rs3812036"]
variant  = "rs3812036"
response = requests.get("https://www.ebi.ac.uk/gwas/rest/api/singleNucleotidePolymorphisms/rs3812036/associations/")

print(response.status_code)
#print(response.headers)

content_type = response.headers["Content-Type"]
print(content_type)

data = json.loads(response.text)
response_dict = response.json()

summary = []
associations = data['_embedded']['associations']

for association in associations:
    #print(association)
    print("Variant:", variant)
    Rs_Number = variant
    if len(association['loci'][0]['authorReportedGenes']) > 0:
        print("Locus:", association['loci'][0]['authorReportedGenes'][0]['geneName'])
        Locus = association['loci'][0]['authorReportedGenes'][0]['geneName']
    else:
        "NA"
    print("Risk_Allele_Frequency:", association['riskFrequency'])
    Risk_AF = association['riskFrequency']
    print("Beta", association['betaNum'])
    Beta = association['betaNum']
    print("Stderr:", association['standardError'])
    Stderr = association['standardError']
    print("Pvalue:", association['pvalue'])
    pval = association['pvalue']
    print("Trait:", association['_links']['study']['href'])
    Study = association['_links']['study']['href']
    #print("Traits:", ", ".join([d["trait"] for d in data]))
    summary.append([Rs_Number, Locus, Risk_AF, Beta, Stderr, pval, Study])


df = pd.DataFrame(summary, columns=["Variant", "Locus", "Risk_Allele_Frequency", "Beta", "Stderr", "Pvalue", "Study_Link"])

print(df)

if "_embedded" in response_dict:
    feature = response_dict["_embedded"]['associations']
    #feature.headers
        # Check if any associations were found
    if len(feature) > 0:
        print("Variant:", variant)
        #print("Risk_Allele_Frequency:", feature['riskFrequency'])
        #print("Pvalue:", feature['pvalue'])
        #print("Traits:", ", ".join([d["trait"] for d in feature]))
    else:
        print("No associated traits found for variant", variant)
else:
    print("No data")






#----------------#
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
import json

# your JSON output
json_output = """<insert your JSON output here>"""

# parse the JSON output
parsed_json = json.loads(json_output)

# now you can access the data in the JSON
associations = parsed_json['_embedded']['associations']
for association in associations:
    print(association['riskFrequency'])
    # access other fields as needed
