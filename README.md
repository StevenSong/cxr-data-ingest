# CXR Data Ingest

This repository contains utilities for ingesting chest X-rays, their corresponding text reports, and preprocessing data samples for downstream modeling use. The 2 primary datasets are MIMIC-CXR and CheXpert Plus.

* MIMIC-CXR: https://physionet.org/content/mimic-cxr-jpg/2.1.0/
* CheXpert Plus: https://aimi.stanford.edu/datasets/chexpert-plus

### TODO

* add CheXpert+ section
* add labeling details

### Prerequisites

* Account credentialing and training on physionet: https://www.physionet.org/settings/credentialing/
* Account on StanfordAIMI: https://stanfordaimi.azurewebsites.net/
* Docker for running chexpert labeler
* Python dependencies specified in requirements.txt

## Table of Contents
1. [MIMIC-CXR](#mimic-cxr)
1. [CheXpert Plus](#chexpert-plus)
1. [Labeling](#labeling)

## MIMIC-CXR

**NB**: the labels provided by the MIMIC-CXR authors are derived over a mixture of report sections. As noted in the original MIMIC-CXR publication (https://arxiv.org/pdf/1901.07042):

> Labels for the images were derived from either the impression section, the findings section (if impression was not present), or the final section of the report (if neither impression nor findings sections were present).

This makes experimentation over separate report sections difficult, as labels may not be derived over the section of interest. To resolve this, we section the reports and rederive labels over distinct report sections. Further, the provided labels are using the original CheXpert labeler rather than its updated version, CheXbert. We relabel using both variants for flexible downstream experimentation.

### To prepare the dataset:

1. Download MIMIC-CXR-JPG: https://physionet.org/content/mimic-cxr-jpg/2.1.0/. This may take a few days if using `wget`.
1. Cleanup folder structure.
    <details>
    <summary>Expand to show the expected file structure for this step</summary>

    ```
    mimic-cxr
    ├── files
    │   └── [...]
    ├── IMAGE_FILENAMES
    ├── LICENSE.txt
    ├── README
    ├── SHA256SUMS.txt
    ├── mimic-cxr-2.0.0-chexpert.csv.gz
    ├── mimic-cxr-2.0.0-metadata.csv.gz
    ├── mimic-cxr-2.0.0-negbio.csv.gz
    ├── mimic-cxr-2.0.0-split.csv.gz
    └── mimic-cxr-2.1.0-test-set-labeled.csv
    ```
    </details>
1. Download the notes from MIMIC-CXR. Rather than download all of MIMIC-CXR which has all of the original `.dcm` files, we can get just the notes:
    ```bash
    wget -r -N -c -np --user <USER> --ask-password https://physionet.org/files/mimic-cxr/2.1.0/mimic-cxr-reports.zip
    ```
1. Unzip the downloaded reports.
    1. Move `mimic-cxr-reports.zip` to the `mimic-cxr` directory. This will result in the notes being unzipped alongside the jpgs. :
        <details>
        <summary>The folder <b>before</b> unzipping should look like this</summary>

        ```
        mimic-cxr
        ├── files
        │   └── [...]
        ├── IMAGE_FILENAMES
        ├── LICENSE.txt
        ├── README
        ├── SHA256SUMS.txt
        ├── mimic-cxr-2.0.0-chexpert.csv
        ├── mimic-cxr-2.0.0-metadata.csv
        ├── mimic-cxr-2.0.0-negbio.csv
        ├── mimic-cxr-2.0.0-split.csv
        ├── mimic-cxr-2.1.0-test-set-labeled.csv
        └── mimic-cxr-reports.zip
        ```
        </details>
    1. Unzip the reports:
        ```bash
        unzip mimic-cxr-reports.zip
        ```
        <details>
        <summary>The folder <b>after</b> unzipping should look like this</summary>

        ```
        mimic-cxr
        ├── files
        │   └── [...]
        ├── IMAGE_FILENAMES
        ├── LICENSE.txt
        ├── README
        ├── SHA256SUMS.txt
        ├── mimic-cxr-2.0.0-chexpert.csv
        ├── mimic-cxr-2.0.0-metadata.csv
        ├── mimic-cxr-2.0.0-negbio.csv
        ├── mimic-cxr-2.0.0-split.csv
        ├── mimic-cxr-2.1.0-test-set-labeled.csv
        ├── mimic-cxr-reports.zip
        └── notes
            └── [...]
        ```
        </details>
1. Extract note sections:
    ```bash
    python 1_create_section_files.py \
    --reports_path /path/to/mimic-cxr/notes \
    --output_path /path/to/mimic-cxr
    ```
    This will create 2 files in `mimic-cxr`:
    * `mimic_cxr_sectioned.csv` - contains individual report sections for findings, impression, comparison, and the last paragraph.
    * `mimic_cxr_selected_section.csv` - single selected section per report, per the method described by the MIMIC-CXR authors.

## CheXpert Plus

Apologies this section is not as detailed with precise download commands, however we outline the steps as follows:

1. 

## Labeling

## References
1. `create_section_files.py` and `section_parser.py` modified from https://doi.org/10.5281/zenodo.2591653
