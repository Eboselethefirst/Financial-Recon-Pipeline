# Eboselethefirst-Financial-Recon-Pipeline
# 💸 Financial Reconciliation Pipeline: Solving the "Ghost Transaction" Mystery

### **The Problem: "Bank says Success, Landlord says No."**
Two days ago, my friend faced a nightmare: multiple transfers made, funds debited, but zero Naira received at the destination. In the Nigerian Fintech space, this is often a **Data Reconciliation** failure. 

This project simulates a production-grade pipeline to identify **Ghost Transactions** (funds missing from NIBSS) and **Amount Mismatches** (discrepancies between App logs and Bank records).
##System Architecture
<img width="455" height="548" alt="Flow chart Diagram for Naija_bank" src="https://github.com/user-attachments/assets/b097eb6c-1461-46a2-abc2-b6f2cd71c9ee" />

The pipeline follows a 4-stage process:
1. **Ingestion:** Consuming internal App Logs (JSON) and NIBSS Bank Data (CSV).
2. **Processing:** Using **DuckDB** and **Regex** to clean narrations and perform high-speed SQL Joins.
3. **Persistence:** Maintaining a local database (`wayne_bank_naija.db`) to track reversal audit trails.
4. **Delivery:** Generating stakeholder-ready Excel reports via **Pandas**.

##Tech Stack & Tools
- **Python:** Core orchestration logic.
- **DuckDB:** In-process OLAP database for fast SQL analysis without cloud overhead.
- **Pandas:** Data manipulation and Excel sheet partitioning.
- **SDV (Synthetic Data Vault):** Used to generate anonymized, realistic financial datasets.
- **Regex:** Essential for extracting 30-digit NIBSS Session IDs from unstructured bank strings.

## Project Structure
* `Nigerian_Fintech.py`: Ingests raw data into the DuckDB environment.
* `recon.py` / `reconciliation.py`: Logic for identifying "Ghosts" (Cynthia) and "Mismatches" (Chukwuma).
* `excel_python.py`: Automates the generation of the final `Daily_account_report.xlsx`.

## How to Run
1. Clone the repo:
   ```bash
   git clone [https://github.com/eboselethefirst/Financial-Recon-Pipeline.git](https://github.com/eboselethefirst/Financial-Recon-Pipeline.git)

2. Install dependencies:
   pip install duckdb pandas openpyxl

3.   Run the scripts in this order:
   Nigerian_Fintech.py
   recon.py
   reconciliation.py
   excel_python.py
   
