# Smart Expense Tracker

expenses = []

def add_expense():
    date = input("Enter date (DD-MM-YYYY): ")
    category = input("Enter category (Food/Travel/Other): ")
    amount = float(input("Enter amount: "))
    expenses.append({"date": date, "category": category, "amount": amount})
    print("Expense added successfully!\n")

def view_expenses():
    if not expenses:
        print("No expenses found.\n")
        return
    print("\nDate\t\tCategory\tAmount")
    print("-" * 40)
    for exp in expenses:
        print(f"{exp['date']}\t{exp['category']}\t\t₹{exp['amount']}")
    print()

def total_expense():
    total = sum(exp["amount"] for exp in expenses)
    print(f"\nTotal Expense: ₹{total}\n")

def menu():
    while True:
        print("==== Smart Expense Tracker ====")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. View Total Expense")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            total_expense()
        elif choice == "4":
            print("Exiting application. Thank you!")
            break
        else:
            print("Invalid choice. Try again.\n")

menu()
