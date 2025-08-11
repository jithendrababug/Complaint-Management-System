import uuid
from datetime import datetime

def input_required(prompt):
    while True:
        val = input(prompt).strip()
        if val:
            return val
        print("This field is required.")

def generate_id():
    return str(uuid.uuid4())[:8]

def get_timestamp():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")
