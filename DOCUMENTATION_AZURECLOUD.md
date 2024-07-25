{\rtf1\ansi\ansicpg1252\cocoartf2709
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw11900\paperh16840\margl1440\margr1440\vieww14420\viewh13360\viewkind0
\pard\tx566\tx1133\tx1700\tx2267\tx2834\tx3401\tx3968\tx4535\tx5102\tx5669\tx6236\tx6803\pardirnatural\partightenfactor0

\f0\fs24 \cf0 # Exchange Rates Analysis Project in Azure Databricks\
\
## Objective\
\
The goal of this project is to fetch exchange rates data from an API, process it using the Medallion architecture in Azure Databricks, and create a dimensional model for analysis.\
\
## Architecture\
\
This project uses the Medallion architecture:\
- **Bronze Layer**: Raw data ingested from the source.\
- **Silver Layer**: Cleansed and enriched data.\
- **Gold Layer**: Aggregated data for analytics and reporting.\
\
## Components\
\
### API Connection\
\
The `fetch_exchange_rates.py` script connects to the API using a stored API key in Databricks secrets, fetches exchange rates data for the specified currencies, and saves it to the Bronze layer.\
\
### Bronze Layer\
\
The `01_Bronze_Layer.ipynb` notebook fetches raw data from the API and saves it in Delta Lake format.\
\
### Silver Layer\
\
The `02_Silver_Layer.ipynb` notebook cleanses and enriches the raw data, preparing it for the Gold layer.\
\
### Gold Layer\
\
The `03_Gold_Layer.ipynb` notebook creates and populates dimension and fact tables in the Gold layer, forming a dimensional model for analysis.\
\
## Audit Tables and Logging\
\
Audit tables are used to track the processing status and logs for each step of the data pipeline. This helps in monitoring and debugging.\
\
## Best Practices\
\
- **Modularity**: Code is organized into separate notebooks and scripts.\
- **Secrets Management**: API keys are securely stored in Databricks secrets.\
- **Version Control**: GitHub is used for version control and collaboration.\
- **Error Handling**: Robust error handling is implemented for API and data processing.\
- **Optimization**: Delta Lake, partitioning, and caching are used for performance.\
\
## Source Files\
\
### Notebooks\
\
- `01_Bronze_Layer.ipynb`: Fetches data from the API and loads it into the Bronze layer.\
- `02_Silver_Layer.ipynb`: Processes and transforms data into the Silver layer.\
- `03_Gold_Layer.ipynb`: Creates and populates dimension and fact tables in the Gold layer.\
\
### Scripts\
\
- `fetch_exchange_rates.py`: Connects to the API and fetches exchange rates data.\
\
### Configs\
\
- `currencies.json`: Specifies the currencies to fetch exchange rates for.\
\
## Optimizations\
\
- **Delta Lake**: Used for efficient data storage and querying.\
- **Partitioning**: Data is partitioned by date for improved query performance.\
- **Caching**: Caching mechanisms are used in Databricks to speed up repeated queries.\
- **Logging**: Comprehensive logging is implemented to track the status and issues of each process.\
}