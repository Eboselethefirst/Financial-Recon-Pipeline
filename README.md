# Eboselethefirst-Financial-Recon-PipelineNigerian Fintech Financial Reconciliation Pipeline
Solving the "Ghost Transaction" Mystery with High-Performance OLAP
The Problem: Ledger-Statement Asymmetry
In the Nigerian Fintech landscape, reconciliation failures are a multi-million Naira problem. Customers face the "debit-without-value" nightmare—where internal application logs show a SUCCESS status, but the NIBSS (National Inter-Bank Settlement System) or partner bank records show no corresponding credit.

This pipeline identifies:

1. Ghost Transactions: Funds debited from the user but missing from the settlement bank.
2. Amount Mismatches: Discrepancies between the amount initiated on the app vs. the amount processed by the bank.
3. Session ID Collisions: Identifying duplicate NIBSS session IDs that cause reconciliation loops.

##System Architecture
<img width="455" height="548" alt="Flow chart Diagram for Naija_bank" src="https://github.com/user-attachments/assets/b097eb6c-1461-46a2-abc2-b6f2cd71c9ee" />

#System Architecture
The pipeline is designed with a "Medallion-lite" architecture, utilizing DuckDB for in-process analytical processing to avoid the latency of traditional row-based RDBMS.
1. Ingestion Layer: Consumes semi-structured App Logs (JSON) and unstructured NIBSS Bank Data (CSV).
2. Transformation Layer (The Engine): * Uses Regex to extract 30-digit NIBSS Session IDs from unstructured narration strings.
3. Implements DuckDB SQL for high-speed joins between the Internal Ledger and Bank Statements.
4. Persistence Layer: Maintains a local wayne_bank_naija.db for audit trails and reversal tracking.
5. Delivery Layer: Generates partitioned Excel reports using Pandas for Finance and Operations teams.

##Tech Stack
1. DuckDB: Chosen for its vectorized execution engine, allowing OLAP-speed joins on a local machine.
2. Python (Pandas/Regex): For complex string parsing and data cleaning.
3. SDV (Synthetic Data Vault): To model realistic, anonymized financial data that mirrors Nigerian banking formats.
4.OpenPyXL: To generate stakeholder-ready reports with conditional formatting.

##Project Structure
1. Nigerian_Fintech.py: Data Ingestion & Schema Enforcement.
2. recon.py: Core reconciliation logic identifying "Orphaned" transactions.
3. reconciliation.py: Advanced matching logic for "Mismatches" and "Reversals."
4. excel_python.py: Automated reporting and Excel partitioning.


## How to Run
1. Clone the repo:
   ```bash
   git clone [https://github.com/eboselethefirst/Financial-Recon-Pipeline.git](https://github.com/eboselethefirst/Financial-Recon-Pipeline.git)

2. Install dependencies:
   pip install duckdb pandas openpyxl

3. Execution Flow
To ensure data integrity, run the scripts in the following order:
. Initialize & Ingest: python Nigerian_Fintech.py
. Run Core Recon: python recon.py
. Handle Edge Cases: python reconciliation.py
. Generate Reports: python excel_python.py
   
