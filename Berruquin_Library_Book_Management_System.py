# Library Book Management System
# Tier Level: Base Level
# Author: Rudy Berruquin
# Date: October 2, 2026
class Book:
    """
    A class to represent a library book with checkout/return functionality.
    """

    def __init__(self, title, author, isbn, year, genre):
        # This initializes a Book object with five parameters and sets default attributes.
        self.title = title
        self.author = author
        self.isbn = isbn
        self.year = year
        self.genre = genre
        self.available = True  # Book is available for checkout by default
        self.borrower = None  # No borrower initially

    def __str__(self):
        # Returns a formatted string representing the book's details.
        status = self.get_status()
        return f"{self.isbn:20s}) {self.title:60s} by {self.author:25s}\n {self.year:6d} {self.genre:15s} {status}"

    def check_out(self, customer_name):
        # Checks out a book to a customer if available; otherwise returns False.
        if self.available:
            self.available = False
            self.borrower = customer_name
            return True
        else:
            return False

    def return_book(self):
        # Processes a book being returned and makes it available again.
        self.available = True
        confirmation = f"'{self.title}' has been returned and is now available."
        self.borrower = None
        return confirmation

    def get_status(self):
        # Return a short status string.
        if self.available:
            return "Available"
        else:
            return f"Checked out to {self.borrower}"


if __name__ == "__main__":
    # Create a collection of at least six Book objects
    collection = [
        Book("1984", "George Orwell", "978-0451524935", 1949, "Dystopian"),
        Book("First-Time Home Buyer", "Mindy Jensen/Scott Trench", "978-0997584783", 2021, "Finance"),
        Book("The Hunger Games", "Suzanne Collins", "978-1407132082", 2008, "Dystopian"),
        Book("Red Rising", "Pierce Brown", "978-0345539788", 2014, "Dystopian"),
        Book("Mathematics for Electrical Engineering and Computing", "Mary P. Attenborough", "978-0750658553", 2003, "Mathematics"),
        Book("The Giver", "Lois Lowry", "978-0385732550", 1993, "Dystopian")
    ]

    print("===Full Collection===")
    # Display books
    for book in collection:
        print(book)
        print()

    # Check out a book
    print("\n" + "=" * 60)
    results = collection[0].check_out("Michael")
    if results:
        print(f"'{collection[0].title}' checked out to Michael.")
    else:
        print(f"'{collection[0].title}' is not available for checkout.")

    results2 = collection[1].check_out("Maddy")
    if results2:
        print(f"'{collection[1].title}' checked out to Maddy.")
    else:
        print(f"'{collection[1].title}' is not available for checkout.")

    # Attempt to checkout the first book again (should fail)
    results3 = collection[0].check_out("Autumn")
    if results3:
        print(f"'{collection[0].title}' checked out to Autumn.")
    else:
        print(f"'{collection[0].title}' is not available for checkout.")

    # Return the second checked out book
    print("\n" + "=" * 60)
    return_message = collection[1].return_book()
    print(return_message)

    # Display the collection sorted by title
    print("\n" + "=" * 60)
    print("===Sorted by Title===")
    sorted_collection = sorted(collection, key=lambda b: b.title)
    for book in sorted_collection:
        print(book)
        print()

    # Display only the available books
    print("\n" + "=" * 60)
    print("===Available Books===")
    available_books = [book for book in collection if book.available is True]
    for book in available_books:
        print(book)
        print()

    print("\n" + "=" * 60)
    print("Program completed successfully.")






