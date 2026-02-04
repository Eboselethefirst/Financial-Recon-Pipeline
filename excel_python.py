import pandas as pd 
import duckdb


conn = duckdb.connect("wayne_bank_naija.db")

df_mismatches= conn.sql("SELECT * from  amount_mismatches").df()
df_reversals = conn.sql("SELECT * FROM pending_reversals").df()

if not df_reversals.empty:
    df_reversals["detected_time"] = pd.to_datetime(df_reversals['detected_time']).dt.tz_localize(None)
try:
    with pd.ExcelWriter("Daily_account_report.xlsx", engine="openpyxl") as writer:
        df_reversals.to_excel(writer,sheet_name="Pending Reversals", index =False)
        df_mismatches.to_excel(writer, sheet_name="Amount_Mismatches", index=False)
    print("Sucess in file creation")
except Exception as e:
    print("There are still issues")


print("Report Ready")
print(" File 'The Daily_account_report.xlsx' has been generated with two sheets.")