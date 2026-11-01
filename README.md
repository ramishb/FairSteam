# FairSteam

FAIRification of the [Steam Store Games](https://www.kaggle.com/datasets/nikdavis/steam-store-games) dataset (Nik Davis, Kaggle, CC BY 4.0).
FAIR Data Engineering, University of Twente, 2026 – Group 02 (Ramish Bhutto).

## Contents

| Folder | Content |
|---|---|
| `Data/Original/` | `steam_raw.csv` (original Kaggle file), `steam_top1000.csv` (cleaned 1000-game subset) |
| `Data/Fairified/` | `steam_top1000.ttl` – the FAIRified data in RDF (Turtle) |
| `Ontology/` | `steam_ont.ttl` – the semantic data model, plus diagrams |
| `Metadata/Schemas/` | SHACL metadata schemas used in the FAIR Data Point |
| `Metadata/Records/` | Metadata records of the FAIR Data Point, catalog, dataset and distributions |
| `Code/` | Subset script and OpenRefine operation history |
| `Docker/` | Configuration of the local FAIR Data Point |

## Identifiers

- Ontology: https://w3id.org/FAIR-course-UT/2026/group02/ont
- FAIRified data: https://w3id.org/FAIR-course-UT/2026/group02/data
- Cleaned CSV: https://w3id.org/FAIR-course-UT/2026/group02/data/csv

## Licence

CC BY 4.0, like the source data. Cite the original as: Nik Davis (2019). Steam Store Games (Clean dataset), version 3. Kaggle.
