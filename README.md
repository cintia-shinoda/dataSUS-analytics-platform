# DataSUS Analytics Platform

An end-to-end analytics platform for the Brazilian public health data (DataSUS), featuring an automated data pipeline, modular architecture, and interactive dashboard for exploratory data analysis.

> Evolution of the project `scrap-data-sus` (2022), that aimed to scrap COVID-19 vaccination data. Redesigned with a modern data stack and scalable architecture.

## Modules
| Module | Data Source | System |
|:---|:---|:---|
| COVID-19 Vaccination | OpenDataSUS S3 / Elasticsearch | SI-PNI |
| Dengue & Arboviruses | SINAN / InfoDengue API | SINAN Online |
| Severe Acute Respiratory Syndrome (SRAG) | Sivep-Gripe (OpenDataSUS) | Sivep-Gripe |
| Mortality | SIM (via PySUS) | SIM |
| Hospitalizations | SIH-SUS (via Py-SUS) | SIH |
| General Immunization | PNI (via PySUS) | PNI |


<!-- ## Data Sources

| Resource | Description |
| --- | --- |
| PySUS |  | SIM, SIH, SINAN, SINASC, PNI, CNES via FTP.Docs |
| OpenDataSUS |  |
| InfoDengue API |  |
| TABNET/DataSUS |  | -->



## Architecture



## Project Structure
```bash
dataSUS-analytics-platform/
├── data/
│   ├── raw/
│   └── processed/
├── docs/
├── notebooks/
├── src/
├── tests/
├── .gitignore
└── README.md
```


## Stack


## Setup

1. Clone the repository:
    ```bash
    git clone https://github.com/cintia-shinoda/dataSUS-analytics-platform.git
    cd dataSUS-analytics-platform
    ```

