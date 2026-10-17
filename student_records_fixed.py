# =========================================================================
# Student Record Management System
# Programming Fundamentals with Python - Week 8 Refactoring Exercise
#
# This program reads student data from a CSV file and provides a menu-driven
# interface to list all students and search for a student by ID.
#
# NOTE TO STUDENTS: This program works correctly but is written in a "top-down"
# style with no functions and uses global variables. Your task is to refactor
# this program to make it more readable and maintainable by organizing the code
# into well-named functions and eliminating the use of global variables.
# =========================================================================

import csv

# -------------------------------------------------------------------------
# Global Variables
# -------------------------------------------------------------------------
student_records = []       # Holds all student records loaded from the CSV
csv_filename = ""          # Stores the filename entered by the user
menu_choice = ""           # Stores the user's menu selection
csv_loaded = False         # Tracks whether a CSV file has been loaded

search_id = ""             # Stores the Student ID entered during a search
found_student = None       # Stores the matching student record, if found
search_index = 0           # Loop counter used during linear search

row_number = 0             # Loop counter used when printing student records
current_student = None     # Holds the current record during iteration

student_id = ""            # Fields parsed from each CSV row
student_name = ""
major = ""
gpa = ""
total_credits = ""

# =========================================================================
# Main Program Loop
# =========================================================================
print("=" * 60)
print("       Student Record Management System")
print("=" * 60)

while True:
    # ---------------------------------------------------------------------
    # Display Menu
    # ---------------------------------------------------------------------
    print()
    print("Please select an option:")
    print("  1. Read CSV")
    print("  2. List CSV Contents")
    print("  3. Search for Student by ID")
    print("  4. Exit")
    print()

    menu_choice = input("Enter your choice (1-4): ").strip()

    # =====================================================================
    # Option 1: Read CSV
    # =====================================================================
    if menu_choice == "1":
        csv_filename = input("Enter the CSV filename (e.g., students.csv): ").strip()

        # Bug 4 Fix: Reset records so reloading does not append duplicates
        student_records = []

        csv_file = open(csv_filename, newline="")
        csv_reader = csv.DictReader(csv_file)

        for row in csv_reader:
            student_id = row["StudentID"]
            student_name = row["StudentName"]
            major = row["Major"]
            gpa = row["GPA"]
            total_credits = row["TotalCredits"]

            student_record = {
                "StudentID": student_id,
                "StudentName": student_name,
                "Major": major,
                "GPA": gpa,
                "TotalCredits": total_credits
            }
            student_records.append(student_record)

        # Bug 1 Fix: Close file after reading rows, not before
        csv_file.close()

        # Bug 3 Fix: Mark csv_loaded as True after successful load
        csv_loaded = True

        print()
        print(f"Success! {len(student_records)} student record(s) loaded from '{csv_filename}'.")

    # =====================================================================
    # Option 2: List CSV Contents
    # =====================================================================
    elif menu_choice == "2":
        if not csv_loaded:
            print()
            print("No data loaded. Please use Option 1 to read a CSV file first.")
        else:
            print()
            # Bug 6 Fix: Changed border width to 82 to align with table width
            print("-" * 82)
            print(f"{'#':<5} {'Student ID':<12} {'Student Name':<22} {'Major':<24} {'GPA':<6} {'Credits'}")
            print("-" * 82)

            row_number = 1
            for current_student in student_records:
                print(
                    f"{row_number:<5}"
                    f"{current_student['StudentID']:<12}"
                    f"{current_student['StudentName']:<22}"
                    f"{current_student['Major']:<24}"
                    f"{current_student['GPA']:<6}"
                    f"{current_student['TotalCredits']}"
                )
                # Bug 5 Fix: Increment row_number for each record
                row_number = row_number + 1

            print("-" * 82)
            print(f"Total records: {len(student_records)}")

    # =====================================================================
    # Option 3: Search for Student by ID
    # =====================================================================
    elif menu_choice == "3":
        if not csv_loaded:
            print()
            print("No data loaded. Please use Option 1 to read a CSV file first.")
        else:
            search_id = input("Enter the Student ID to search for: ").strip()

            # Bug 9 Fix: Reset found_student to None before starting search
            found_student = None
            search_index = 0

            # Bug 8 Fix: Use < instead of <= to prevent IndexError
            while search_index < len(student_records):
                # Bug 10 Fix: Apply .upper() to search_id for case-insensitive search
                if student_records[search_index]["StudentID"].upper() == search_id.upper():
                    found_student = student_records[search_index]
                    search_index = len(student_records)  # Force loop to end
                else:
                    search_index = search_index + 1

            print()
            if found_student is None:
                print(f"No student found with ID '{search_id}'.")
            else:
                print("Student found!")
                print("-" * 40)
                # Bug 2 Fix: Changed key from 'Student_ID' to 'StudentID'
                print(f"  Student ID    : {found_student['StudentID']}")
                print(f"  Student Name  : {found_student['StudentName']}")
                print(f"  Major         : {found_student['Major']}")
                print(f"  GPA           : {found_student['GPA']}")
                print(f"  Total Credits : {found_student['TotalCredits']}")
                print("-" * 40)

    # =====================================================================
    # Option 4: Exit
    # =====================================================================
    # Bug 7 Fix: Compare menu_choice to string "4" instead of integer 4
    elif menu_choice == "4":
        print()
        print("Thank you for using the Student Record Management System. Goodbye!")
        break

    # =====================================================================
    # Invalid Input
    # =====================================================================
    else:
        print()
        print(f"'{menu_choice}' is not a valid option. Please enter 1, 2, 3, or 4.")