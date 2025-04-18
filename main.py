import csv

FILENAME = "books.csv"

# Check if a book ID already exists
def book_exists(book_id):
    try:
        with open(FILENAME, "r", newline="") as file:
            reader = csv.reader(file)
            for row in reader:
                if row[0] == book_id:
                    return True
    except FileNotFoundError:
        return False
    return False

# Check if book with same title, author and copies exists (to avoid duplicates)
def book_data_exists(title, author, copies, exclude_id=None):
    try:
        with open(FILENAME, "r", newline="") as file:
            reader = csv.reader(file)
            for row in reader:
                if exclude_id and row[0] == exclude_id:
                    continue
                if row[1] == title and row[2] == author and row[3] == copies:
                    return True
    except FileNotFoundError:
        return False
    return False

# Add a new book
def add_book():
    book_id = input("Enter Book ID: ")
    if book_exists(book_id):
        print("Book ID already exists!")
        return

    title = input("Enter Book Title: ")
    author = input("Enter Author Name: ")
    copies = input("Enter Number of Copies: ")

    if book_data_exists(title, author, copies):
        print("This book already exists with different ID!")
        return

    with open(FILENAME, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([book_id, title, author, copies])
        print("Book added successfully!")

# Show all books
def view_books():
    try:
        with open(FILENAME, "r", newline="") as file:
            reader = csv.reader(file)
            print("\nBooks in Library:")
            print("ID\tTitle\tAuthor\tCopies")
            print("-" * 30)
            for row in reader:
                print(f"{row[0]}\t{row[1]}\t{row[2]}\t{row[3]}")
    except FileNotFoundError:
        print("No books found!")

# Search a book by ID
def search_book():
    book_id = input("Enter Book ID to search: ")
    found = False
    try:
        with open(FILENAME, "r", newline="") as file:
            reader = csv.reader(file)
            for row in reader:
                if row[0] == book_id:
                    print("\nBook Found:")
                    print("ID:", row[0])
                    print("Title:", row[1])
                    print("Author:", row[2])
                    print("Copies:", row[3])
                    found = True
                    break
        if not found:
            print("Book not found!")
    except FileNotFoundError:
        print("No books found!")

# Update book details
def update_book():
    book_id = input("Enter Book ID to update: ")
    if not book_exists(book_id):
        print("Book not found!")
        return

    title = input("Enter new Title: ")
    author = input("Enter new Author: ")
    copies = input("Enter new Copies: ")

    if book_data_exists(title, author, copies, exclude_id=book_id):
        print("Another book with same details already exists!")
        return

    updated_rows = []
    with open(FILENAME, "r", newline="") as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == book_id:
                updated_rows.append([book_id, title, author, copies])
            else:
                updated_rows.append(row)

    with open(FILENAME, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(updated_rows)
        print("Book updated successfully!")

# Delete a book
def delete_book():
    book_id = input("Enter Book ID to delete: ")
    updated_rows = []
    found = False
    try:
        with open(FILENAME, "r", newline="") as file:
            reader = csv.reader(file)
            for row in reader:
                if row[0] != book_id:
                    updated_rows.append(row)
                else:
                    found = True

        if found:
            with open(FILENAME, "w", newline="") as file:
                writer = csv.writer(file)
                writer.writerows(updated_rows)
            print("Book deleted successfully!")
        else:
            print("Book not found!")
    except FileNotFoundError:
        print("No books found!")

# Main menu
def main():
    while True:
        print("\nLibrary Book Management System")
        print("1. Add Book")
        print("2. View Books")
        print("3. Search Book")
        print("4. Update Book")
        print("5. Delete Book")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_book()
        elif choice == "2":
            view_books()
        elif choice == "3":
            search_book()
        elif choice == "4":
            update_book()
        elif choice == "5":
            delete_book()
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice!")

# Run the program
if __name__ == "__main__":
    main()
