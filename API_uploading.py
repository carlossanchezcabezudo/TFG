# uploader_engine.py

import os
import csv
import time
import json
import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
from requests.exceptions import SSLError, RequestException

# Global configuration
#API_KEY = "Xxx"
BASE_URL = "https://heratropic-main-c6ba0ae.d2.zuplo.dev"
INPUT_FOLDER = "Videos"
OUTPUT_FILE = "resulting_urls.csv"
ERROR_LOG = "errores.log"

# Handles retrying the upload if transient server issues occur
def upload_video(file_path, presigned_url, attempts=3):
    session = requests.Session()
    retry_config = Retry(total=attempts, backoff_factor=2, status_forcelist=[500, 502, 503, 504])
    adapter = HTTPAdapter(max_retries=retry_config)
    session.mount("https://", adapter)

    try:
        with open(file_path, "rb") as video_data:
            headers = {
                "Content-Type": "video/mp4",
                "Connection": "close"
            }
            response = session.put(presigned_url, data=video_data, headers=headers, timeout=60)
            return response.status_code == 200

    except SSLError as ssl_err:
        print(f"❌ SSL error while uploading {os.path.basename(file_path)}: {ssl_err}")
        with open(ERROR_LOG, "a") as log:
            log.write(f"SSL error for {file_path}: {ssl_err}\n")

    except RequestException as req_err:
        print(f"❌ Network error while uploading {os.path.basename(file_path)}: {req_err}")
        with open(ERROR_LOG, "a") as log:
            log.write(f"Request error for {file_path}: {req_err}\n")

    return False

# Retrieves both the presigned upload URL and the final result URL
def get_presigned_urls(video_filename):
    payload = {
        "filename": video_filename,
        "external_vars": json.dumps({"id": "1"})
    }
    headers = {"Authorization": f"Bearer {API_KEY}"}

    response = requests.post(f"{BASE_URL}/v1/upload/large", data=payload, headers=headers)

    if response.status_code == 200:
        data = response.json()["response"]
        return data["upload_url"], data["result_url"]

    else:
        print(f"❌ Failed to retrieve URL for {video_filename}: {response.text}")
        with open(ERROR_LOG, "a") as log:
            log.write(f"Failed to obtain URL for {video_filename}: {response.text}\n")
        return None, None

# Main execution function for iterating through all videos and uploading them
def execute_batch_upload():
    with open(OUTPUT_FILE, "w", newline="") as csv_out:
        writer = csv.writer(csv_out)
        writer.writerow(["filename", "result_url"])

        video_list = [file for file in os.listdir(INPUT_FOLDER) if file.endswith(".mp4")]

        for video_name in video_list:
            full_path = os.path.join(INPUT_FOLDER, video_name)
            upload_url, result_url = get_presigned_urls(video_name)

            if upload_url and result_url:
                if upload_video(full_path, upload_url):
                    print(f"✅ Successfully uploaded {video_name}")
                    writer.writerow([video_name, result_url])
                else:
                    print(f"❌ Upload failed for {video_name}")
                    with open(ERROR_LOG, "a") as log:
                        log.write(f"Upload failed: {video_name}\n")
                    time.sleep(5)  # brief pause before the next attempt

# Entry point of the script
if __name__ == "__main__":
    execute_batch_upload()
