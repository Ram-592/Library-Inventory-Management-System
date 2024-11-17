# File to store book details
FILENAME = "books.txt"

# Function to add a book
def add_book():
    with open(FILENAME, "a") as file:
        book_id = input("Enter Book ID: ")
        title = input("Enter Book Title: ")
        author = input("Enter Author Name: ")
        copies = input("Enter Number of Copies: ")
        file.write(f"{book_id},{title},{author},{copies}\n")
        print("Book added successfully!")

# Function to view all books
def view_books():
    try:
        with open(FILENAME, "r") as file:
            print("\nLibrary Books:")
            print("ID\tTitle\t\tAuthor\t\tCopies")
            print("-" * 40)
            for line in file:
                book_id, title, author, copies = line.strip().split(",")
                print(f"{book_id}\t{title}\t\t{author}\t\t{copies}")
    except FileNotFoundError:
        print("No books found! Add a book first.")

# Function to search for a book by ID
def search_book():
    book_id = input("Enter Book ID to search: ")
    found = False
    try:
        with open(FILENAME, "r") as file:
            for line in file:
                record = line.strip().split(",")
                if record[0] == book_id:
                    print("\nBook Found:")
                    print("ID:", record[0])
                    print("Title:", record[1])
                    print("Author:", record[2])
                    print("Copies:", record[3])
                    found = True
                    break
        if not found:
            print("Book not found!")
    except FileNotFoundError:
        print("No books found! Add a book first.")

# Function to update book details
def update_book():
    book_id = input("Enter Book ID to update: ")
    updated_lines = []
    found = False
    try:
        with open(FILENAME, "r") as file:
            for line in file:
                record = line.strip().split(",")
                if record[0] == book_id:
                    found = True
                    print("Enter new details:")
                    title = input("Enter Book Title: ")
                    author = input("Enter Author Name: ")
                    copies = input("Enter Number of Copies: ")
                    updated_lines.append(f"{book_id},{title},{author},{copies}\n")
                else:
                    updated_lines.append(line)
        if found:
            with open(FILENAME, "w") as file:
                file.writelines(updated_lines)
            print("Book details updated successfully!")
        else:
            print("Book not found!")
    except FileNotFoundError:
        print("No books found! Add a book first.")

# Function to delete a book
def delete_book():
    book_id = input("Enter Book ID to delete: ")
    updated_lines = []
    found = False
    try:
        with open(FILENAME, "r") as file:
            for line in file:
                record = line.strip().split(",")
                if record[0] == book_id:
                    found = True
                else:
                    updated_lines.append(line)
        if found:
            with open(FILENAME, "w") as file:
                file.writelines(updated_lines)
            print("Book deleted successfully!")
        else:
            print("Book not found!")
    except FileNotFoundError:
        print("No books found! Add a book first.")

# Main Menu
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
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.")

# Run the program
if __name__ == "__main__":
    main()
