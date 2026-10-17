"""
Student Records Assignment
Tier Level: Assignement + attempt at bonus
Date: October 15, 2026
Author: Rudy Berruquin
"""
import csv


class Student:
    """Class to hold information for one student."""

    def __init__(self, student_id, student_name, major, gpa, total_credits):
        # Save all student info and strip extra spaces
        self.student_id = student_id.strip()
        self.student_name = student_name.strip()
        self.major = major.strip()
        self.gpa = gpa.strip()
        self.total_credits = total_credits.strip()

    def __str__(self):
        # Return a nicely formatted block of text with student details
        output = "-" * 40 + "\n"
        output += f"  Student ID    : {self.student_id}\n"
        output += f"  Student Name  : {self.student_name}\n"
        output += f"  Major         : {self.major}\n"
        output += f"  GPA           : {self.gpa}\n"
        output += f"  Total Credits : {self.total_credits}\n"
        output += "-" * 40
        return output


class GraduateStudent(Student):
    """Subclass for graduate students with a thesis topic."""

    def __init__(self, student_id, student_name, major, gpa, total_credits, thesis_topic="N/A"):
        # Call the parent constructor first
        super().__init__(student_id, student_name, major, gpa, total_credits)
        self.thesis_topic = thesis_topic.strip()

    def __str__(self):
        # Format output including the thesis topic
        output = "-" * 40 + "\n"
        output += f"  Student ID    : {self.student_id}\n"
        output += f"  Student Name  : {self.student_name}\n"
        output += f"  Major         : {self.major}\n"
        output += f"  GPA           : {self.gpa}\n"
        output += f"  Total Credits : {self.total_credits}\n"
        output += f"  Thesis Topic  : {self.thesis_topic}\n"
        output += "-" * 40
        return output


class StudentRoster:
    """Class to manage the list of students and menu actions."""

    def __init__(self):
        # Start with an empty list and track if CSV is loaded
        self.students = []
        self.csv_loaded = False
        self.current_filename = ""

    def load_csv(self, filename):
        """Opens and reads the student CSV file."""
        temp_students = []
        try:
            with open(filename, mode="r", newline="") as csv_file:
                csv_reader = csv.DictReader(csv_file)
                for row in csv_reader:
                    # Create a Student object from each row
                    student = Student(
                        row["StudentID"],
                        row["StudentName"],
                        row["Major"],
                        row["GPA"],
                        row["TotalCredits"]
                    )
                    temp_students.append(student)

            # Save the loaded list and sort it for binary search
            self.students = temp_students
            self.students.sort(key=lambda s: s.student_id.upper())
            self.csv_loaded = True
            self.current_filename = filename

            print()
            print(f"Success! {len(self.students)} student record(s) loaded from '{filename}'.")
            return True

        except FileNotFoundError:
            print()
            print(f"Error: File '{filename}' was not found. Please check the name and try again.")
            return False
        except KeyError as err:
            print()
            print(f"Error reading CSV: Missing column {err}.")
            return False
        except Exception as err:
            print()
            print(f"An unexpected error occurred: {err}")
            return False

    def list_students(self):
        """Prints all students in a table format."""
        if not self.csv_loaded:
            print()
            print("No data loaded. Please use Option 1 to read a CSV file first.")
            return

        print()
        print("-" * 82)
        print(f"{'#':<5} {'Student ID':<12} {'Student Name':<22} {'Major':<24} {'GPA':<6} {'Credits'}")
        print("-" * 82)

        # Loop through and print each student with a row number
        row_number = 1
        for student in self.students:
            print(
                f"{row_number:<5}"
                f"{student.student_id:<12}"
                f"{student.student_name:<22}"
                f"{student.major:<24}"
                f"{student.gpa:<6}"
                f"{student.total_credits}"
            )
            row_number = row_number + 1

        print("-" * 82)
        print(f"Total records: {len(self.students)}")

    def search_by_id(self, search_id):
        """Uses binary search to find a student by ID."""
        if not self.csv_loaded:
            print()
            print("No data loaded. Please use Option 1 to read a CSV file first.")
            return

        clean_id = search_id.strip().upper()
        low = 0
        high = len(self.students) - 1
        found_student = None

        # Binary search loop
        while low <= high:
            mid = (low + high) // 2
            current_id = self.students[mid].student_id.upper()

            if current_id == clean_id:
                found_student = self.students[mid]
                break
            elif current_id < clean_id:
                low = mid + 1
            else:
                high = mid - 1

        print()
        if found_student is None:
            print(f"No student found with ID '{search_id.strip()}'.")
        else:
            print("Student found!")
            print(found_student)

    def display_menu(self):
        """Shows the menu choices to the user."""
        print()
        print("Please select an option:")
        print("  1. Read CSV")
        print("  2. List CSV Contents")
        print("  3. Search for Student by ID")
        print("  4. Exit")
        print()

    def run(self):
        """Runs the main menu loop."""
        print("=" * 60)
        print("       Student Record Management System")
        print("=" * 60)

        while True:
            self.display_menu()
            menu_choice = input("Enter your choice (1-4): ").strip()

            if menu_choice == "1":
                filename = input("Enter the CSV filename (e.g., students.csv): ").strip()
                self.load_csv(filename)
            elif menu_choice == "2":
                self.list_students()
            elif menu_choice == "3":
                search_id = input("Enter the Student ID to search for: ").strip()
                self.search_by_id(search_id)
            elif menu_choice == "4":
                print()
                print("Thank you for using the Student Record Management System. Goodbye!")
                break
            else:
                print()
                print(f"'{menu_choice}' is not a valid option. Please enter 1, 2, 3, or 4.")


if __name__ == "__main__":
    roster = StudentRoster()
    roster.run()
