"""
Author: Rudy Berruquin
Date September 20, 2026
Assignment: Personal Expense Tracker (Week 4)
Tier level: Base Level
Description: A personal expense tracker that records daily expenses into a plain text file and displays saved records in a neatly aligned table format.

Testing scenarios and results:
1. First run (no file exists):
    - load_records() caught FileNotFoundError and returned an empty list.
    - Displayed: "No expenses on record yet."
2. Added two expenses and exited; ran again:
    - Both saved records loaded properly and displayed on the second run.
3. Long description check:
    - Entered a 40-character description; verified it was truncated on the second run.
4. Added 0 expenses:
    - Loop executed 0 times; displayed existing records without modification.
5.Column alignment check:
    - Header and all row values lined up neatly under fixed column widths.
"""

import datetime
import os

def build_record(description, amount, category):

    """
    Builds a single comma-seperated record string.
    Caps description to 30 characters for formats amount to 2 decimal places.
     """
    #Get today's date as a string
    today_date = str(datetime.date.today())

    #Slice description so it will not exceed 30 characters
    short_description = description[:30]

    #Format the numeric amount to two decimal places
    formatted_amount = f"{amount:.2f}"

    #Combine all four fields into one comma-seperated string
    record_fields = [today_date, short_description, formatted_amount, category]
    record_line = ",".join(record_fields)

    return record_line

def load_records(filename):
    """
    Reads records from a text file and returns tham as a list of lists.
    Catches FileNotFoundError if the file does not exist yet    
    """

    records = []

    try:
        #Open file read mode
        with open(filename, "r") as file:
            for line in file:
                #Remove leading/trailing whitespace and newline characters
                clean_line = line.strip()

                ##skip blank lines if any exist
                if clean_line !="":
                    fields = clean_line.split(",")
                    records.append(fields)

    except FileNotFoundError:
        #Return an empty list if the file does not exist yet
        return[]
    return records

def clear_records(filename):
    """Removes all saved expense records from the file."""
    with open(filename, "w"):
        pass

def display_records(records):

    """
    Prints all expense records in an aligned format.
    """

    if not records:
        print("No expenses on record yet.")
        return

    #Print table header with fixed column widths
    print(f"{'Date':<12}{'Description':<32}{'Amount':<10}{'Category':<15}")
    print("-"*75)

    #Print each expense row
    for record in records:
        date = record[0]
        description = record[1]
        amount = f"${float(record[2]):.2f}"
        category = record[3]

        print(f"{date:<12}{description:<32}{amount:<10}{category:<15}")

# Main program
if __name__ == "__main__":
    filename = "expense.txt"

    print("=====Expense Records=====")

    #1. Load and display existing records
    saved_records = load_records(filename)
    display_records(saved_records)
    print()

    clear_choice = input("Clear all saved records? (y/n): ").strip().lower()
    if clear_choice == "y":
        clear_records(filename)
        saved_records = []
        print("All expense records were cleared.")
    print()

    #2. Ask user how many expenses to add
    count = int(input("How many expenses do you want to add? "))

    #3. Collect entries in aloop and append each to the file
    for i in range (count):
        print(f"\n---Expense {i+1}---")
        description_input = input("Description: ")
        amount_input = float(input("Amount: "))
        category_input = input("Category: ")

        #Create formatted record string
        new_record_line = build_record(
            description_input, amount_input, category_input
        )

        #Append to the text file insode a dedicated open call
        with open(filename, "a") as file:
            file.write(new_record_line + "\n")

    #4. Reloadand display updated records
    print("\n=====Updated expense Records=====")
    updated_records = load_records(filename)
    display_records(updated_records)
