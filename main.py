from complaint_handler import (
    submit_complaint,
    view_complaints,
    search_complaint,
    delete_complplaint
)

def main():
    while True:
        print("\n===== Complaint Management System =====")
        print("1. Submit Complaint")
        print("2. View All Complaints")
        print("3. Search Complaint by ID")
        print("4. Delete Complaint")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ").strip()
        if choice == '1':
            submit_complaint()
        elif choice == '2':
            view_complaints()
        elif choice == '3':
            search_complaint()
        elif choice == '4':
            delete_complplaint()
        elif choice == '5':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
