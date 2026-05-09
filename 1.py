import json


class ExpenseTracker:
    def __init__(self):
        self.expenses = []

    def add_expense(self, category, amount):
        expense = {
            "category": category,
            "amount": amount
        }
        self.expenses.append(expense)

    def total_expense(self):
        return sum(expense["amount"] for expense in self.expenses)

    def save_to_file(self, filename):
        with open(filename, "w") as file:
            json.dump(self.expenses, file, indent=4)

    def load_from_file(self, filename):
        with open(filename, "r") as file:
            self.expenses = json.load(file)


def main():
    tracker = ExpenseTracker()

    tracker.add_expense("Food", 250)
    tracker.add_expense("Transport", 100)
    tracker.add_expense("Entertainment", 300)

    print("Total Expense:", tracker.total_expense())

    tracker.save_to_file("expenses.json")


if __name__ == "__main__":
    main()