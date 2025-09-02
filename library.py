from collections import Counter

borrow_records = {
    "Alice": {"Harry Potter": 3, "Lord of the Rings": 2},
    "Bob": {"Harry Potter": 5},
    "Charlie": {"Game of Thrones": 0},
    "Diana": {"Lord of the Rings": 1}
}

def average_books_borrowed(records):
    total_books = 0
    total_members = len(records)
    for books in records.values():
        total_books += sum(books.values())
    if total_members == 0:
        return 0
    return total_books / total_members

def highest_and_lowest_borrowed_books(records):
    book_counts = Counter()
    for books in records.values():
        for book, count in books.items():
            book_counts[book] += count
    if not book_counts:
        return None, None
    highest = max(book_counts.items(), key=lambda x: x[1])
    lowest = min(book_counts.items(), key=lambda x: x[1])
    return highest, lowest

def count_members_with_zero_borrows(records):
    count = 0
    for books in records.values():
        if sum(books.values()) == 0:
            count += 1
    return count

def most_frequently_borrowed_book(records):
    book_counts = Counter()
    for books in records.values():
        for book, count in books.items():
            book_counts[book] += count
    if not book_counts:
        return None
    return book_counts.most_common(1)[0]

# Using the functions:

print(f"Average books borrowed per member: {average_books_borrowed(borrow_records):.2f}")

highest, lowest = highest_and_lowest_borrowed_books(borrow_records)
print(f"Most borrowed book: {highest[0]} ({highest[1]} times)")
print(f"Least borrowed book: {lowest[0]} ({lowest[1]} times)")

zero_borrowers = count_members_with_zero_borrows(borrow_records)
print(f"Members who borrowed no books: {zero_borrowers}")

most_frequent = most_frequently_borrowed_book(borrow_records)
print(f"Most frequently borrowed book: {most_frequent[0]} ({most_frequent[1]} times)")
