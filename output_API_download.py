# results_downloader.py

import os
import csv
import json
import subprocess

# Configuration values
#API_TOKEN = "xxx"
API_BASE = "https://heratropic-main-c6ba0ae.d2.zuplo.dev"
RESULT_DIR = "resultados"
INPUT_CSV = "urls_resultado.csv"

# Ensure that the output folder exists
os.makedirs(RESULT_DIR, exist_ok=True)

# Load all rows from the input CSV and query the API for each result URL
with open(INPUT_CSV, newline="", encoding="utf-8") as infile:
    csv_reader = csv.DictReader(infile)

    for entry in csv_reader:
        video_name = entry["filename"]
        result_path = entry["result_url"]
        request_url = f"{API_BASE}{result_path}"
        output_file = os.path.join(RESULT_DIR, video_name.replace(".mp4", ".json"))

        print(f"📡 Fetching analysis result for {video_name}...")

        try:
            curl_command = [
                "curl", "-s", "-X", "GET", request_url,
                "-H", f"Authorization: Bearer {API_TOKEN}"
            ]

            response = subprocess.run(curl_command, capture_output=True, text=True)

            if response.returncode == 0:
                try:
                    parsed = json.loads(response.stdout)
                    with open(output_file, "w", encoding="utf-8") as f_out:
                        json.dump(parsed, f_out, indent=4)
                    print(f"✅ Saved to {output_file}")
                except json.JSONDecodeError:
                    print(f"❌ Invalid JSON response for {video_name}")
            else:
                print(f"❌ curl execution failed: {response.stderr}")

        except Exception as error:
            print(f"❌ Unexpected error while handling {video_name}: {error}")
