# Discriminating Bacterial Phenotypes at the Population and Single-Cell Level: A Comparison of Flow Cytometry and Raman Spectroscopy Fingerprinting

This repository accompanies the manscript "*Discriminating Bacterial Phenotypes at the Population and Single-Cell Level: A Comparison of Flow Cytometry and Raman Spectroscopy Fingerprinting*" by [C. Garcia-Timermans](https://github.com/Cristina-GT), [P. Rubbens](https://github.com/prubbens), [R. Props](https://github.com/rprops), [F.-M. Kerckhof](https://github.com/FMKerckhof), [J. Heyse](https://github.com/jeheyse), A. Skirtach,  W. Waegeman and N. Boon. 

## ABSTRACT: 
Investigating phenotypic heterogeneity can help to better understand and manage microbial communities. However, characterizing phenotypic heterogeneity remains a challenge, as there is no standardized analysis framework. Several optical tools are available, such as ﬂow cytometry and Raman spectroscopy, which describe optical properties of the individual cell. In this work, we compare Raman spectroscopy and ﬂow cytometry to study phenotypic heterogeneity in bacterial populations. The growth stages of three replicate Escherichia coli populations were characterized using both technologies. Our ﬁndings show that ﬂow cytometry detects and quantiﬁes shifts in phenotypic heterogeneity at the population level due to its high-throughput nature. Raman spectroscopy, on the other hand, offers a much higher resolution at the singlecell level (i.e., more biochemical information is recorded). Therefore, it can identify distinct phenotypic populations when coupled with analyses tailored toward single-cell data. In addition, it provides information about biomolecules that are present, which can be linked to cell functionality. We propose a computational workﬂow to distinguish between bacterial phenotypic populations using Raman spectroscopy and validated this approach with an external data set. We recommend using ﬂow cytometry to quantify phenotypic heterogeneity at the population level, and Raman spectroscopy to perform a more in-depth analysis of heterogeneity at the single-cell level. 

## Structure: 
* Analysis performed in R can be found [here](https://github.com/CMET-UGent/FCMvsRaman/blob/master/Analysis_Phenotyping%20isogenic%20bacterial%20populations%20using%20flow%20cytometry%20and%20Raman%20spectroscopy.Rmd). 
* Analysis in Python (PhenoGraph and t-SNE) can be found in the file ``phenograph.py`` and ``plot_tsne_density.py``. Results were stored in the directory ``Clustering_PhenoGraph_k``. 
* Gated flow cytometry data can be found  in the directory ``FCSfiles_Ecoli2092`` or on Flowrepository(ID: FR-FCM-ZYV6). 
* Raw Raman spectra can be found in the directory ``Raman_Ecoli2092``. Processed Raman data, in .CSV format, can be found in the file ``hsNorm_RamanSpectra.csv``).
* Additional validation of PhenoGraph and t-SNE using an external dataset can be found directory ``Ramanome_analysis``. Data was originally published by [Teng et al., 2016](https://www.nature.com/articles/srep34359). 

## Example: 
Raman spectroscopy offers a high-resolution characterization of bacterial cells, which can be analyzed with automated algorithms, developed for single-cell data. Here you see an example of a visualization using t-SNE, along with an automated clustering according to the PhenoGraph algorithm:  

<p align="center">
  <img src="./Figures/TSNE_RAMAN.png" width="350"/>
  <img src="./Figures/TSNE_Pheno_k30.png" width="350"/>
</p>


## Acknowledgements
If you find our study useful, please consider citing: 
``` bibtex
@Article{García-Timermans2019,
  Title       = {Discriminating Bacterial Phenotypes at the Population and Single-Cell Level: A Comparison of Flow Cytometry and Raman Spectroscopy Fingerprinting},
  Author      = {García-Timermans, C. and Rubbens, P. and Props, R. and Kerckhof, F.-M. and Heyse, J. and Skirtach, A. and Boon, N. and Waegeman, W. },
  Journal     = {Cytometry Part A},
  Year        = {2019},
}
```
