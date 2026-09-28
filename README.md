# Portfolio

This project is meant to demonstrate the skills of a full-stack data pipeline. From source, through transformations, modeled, and finally visualized. 

The domain is not the important subject, but for context, this data comes from a popular esport, competitive Fortnite. 

## Overview 

Data is pulled from an API and landed into a storage layer for analysis. The pipeline then standardizes, cleans, and enriches the raw records before loading them into a warehouse-friendly model. From there, the data is used to answer business-facing questions and create a simple visualization layer for analysis.

### Pipeline stages

- Ingestion: pull raw Fortnite-related data from an external API and store the original payload.
- Transformation: normalize field names, handle missing values, deduplicate records, and prepare a clean analytical dataset.
- Modeling: build curated fact and dimension tables that support downstream reporting.
- Visualization: expose key metrics with charts and dashboards for easy exploration.

### What this project demonstrates

- API extraction and orchestration
- Data quality checks and validation
- ELT/ETL workflow patterns
- SQL-based transformations and modeling
- Dashboarding and stakeholder-friendly reporting

### Typical questions this project can answer

- Which players or teams have the strongest recent performance?
- How do metrics trend over time across seasons or tournaments?
- What patterns emerge when comparing player stats or match outcomes?

### Tech stack

This project is designed to be flexible and representative of modern data engineering workflows. A typical stack for this kind of solution could include:

- Python for API calls and orchestration
- SQL for transformation logic and modeling
- DuckDB for analytical data warehouse data persistance 
- Tableau for visualization

### Project goals

The goal is to showcase a complete end-to-end data workflow from raw source data to clean, modeled insights that can support real-world analysis and decision-making.

## Future Work

- Rewrite readme to tell a story from the beginning, then bring in tech stack as needed
- Add automated scheduling for API pulls and refreshes to keep the dataset current
- Add data quality checks
- Add more curated model layers for player performance, team trends, and tournament-level analysis
- Add dbt for more robust modeling tech stack
