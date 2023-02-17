# variant_interrogation
Querying multiple SNPs in genomic databases


- Fo look-up of the variants we had several options which covered difference genetic databases. These optios are:
1. [Phenoscanner](http://www.phenoscanner.medschl.cam.ac.uk/)
2. [OpenTargets](https://www.opentargets.org/)
3. [GWAS Catalog](https://www.ebi.ac.uk/gwas/home)
4. [PheWeb](https://github.com/statgen/pheweb)

- Having pooled the results of look-up of the variants in phenoscanner with the scan of the variants in OpenTargets provided by David's aid, we found that there is no common traits that remained after interrogating variants association with different traits between these two look-up results and we are still missing the important info like effect size and standard errors of the interrogated variants significant at 5E-08 level. Therefore, we decided to look the variants up in the GWAS catalog database. 

- To do the interrogation of the variants in GWAS Catalog, there are two options: 
(1) is using the [GWASrapidd v. 0.99.14](https://rmagno.eu/gwasrapidd/reference/get_variants.html) which is an R package available on [Cran](https://cran.r-project.org/web/packages/gwasrapidd/) lokking for the variants to find an evidence in GWAS Catalog database.
(2) is the [GWAS Catalog official](https://www.ebi.ac.uk/gwas/docs/api) [REST API](https://github.com/EBISPOT/goci-rest) in Python.

- Here we are taking the advantage of the GWAS Catalog API to automatically query the SNPs to find the corresponding associated traits (14-Feb-2023).

- Having got a try to an R package, switched to REST API on python and store the lokik-up results in am dataframe. Still some manipulations needed to save the reported trait in the summary results using the study info or url (17-Feb-2023).

