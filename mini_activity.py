# # 230609 - Main Activity

# Activity 1: Building a Library Catalog System

# Objective: Implement a library catalog system using encapsulation principles.

# Instructions:

# Define a class called Book with the following attributes and methods:

# Attributes:

# title : The title of the book.
# author: The author of the book.
# publication_year: The year the book was published.
# is_available: Indicates whether the book is available for borrowing.

# Methods:

# __init__(self, title, author, publication_year): Initializes the book object with the given title, author, and publication year. Set is_available to True by default.
# get_title(self): Returns the title of the book.
# get_author(self): Returns the author of the book.
# get_publication_year(self): Returns the publication year of the book.
# is_book_available(self): Returns the availability status of the book.
# borrow_book(self): Marks the book as borrowed (sets is_available to False).
# return_book(self): Marks the book as returned (sets is_available to True).
# Create a list called library to store the book objects.

# Implement the following functionality in the main program:

# - Prompt the user to enter book details (title, author, publication year).
# - Create a Book object with the provided details and add it to the library list.
# - Repeat the above step to add multiple books to the library.
# - Display the available books in the library.
# - Prompt the user to choose a book to borrow by entering its index.
# -- If the chosen book is available, mark it as borrowed and display a success message. Otherwise, display an error message.
#   --- Display the available books in the library again.
#   --- Prompt the user to choose a book to return by entering its index.
#   --- If the chosen book is not available, mark it as returned and display a success message. Otherwise, display an error message.
#   --- Display the available books in the library one final time.

#  Note: You can use the input() function to get user input and the print() function to display messages and book information.

#  Add your activity GitHub link
#  Screen your code-based and output and paste in our lecture SB account

# Grading:
# 			First 1-10 submission without errors --> 100 points
# 			Second 11-20 submission without errors --> 90 points
# 			Third 21-30 submission without errors --> 85
# 			the rest without errors --> 80
# 			Late submission or submission with error --> 60
# '''

class Book:

    def __init__(self, title, author, publication_year, is_available):
        self.title = title
        self.author = author
        self.publication_year = publication_year
        self.is_available = is_available

    def get_title(self):
        return self.title

    def get_author(self):
        return self.author

    def get_publication_year(self):
        return self.publication_year

    def is_book_available(self):
        return self.is_available

    def borrow_book(self):
        if self.is_available:
            self.is_available = False
            print(f"\n-- \"{self.title}\" was borrowed successfully. --")
        else:
            print(f"\n-- \"{self.title}\" is currently unavailable. --")

    def return_book(self):
        if self.is_available:
            print(f"\n-- \"{self.title}\" is already in the library. --")
        else:
            print(f"\n-- \"{self.title}\" was returned successfully. --")
            self.is_available = True


library = []

while True:

    choice = input("\n[add] = add a book.\n[borrow] = borrow a book.\n[return] = return a book.\n[library] = see "
                   "library list.\n\nEnter input : ").lower()

    if choice in {"add", "borrow", "return", "library"}:
        if choice == "add":
            book_title = input("\nEnter book title: ")
            book_author = input("Enter book author: ")
            book_publication_year = input("Enter book publication year: ")
            library.append(Book(book_title, book_author, book_publication_year, True))
            print(f"\n-- Book successfully added to library. --")

        if choice == "borrow":
            print("\nList of Books in the Library: \n")
            print("[back] ...")
            for books in range(len(library)):
                if library[books].is_book_available():
                    print(
                        f"[{books}] {library[books].get_title()} ({library[books].get_publication_year()}) by {library[books].get_author()} (available)")
                else:
                    print(f"[{books}] {library[books].get_title()} ({library[books].get_publication_year()}) by {library[books].get_author()} (not available)")
            print()

            while True:
                book_choice = input("Which book do you want to borrow? [book index]: ").lower()

                if book_choice == "back":
                    break
                if 0 <= int(book_choice) < len(library):
                    library[int(book_choice)].borrow_book()
                    break
                else:
                    print("Enter a valid index.")

        if choice == "return":
            print("\nList of Books in the Library: \n")
            print("[back] ...")
            for books in range(len(library)):
                if library[books].is_book_available():
                    print(f"[{books}] {library[books].get_title()} ({library[books].get_publication_year()}) by {library[books].get_author()} (available)")
                else:
                    print(f"[{books}] {library[books].get_title()} ({library[books].get_publication_year()}) by {library[books].get_author()} (not available)")
            print()

            while True:
                book_choice = input("Which book do you want to return? [book index]: ").lower()

                if book_choice == "back":
                    break
                if 0 <= int(book_choice) < len(library):
                    library[int(book_choice)].return_book()
                    break
                else:
                    print("Enter a valid index.")

        if choice == "library":
            print("\nList of Books in the Library: \n")
            for books in range(len(library)):
                if library[books].is_book_available():
                    print(
                        f"[{books}] {library[books].get_title()} ({library[books].get_publication_year()}) by {library[books].get_author()}  (available)")
                else:
                    print(f"[{books}] {library[books].get_title()} ({library[books].get_publication_year()}) by {library[books].get_author()} (not available)")
