#!/usr/bin/bash


# Accessing the API
#curl 'https://www.ebi.ac.uk/gwas/rest/api' -i -H 'Accept: application/json'

# Listing studies
#curl 'https://www.ebi.ac.uk/gwas/rest/api/studies' -i -H 'Accept: application/json'

# Searching studies
#curl 'https://www.ebi.ac.uk/gwas/rest/api/studies/search' -i -H 'Accept: application/json'

# Listing associations
#curl 'https://www.ebi.ac.uk/gwas/rest/api/associations' -i -H 'Accept: application/json'

# Searching associations
#curl 'https://www.ebi.ac.uk/gwas/rest/api/associations/search' -i -H 'Accept: application/json'

# Retrieve an association
#curl 'https://www.ebi.ac.uk/gwas/rest/api/associations/16510553' -i -H 'Accept: application/json'

# Listing SNPs
#curl 'https://www.ebi.ac.uk/gwas/rest/api/singleNucleotidePolymorphisms' -i -H 'Accept: application/json'


#cat myresults.json | jq -r '(map(keys) | add | unique) as $cols | map(. as $row | $cols | map($row[.])) as $rows | $cols, $rows[] | @csv' 

#cat myresults.json | jq -r '.[]| join(",")'

#curl -X GET https://www.ebi.ac.uk/gwas/summary-statistics-api/variant/rs3812036/associations

#curl 'https://www.ebi.ac.uk/gwas/rest/api/efoTraits/EFO_0001060' -i -H 'Accept: application/json'

curl 'https://www.ebi.ac.uk/gwas/rest/api/singleNucleotidePolymorphisms/rs7329174/associations/' -i -H 'Accept: application/json' > slc34a1.json

cat slc34a1.json | jq -r '(.[0] | keys_unsorted) as $keys | $keys, map([.[ $keys[] ]])[] | @csv' > slc34a1.csv

