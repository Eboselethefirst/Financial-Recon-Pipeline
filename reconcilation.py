import pandas as pd
import duckdb 


conn = duckdb.connect("wayne_bank_naija.db")

conn.execute(r"""  
    CREATE OR REPLACE TABLE amount_mismatches AS
    SELECT 
        app.user_name,
        app.session_id,
        app.amount as app_amount,
        bank.amount as bank_amount,
        (bank.amount - app.amount) AS variance_amount,
        'INVESTIGATION_REQUIRED' AS internal_status
        FROM read_json_auto('internal_app_log.json') AS app
        LEFT JOIN read_csv_auto('nigerian_banking_transactions_1000.csv') AS bank
        ON app.session_id = regexp_extract(bank.narration, '(\d{30})')
        WHERE app.amount != bank.amount
""")

print("Mismatch Table For Audit")


#for the records requiring review
print("---- RECORDS REQUIRING ACCOUNTING OVERVIEW ----")
print(conn.sql("SELECT * from  amount_mismatches").show())

