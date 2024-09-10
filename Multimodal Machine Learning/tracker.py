# # Basic expense tracker that allows to add, view and calculate expenses
# expenses = []

# def add_expense():
#     amount = float(input("Enter the expense amount: "))
#     expenses.append(amount)
#     print("Expense added successfully!")

# def view_expenses():
#     print("Expenses:")
#     for i, expense in enumerate(expenses, start=1):
#         print(f"{i}. {expense}")

# def calculate_total():
#     total = sum(expenses)
#     print(f"Total expenses: {total}")

# def main():
#     while True:
#         print("1. Add Expense")
#         print("2. View Expenses")
#         print("3. Calculate Total")
#         print("4. Exit")
#         choice = input("Enter your choice: ")

#         if choice == "1":
#             add_expense()
#         elif choice == "2":
#             view_expenses()
#         elif choice == "3":
#             calculate_total()
#         elif choice == "4":
#             break
#         else:
#             print("Invalid choice. Please try again.")

# if __name__ == "__main__":
#     main()

nums = [2, 7, 11, 15]
target = 9

num_dict = {}
for i, num in enumerate(nums):
    num_dict[num] = i

print(num_dict[7])