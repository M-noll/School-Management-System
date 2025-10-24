import json
import os

class FeeNode:
    def __init__(self, student_id, amount):
        self.student_id = student_id
        self.amount = amount
        self.left = None
        self.right = None

class FeeBST:
    def __init__(self, filename="fees.json"):
        self.root = None
        self.filename = filename
        self.load_fees()

    def insert(self, student_id, amount):
        """Insert or update fee for a student"""
        self.root = self._insert(self.root, student_id, amount)
        self.save_fees()

    def _insert(self, node, student_id, amount):
        if node is None:
            return FeeNode(student_id, amount)
        if student_id < node.student_id:
            node.left = self._insert(node.left, student_id, amount)
        elif student_id > node.student_id:
            node.right = self._insert(node.right, student_id, amount)
        else:
            node.amount += amount  # update existing
        return node

    def in_order(self):
        """Return all fees in-order"""
        result = []
        self._in_order(self.root, result)
        return result

    def _in_order(self, node, result):
        if node:
            self._in_order(node.left, result)
            result.append({"student_id": node.student_id, "amount": node.amount})
            self._in_order(node.right, result)

    def save_fees(self):
        """Save BST to JSON (flattened)"""
        data = self.in_order()
        with open(self.filename, "w") as f:
            json.dump(data, f, indent=4)

    def load_fees(self):
        """Load fees from JSON and rebuild BST"""
        if os.path.exists(self.filename):
            with open(self.filename, "r") as f:
                data = json.load(f)
                for entry in data:
                    self.root = self._insert(self.root, entry["student_id"], entry["amount"])
