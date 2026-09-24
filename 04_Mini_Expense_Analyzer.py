def get_total(expenses):
    total = 0

    for expense in expenses:
        total += expense

    return total

def show_large_expenses(expenses, limit):
    print(f"Expenses larger than {limit}:")
    for expense in expenses:
        if expense > limit:
            print(expense)

expenses = [250, 400, 120, 600, 300]

Total_expense = get_total(expenses)
print(Total_expense)

user_limit = int(input("Enter the limit: "))
show_large_expenses(expenses,user_limit)
