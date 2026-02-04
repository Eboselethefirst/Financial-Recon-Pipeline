import duckdb

conn = duckdb.connect("wayne_bank_naija.db")

print("--- STARTING THE DATABASE CONNECTION---")

query = """
    SELECT 
        app.user_name AS Customer,
        app.amount AS App_Amount,
        bank.amount AS Bank_Amount,
        CASE 
            WHEN bank.amount IS NULL THEN 'FAILED (Not in Bank)'
            WHEN app.amount != bank.amount THEN 'DISCREPANCY (Wrong Amount)'
            ELSE 'MATCHED'
        END AS Status
        FROM read_json_auto('internal_app_log.json') AS app
        LEFT JOIN read_csv_auto('nigerian_banking_transactions_1000.csv') AS bank
        ON app.session_id = regexp_extract(bank.narration, '(\d{30})')
 """
#Print the results
results = conn.sql(query)
print(results.show())

print("\n ------- SUMMARY OF FAILED TRANSFERS ----  ")
failures = conn.sql(f"SELECT * FROM ({query}) WHERE Status != 'MATCHED'")
print(failures.show())