# library_management.py

class Book:
    """
    Represents a single book in the library.
    Public attributes  : title, author
    Private attribute  : _is_checked_out  (bool)
    """

    def __init__(self, title: str, author: str):
        self.title = title
        self.author = author
        self._is_checked_out = False  # starts available

    # ---------- Behaviour ----------
    def check_out(self) -> bool:
        """
        Mark book as checked out.
        Returns True if the operation succeeds, False if it was already out.
        """
        if self._is_checked_out:
            return False
        self._is_checked_out = True
        return True

    def return_book(self) -> bool:
        """
        Mark book as returned / available.
        Returns True if the operation succeeds, False if it was already in.
        """
        if not self._is_checked_out:
            return False
        self._is_checked_out = False
        return True

    def is_available(self) -> bool:
        """True if the book is not checked out."""
        return not self._is_checked_out

    # ---------- Pretty‐print ----------
    def __str__(self):
        return f"{self.title} by {self.author}"


class Library:
    """
    Manages a collection of Book objects.
    """

    def __init__(self):
        self._books: list[Book] = []

    # ---------- Collection management ----------
    def add_book(self, book: Book) -> None:
        """Add a new Book instance to the collection."""
        self._books.append(book)

    # ---------- User actions ----------
    def check_out_book(self, title: str) -> None:
        """
        Attempt to check out the first available copy matching `title`.
        If no available copy is found, print a helpful message.
        """
        for book in self._books:
            if book.title == title and book.is_available():
                book.check_out()
                return
        print(f"No available copy of '{title}' found.")

    def return_book(self, title: str) -> None:
        """
        Attempt to return the first checked‑out copy matching `title`.
        If none are checked out, print a helpful message.
        """
        for book in self._books:
            if book.title == title and not book.is_available():
                book.return_book()
                return
        print(f"No checked‑out copy of '{title}' to return.")

    # ---------- Display ----------
    def list_available_books(self) -> None:
        """Print all books that are currently available."""
        available = [book for book in self._books if book.is_available()]
        if not available:
            print("No books available.")
        else:
            for book in available:
                print(book)
