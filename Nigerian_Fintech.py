#Import Libraries
import pandas as pd 
import numpy as np
import duckdb
import re 
import json
import random 

#Initializing the duckdb connection
conn = duckdb.connect("Wayne_bank_naija.db")

#Using pandas to read the csv file that we have
df = pd.read_csv("nigerian_banking_transactions_1000.csv")
internal_records = []

for i in range(990):
    row = df.iloc[i]
    #Finding the 30-digit NIBSS in the narration 
    match = re.search(r'\d{30}', str(row['narration']))
    session_id = match.group(0) 

#This record is in the app  but does not exist in the bank csv
internal_records.append({
    "internal_id":"WEB/PAYSTACK/REF",
    "session_id":"999260753529965053533694756153",
    "amount":25000,
    "user_name":"Cynthia Adeyemi",
    "status":"FAILURE"
},
{
        "user_name": "Chukwuma Ifeanyi",
        "session_id": "999260411130197198839195553989",
        "amount": 49000,
        "status": "SUCCESS"
    })

with open("internal_app_log.json", "w") as f:
    json.dump(internal_records, f, indent=4)

print("The Internal Logs have been created")
