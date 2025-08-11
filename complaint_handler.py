from file_storage import load_complaints, save_complaint, save_all_complaints
from utils import input_required, generate_id, get_timestamp

def submit_complaint():
    name = input_required("Enter your name: ")
    dept = input_required("Enter department: ")
    text = input_required("Enter your complaint: ")

    complaint = {
        "id": generate_id(),
        "name": name,
        "department": dept,
        "complaint": text,
        "timestamp": get_timestamp()
    }

    save_complaint(complaint)
    print(f"Complaint submitted successfully with ID: {complaint['id']}")

def view_complaints():
    complaints = load_complaints()
    if not complaints:
        print("No complaints found.")
        return

    print("\nList of Complaints:")
    print("-" * 60)
    for c in complaints:
        print(f"ID: {c['id']} | Name: {c['name']} | Dept: {c['department']} | Time: {c['timestamp']}")
        print(f"Complaint: {c['complaint']}\n")

def search_complaint():
    cid = input_required("Enter complaint ID: ")
    complaints = load_complaints()
    for c in complaints:
        if c['id'] == cid:
            print("\nComplaint Found:")
            print(f"ID        : {c['id']}")
            print(f"Name      : {c['name']}")
            print(f"Department: {c['department']}")
            print(f"Time      : {c['timestamp']}")
            print(f"Complaint : {c['complaint']}\n")
            return
    print("Complaint not found.")

def delete_complplaint():
    cid = input_required("Enter complaint ID to delete: ")
    complaints = load_complaints()
    updated = [c for c in complaints if c['id'] != cid]

    if len(updated) == len(complaints):
        print("Complaint ID not found.")
    else:
        save_all_complaints(updated)
        print(f"Complaint ID {cid} deleted successfully.")
