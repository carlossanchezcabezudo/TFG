# compile_json_to_csv.py

import os
import csv
import json

# Folder containing input JSON files
SOURCE_DIR = "resultados"
# Output CSV file
OUTPUT_CSV = "resultados_final.csv"

# Define the CSV header
HEADER = [
    "created_at", "aid", "extension", "format", "duration", "FILE_STORED", "FACIAL_ANALYSED",
    "VOICE_ANALYSED", "VOICE_TRANSCRIBED", "BIOMETRICS_EXTRACTED", "SPEECH_ANALYSED", "PERSONALITY_ANALYSED",
    "FACES_EXTRACTED", "id", "angry_facial", "disgust_facial", "fear_facial", "happy_facial", "sad_facial",
    "surprise_facial", "neutral_facial", "most_frequent_dominant_emotion", "dominant_emotion_counts_surprise",
    "average_face_confidence", "extraversion", "neuroticism", "agreeableness", "conscientiousness", "openness",
    "survival", "creativity", "self_esteem", "compassion", "communication", "imagination", "awareness",
    "stress_high", "stress_medium", "stress_low", "helplessness_high", "helplessness_medium", "helplessness_low",
    "self_efficacy_medium", "self_efficacy_low", "self_efficacy_high", "depression_high", "depression_medium",
    "depression_low", "voice_mean", "voice_sd", "voice_median", "voice_mode", "voice_Q25", "voice_Q75", "voice_IQR",
    "voice_skewness", "voice_kurtosis", "voice_mean_note", "voice_median_note", "voice_mode_note", "voice_Q25_note",
    "voice_Q75_note", "voice_rmse", "pitch", "tone", "sad_voice", "disgust_voice", "fearful_voice", "neutral_voice",
    "happy_voice", "angry_voice", "calm_voice", "language", "surprised_voice", "no_speech_prob", "entropy",
    "tense_past", "tense_present", "tense_future", "sentiment_polarity", "sentiment_subjectivity", "translation", "variable"
]

# Extracts nested values safely from a JSON object
def extract_nested_value(obj, *keys):
    for key in keys:
        if not isinstance(obj, dict):
            return "null"
        obj = obj.get(key, {})
    return obj if isinstance(obj, (int, float, str)) else "null"

# Temporary function to identify the class (modify if needed)
def classify_variable(file_name):
    return "Ansiedad"

# Write output file and process each .json inside the directory
with open(OUTPUT_CSV, "w", newline="", encoding="utf-8") as outfile:
    writer = csv.writer(outfile)
    writer.writerow(HEADER)

    for file in os.listdir(SOURCE_DIR):
        if file.endswith(".json"):
            full_path = os.path.join(SOURCE_DIR, file)

            try:
                with open(full_path, "r", encoding="utf-8") as f:
                    json_data = json.load(f).get("response", {})

                # Structured data extraction
                metadata = json_data.get("original_file", {})
                status_flags = json_data.get("status", {})
                traits = json_data.get("data", {}).get("traits", {})
                facial_avg = json_data.get("data", {}).get("facial", {}).get("average_emotions", {})
                facial_meta = json_data.get("data", {}).get("facial", {})
                voice_data = json_data.get("data", {}).get("voice", {}).get("frequencies", {}) or {}
                voice_emotions = json_data.get("data", {}).get("voice", {}).get("emotions", {}) or {}
                speech_data = json_data.get("data", {}).get("speech", {}) or {}
                tense_info = speech_data.get("tense", {}) or {}
                sentiment_data = speech_data.get("sentiment", {}) or {}

                row_data = [
                    json_data.get("created_at", "null"),
                    json_data.get("aid", "null"),
                    metadata.get("extension", "null"),
                    metadata.get("format", "null"),
                    metadata.get("duration", "null"),
                    status_flags.get("FILE_STORED", "null"),
                    status_flags.get("FACIAL_ANALYSED", "null"),
                    status_flags.get("VOICE_ANALYSED", "null"),
                    status_flags.get("VOICE_TRANSCRIBED", "null"),
                    status_flags.get("BIOMETRICS_EXTRACTED", "null"),
                    status_flags.get("SPEECH_ANALYSED", "null"),
                    status_flags.get("PERSONALITY_ANALYSED", "null"),
                    status_flags.get("FACES_EXTRACTED", "null"),
                    json_data.get("external_vars", {}).get("id", "null"),
                    facial_avg.get("angry", "null"),
                    facial_avg.get("disgust", "null"),
                    facial_avg.get("fear", "null"),
                    facial_avg.get("happy", "null"),
                    facial_avg.get("sad", "null"),
                    facial_avg.get("surprise", "null"),
                    facial_avg.get("neutral", "null"),
                    facial_meta.get("most_frequent_dominant_emotion", "null"),
                    facial_meta.get("dominant_emotion_counts", {}).get("surprise", "null"),
                    facial_meta.get("average_face_confidence", "null"),
                    traits.get("extraversion", "null"),
                    traits.get("neuroticism", "null"),
                    traits.get("agreeableness", "null"),
                    traits.get("conscientiousness", "null"),
                    traits.get("openness", "null"),
                    extract_nested_value(traits, "survival"),
                    extract_nested_value(traits, "creativity"),
                    extract_nested_value(traits, "self_esteem"),
                    extract_nested_value(traits, "compassion"),
                    extract_nested_value(traits, "communication"),
                    extract_nested_value(traits, "imagination"),
                    extract_nested_value(traits, "awareness"),
                    extract_nested_value(traits, "stress", "high"),
                    extract_nested_value(traits, "stress", "medium"),
                    extract_nested_value(traits, "stress", "low"),
                    extract_nested_value(traits, "helplessness", "high"),
                    extract_nested_value(traits, "helplessness", "medium"),
                    extract_nested_value(traits, "helplessness", "low"),
                    extract_nested_value(traits, "self_efficacy", "medium"),
                    extract_nested_value(traits, "self_efficacy", "low"),
                    extract_nested_value(traits, "self_efficacy", "high"),
                    extract_nested_value(traits, "depression", "high"),
                    extract_nested_value(traits, "depression", "medium"),
                    extract_nested_value(traits, "depression", "low"),
                    voice_data.get("mean", "null"),
                    voice_data.get("sd", "null"),
                    voice_data.get("median", "null"),
                    voice_data.get("mode", "null"),
                    voice_data.get("Q25", "null"),
                    voice_data.get("Q75", "null"),
                    voice_data.get("IQR", "null"),
                    voice_data.get("skewness", "null"),
                    voice_data.get("kurtosis", "null"),
                    voice_data.get("mean_note", "null"),
                    voice_data.get("median_note", "null"),
                    voice_data.get("mode_note", "null"),
                    voice_data.get("Q25_note", "null"),
                    voice_data.get("Q75_note", "null"),
                    voice_data.get("rmse", "null"),
                    extract_nested_value(json_data, "data", "voice", "pitch"),
                    extract_nested_value(json_data, "data", "voice", "tone"),
                    voice_emotions.get("sad", "null"),
                    voice_emotions.get("disgust", "null"),
                    voice_emotions.get("fearful", "null"),
                    voice_emotions.get("neutral", "null"),
                    voice_emotions.get("happy", "null"),
                    voice_emotions.get("angry", "null"),
                    voice_emotions.get("calm", "null"),
                    speech_data.get("language", "null"),
                    voice_emotions.get("surprised", "null"),
                    speech_data.get("no_speech_prob", "null"),
                    speech_data.get("entropy", "null"),
                    tense_info.get("past", "null"),
                    tense_info.get("present", "null"),
                    tense_info.get("future", "null"),
                    sentiment_data.get("polarity", "null"),
                    sentiment_data.get("subjectivity", "null"),
                    json_data.get("response", {}).get("data", {}).get("translation", "null"),
                    classify_variable(file)
                ]

                writer.writerow(row_data)
                print(f"✅ Row written for {file}")

            except Exception as err:
                print(f"❌ Failed processing {file}: {err}")
