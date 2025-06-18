# enrich_csv_with_text.py

import os
import json
import pandas as pd
import csv

# File and directory configuration
INPUT_CSV = "csv_finalCSVMulti.csv"
OUTPUT_CSV = "dataset_con_texto.csv"
JSON_DIR = "resultados"

# Load the base CSV file into a DataFrame
dataframe = pd.read_csv(INPUT_CSV)

# Add placeholder columns to be filled with values from JSON
dataframe["text"] = None
dataframe["translation"] = None

# Iterate over all JSON files in the given folder
for file in os.listdir(JSON_DIR):
    if file.endswith(".json"):
        json_path = os.path.join(JSON_DIR, file)

        try:
            with open(json_path, "r", encoding="utf-8") as json_file:
                content = json.load(json_file)

            # Extract 'aid' to match the corresponding row in the DataFrame
            identifier = content.get("response", {}).get("aid", None)

            if not identifier:
                print(f"{file}: missing 'aid' field.")
                continue

            speech_section = content.get("response", {}).get("data", {}).get("speech", {})
            extracted_text = speech_section.get("text", "null")

            translated_text = content.get("response", {}).get("data", {}).get("translation", "null")

            # Update corresponding rows in the DataFrame
            dataframe.loc[dataframe["aid"] == identifier, "text"] = extracted_text
            dataframe.loc[dataframe["aid"] == identifier, "translation"] = translated_text

        except Exception as err:
            print(f"Error processing file {file}: {err}")

# Save the updated DataFrame as a fully quoted CSV file
dataframe.to_csv(OUTPUT_CSV, index=False, encoding="utf-8", quoting=csv.QUOTE_ALL)

print(f"\n✅ Final CSV saved as: {OUTPUT_CSV}")
