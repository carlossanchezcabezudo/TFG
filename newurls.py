# url_formatter.py

import pandas as pd

# Define the path to the Excel source file
source_path = "csv_finalCSVMulti.xlsx"

# Load the Excel file without treating the first row as headers (everything is in one column)
raw_data = pd.read_excel(source_path, header=None)

# Split the single column into multiple columns using the comma delimiter
structured_data = raw_data[0].str.split(",", expand=True)

# Assign column headers from the first row and discard that row from the dataset
structured_data.columns = structured_data.iloc[0]
structured_data = structured_data.drop(index=0).reset_index(drop=True)

# Prepare the final DataFrame by formatting filenames and result URLs
output_df = pd.DataFrame()
output_df["filename"] = structured_data["variable"] + (structured_data.index + 1).astype(str) + ".mp4"
output_df["result_url"] = "/v1/result/" + structured_data["aid"]

# Export the transformed data into a new CSV file
output_df.to_csv("urls_resultado.csv", index=False)

print("The file 'urls_resultado.csv' has been successfully created.")
