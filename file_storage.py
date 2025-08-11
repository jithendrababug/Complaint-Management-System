import json
import os

DATA_FILE = "complaints.json"

def load_complaints():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r") as file:
        content = file.read().strip()
        if not content:
            return []
        return json.loads(content)


def save_complaint(complaint):
    complaints = load_complaints()
    complaints.append(complaint)
    save_all_complaints(complaints)

def save_all_complaints(complaints):
    with open(DATA_FILE, "w") as file:
        json.dump(complaints, file, indent=4)
