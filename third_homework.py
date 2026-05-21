# #TASK#1 - Calculator
# while True:
#     first_input = input("Enter the first number (or 'q' to quit): ").strip()
    
#     if first_input.lower() == 'q':
#         print("Calculator stopped.")
#         break

#     second_input = input("Enter the second number: ").strip()

#     operation = input("Enter the operation (+, -, *, /, **): ").strip()

#     try:
       num1, num2 = float(first_input), float(second_input)

#         if operation == "+":
#             result = num1 + num2
#         elif operation == "-":
#             result = num1 - num2
#         elif operation == "*":
#             result = num1 * num2
#         elif operation == "/":
#             if num2 == 0:
#                 print("Error: division by zero")
#                 continue
#             result = num1 / num2
#         elif operation == "**":
#             result = num1 ** num2
#         else:
#             print("Invalid operation. Please enter one of +, -, *, /, **.")
#             continue

#         print("Result:", result)

#     except ValueError:
#         print("Error: please enter valid numbers")

#TASK#2 - Expense tracking by categories
while True:
    balance_input = input("Enter your total balance: ").strip()
    try:
        balance = float(balance_input)
        if balance <= 0:
            print("Error: balance must be greater than zero")
            continue
        break
    except ValueError:
        print("Error: please enter a valid number")

expenses = {}

while True:
    print(f"\nTotal balance: {balance:.2f}")
    print("Expenses by category:")

    if expenses:
        for category, amount in expenses.items():
            print(f"{category}: {amount:.2f}")
    else:
        print("No expenses yet")

    category = input("\nChoose a category where you spent money (or type 'q' to finish): ").strip().lower()
    if category == "q":
        print("Program stopped.")
        break

    amount_input = input("Enter the expense amount: ").strip()
    try:
        amount = float(amount_input)
    except ValueError:
        print("Error: please enter a valid number")
        continue

    if amount <= 0:
        print("Error: expense amount must be greater than zero")
        continue

    if balance - amount < 0:
        print("Insufficient funds for this expense")
        continue

    balance -= amount

    expenses[category] = expenses.get(category, 0) + amount