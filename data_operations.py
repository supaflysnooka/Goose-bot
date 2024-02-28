# data_operations.py

import json

def load_data(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

async def save_data(file_path, new_entry):
    existing_data = load_data(file_path)
    existing_data.append(new_entry)
    try:
        with open(file_path, 'w', encoding='utf-8') as file:
            json.dump(existing_data, file, ensure_ascii=False, indent=2)
    except Exception as e:
        print(f"Error saving data: {e}")
