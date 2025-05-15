expenses = []

def add_expense():
    print("\n--- Add New Expense ---")
    date = input("Enter date (YYYY-MM-DD): ")
    category = input("Enter category (Food, Transport, etc.): ")
    amount = float(input("Enter amount: "))
    description = input("Enter description: ")

    expense = {
        "date": date,
        "category": category,
        "amount": amount,
        "description": description
    }
    expenses.append(expense)
    print("Expense added!\n")

def view_expenses():
    print("\n--- All Expenses ---")
    if not expenses:
        print("No expenses recorded.\n")
        return
    for i, exp in enumerate(expenses, start=1):
        print(f"{i}. {exp['date']} | {exp['category']} | ${exp['amount']} | {exp['description']}")
    print()

def total_by_category():
    print("\n--- Total by Category ---")
    cat = input("Enter category name: ")
    total = sum(exp['amount'] for exp in expenses if exp['category'].lower() == cat.lower())
    print(f"Total spent in '{cat}': ${total:.2f}\n")

def delete_expense():
    view_expenses()
    idx = input("Enter expense number to delete: ")
    if idx.isdigit():
        idx = int(idx)
        if 1 <= idx <= len(expenses):
            deleted = expenses.pop(idx - 1)
            print(f"Deleted: {deleted['description']} - ${deleted['amount']}\n")
        else:
            print("Invalid number.\n")
    else:
        print("Invalid input.\n")

def main():
    while True:
        print("=== Expense Tracker ===")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. Total by Category")
        print("4. Delete an Expense")
        print("5. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            add_expense()
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            total_by_category()
        elif choice == '4':
            delete_expense()
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid choice.\n")

main()
