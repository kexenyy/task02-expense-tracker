from datetime import datetime

expenses = []

while True:
    date = input("Enter date: ")
    category = input("Enter category: ")
    amount = float(input("Enter amount: "))

    valid_date = True

    try:
        datetime.strptime(date, "%Y-%m-%d")
    except ValueError:
        valid_date = False
        print("Invalid date")

    if valid_date and amount > 0:
        expense = {
            "date": date,
            "category": category,
            "amount": amount
        }
        expenses.append(expense)

    elif amount <= 0:
        print("Invalid amount")

    choice = input("Add another expense? (yes/no): ")

    if choice == "no":
        break

totals = {}

for expense in expenses:
    category = expense["category"]
    amount = expense["amount"]

    if category in totals:
        totals[category] += amount
    else:
        totals[category] = amount

print("\n--- Total Spending by Category ---")

for category in totals:
    print(category, ":", totals[category])

import csv

with open("expenses.csv", "w", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=["date", "category", "amount"])
    writer.writeheader()
    writer.writerows(expenses)

print("\nExpenses saved to expenses.csv")