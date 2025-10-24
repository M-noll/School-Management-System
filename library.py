import json
import os

class LibrarySystem:
    def __init__(self, filename="library.json"):
        self.filename = filename
        self.books = {}  # Hash map: ISBN -> {"title": str, "available": int}
        self.borrow_history = []  # Stack to track borrow/return history
        self.load_library()

    def add_book(self, isbn, title, quantity=1):
        if isbn in self.books:
            self.books[isbn]["available"] += quantity
        else:
            self.books[isbn] = {"title": title, "available": quantity}
        self.save_library()

    def borrow_book(self, isbn, student_id):
        if isbn in self.books and self.books[isbn]["available"] > 0:
            self.books[isbn]["available"] -= 1
            self.borrow_history.append({"action": "borrow", "isbn": isbn, "student_id": student_id})
            self.save_library()
            return True
        return False  # Book unavailable

    def return_book(self, isbn, student_id):
        if isbn in self.books:
            self.books[isbn]["available"] += 1
            self.borrow_history.append({"action": "return", "isbn": isbn, "student_id": student_id})
            self.save_library()
            return True
        return False

    def check_availability(self, isbn):
        return self.books.get(isbn, {}).get("available", 0)

    def save_library(self):
        with open(self.filename, "w") as f:
            json.dump({"books": self.books, "borrow_history": self.borrow_history}, f, indent=4)

    def load_library(self):
        if os.path.exists(self.filename):
            with open(self.filename, "r") as f:
                data = json.load(f)
                self.books = data.get("books", {})
                self.borrow_history = data.get("borrow_history", [])
        else:
            self.books = {}
            self.borrow_history = []
