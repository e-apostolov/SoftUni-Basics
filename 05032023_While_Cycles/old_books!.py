name_of_book_needed = input()
books_checked = 0

while True:
    book_name = input()
    books_checked += 1
    if book_name == "No More Books":
        print("The book you search is not here!")
        print(f"You checked {books_checked - 1} books.")
        break
    if book_name == name_of_book_needed:
        print(f"You checked {books_checked - 1} books and found it.")
        break








