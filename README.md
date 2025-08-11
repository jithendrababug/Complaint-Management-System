# Complaint Management System

A simple **command-line application** for managing complaints.  
Users can submit, view, search, and delete complaints. All data is stored locally in a JSON file.

## Features
- **Submit Complaint** – Enter your name, department, and complaint text.
- **View All Complaints** – Display all complaints in a formatted list.
- **Search Complaint by ID** – Quickly find a complaint using its unique ID.
- **Delete Complaint** – Remove a complaint from the system by ID.
- **Persistent Storage** – Data stored in `complaints.json` for later retrieval.

## Project Structure
```
.
├── complaint_handler.py   # Handles complaint submission, viewing, searching, and deletion
├── complaints.json        # Stores complaint records in JSON format
├── file_storage.py        # Handles file read/write operations
├── main.py                # Entry point with the main menu loop
├── utils.py               # Utility functions (ID generation, timestamp, input validation)
```

## Installation & Setup
1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/complaint-management-system.git
   cd complaint-management-system
   ```

2. **Ensure you have Python installed**
   - Python 3.6+ recommended
   - Check version:
     ```bash
     python --version
     ```

3. **Install dependencies**  
   *(No external dependencies – only Python’s standard library is used.)*

4. **Run the application**
   ```bash
   python main.py
   ```

## Usage
When you run the program, you will see a menu:
```
===== Complaint Management System =====
1. Submit Complaint
2. View All Complaints
3. Search Complaint by ID
4. Delete Complaint
5. Exit
```
- Select an option by entering its number.
- Follow the prompts for data entry.

## Data Storage
Complaints are stored in a JSON file (`complaints.json`) in the following format:
```json
[
    {
        "id": "e0b12d56",
        "name": "raj",
        "department": "it",
        "complaint": "torture",
        "timestamp": "2025-07-21 15:11:20"
    }
]
```

## License
This project is licensed under the MIT License. See the LICENSE file for details.
