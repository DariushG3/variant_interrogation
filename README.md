# variant_interrogation
Querying multiple SNPs in genomic databases


- Fo look-up of the variants we had several options which covered difference genetic databases. These optios are:
1. [Phenoscanner (PS)](http://www.phenoscanner.medschl.cam.ac.uk/)
2. [OpenTargets (OT)](https://www.opentargets.org/)
3. [GWAS Catalog (GC)](https://www.ebi.ac.uk/gwas/home)
4. [PheWeb (PW)](https://github.com/statgen/pheweb)

- Having pooled the results of look-up of the variants in __PS__ with the scan of the variants in __OT__ provided by David's aid, we found that there is no common traits that remained after interrogating variants association with different traits between these two look-up results and we are still missing the important info like effect size and standard errors of the interrogated variants significant at 5E-08 level. Therefore, we decided to look the variants up in the GWAS catalog database. 

- To do the interrogation of the variants in GWAS Catalog, there are two options: 
(1) is using the [GWASrapidd v. 0.99.14](https://rmagno.eu/gwasrapidd/reference/get_variants.html) which is an R package available on [Cran](https://cran.r-project.org/web/packages/gwasrapidd/) lokking for the variants to find an evidence in GWAS Catalog database.
(2) is the [GWAS Catalog official](https://www.ebi.ac.uk/gwas/docs/api) [REST API](https://github.com/EBISPOT/goci-rest) in Python.

- Here we are taking the advantage of the __GC__ API to automatically query the SNPs to find the corresponding associated traits (14-Feb-2023).

- Having got a try to an R package, switched to REST API on python and store the look-up results in am dataframe. Still some manipulations needed to save the reported trait in the summary results using the study info or url (17-Feb-2023).

- Using the __GWAS Catalog rest API__ we qureried the variants on  __GC__  summary statistics. The most recent update made to the website was on 15-Feb-23 as it was mentioned on the [home page](https://www.ebi.ac.uk/gwas/home) of their website that: "As of 2023-02-15, the GWAS Catalog contains 6263 publications, 487213 top associations and 55244 full summary statistics." Wow!! The last recent added study dates back to 19-Jan-2023 when the Miyazawa K et al. summary results was added (PubMed id = 36653681). More info on the recnlty added studies [here](https://www.ebi.ac.uk/gwas/downloads/summary-statistics) We did the interrogation of our variants on 18-Feb-2023, though.

- After merging the __GC__ and previous __PS__ variants look-up results, we figured out we still miss the important information of the associations (Beta, SE) for some of the studies (19-Feb-23). 

- So we diecided to query the variants using __PW__ commandline tool which mostly contains the summary ststistics of GWAS studies done on UKBB data (19-Feb-23).

- I encountered with some errors in installation of __PW__ in my directory on Eurac servers. Let's find the solution later to install it properly. Until then, the priority is first finishing the missing info in the merged __PS + GC__ summary results and merge it with step 3 of the mediation analysis. DO NOT forget to align the risk allele for each assoication results before using it for merging or even after for merging with step 3 results of the paper (21-Feb-23).

- As we decided to manually fill the mnissing information of the summary results of interrogation in __GC__, I manually seeked for those studies wih missing beta or se. Having looked at their results tables or in most cases at the suppl. tables, I figured out the p-values retrieved from the __GC__ look-up are rounded. Thus, I corrected with its actual value for these studies. However, seems that the manuall investigating the variants in pubmed doesn't help that much I expected at the beginning. **The __GC__ rest API indeed retrieved all the available information from these studies. The rest which is missing or empty have not been provided by the study authors, to be honest**. Therefore, it's time to go ahead and warp up the variants interrogation job by all the results we could gather by querying our variants in __PS + OT + GC__ during the last few months (22-Feb-23).

- The summary results of interrogation in __GC__ and __PS__ have been manually cleaned by looking at each study missing some association details. Now just Ancestry type needs to be added to __GC__ results. So, the python function should be updated to incorporate Ancestry to the parsed json output in the csv file. Then, it is time to merge the __GC__ and __PS__ results (24-Feb-23).

