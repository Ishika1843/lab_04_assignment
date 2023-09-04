## Define the employee data as a list of dictionaries
employee_data = [
    {"Employee ID": "161E90", "Name": "Raman", "Age": 41, "Salary (PM)": 56000},
    {"Employee ID": "161F91", "Name": "Himadri", "Age": 38, "Salary (PM)": 67500},
    {"Employee ID": "161F99", "Name": "Jaya", "Age": 51, "Salary (PM)": 82100},
    {"Employee ID": "171E20", "Name": "Tejas", "Age": 30, "Salary (PM)": 55000},
    {"Employee ID": "171G30", "Name": "Ajay", "Age": 45, "Salary (PM)": 44000}
]

# Function to sort and print the employee data based on the chosen parameter
def sort_and_print_employee_data(sort_parameter):
    if sort_parameter == 1:
        sorted_data = sorted(employee_data, key=lambda x: x["Age"])
    elif sort_parameter == 2:
        sorted_data = sorted(employee_data, key=lambda x: x["Name"])
    elif sort_parameter == 3:
        sorted_data = sorted(employee_data, key=lambda x: x["Salary (PM)"])
    else:
        print("Invalid sorting parameter")
        return

    print("{:<12} {:<10} {:<4} {:<12}".format("Employee ID", "Name", "Age", "Salary (PM)"))
    print("-" * 42)
    for employee in sorted_data:
        print("{:<12} {:<10} {:<4} {:<12}".format(
            employee["Employee ID"], employee["Name"], employee["Age"], employee["Salary (PM)"]))

# Get user input for sorting parameter
print("Choose a sorting parameter:")
print("1. Age")
print("2. Name")
print("3. Salary")
sort_parameter = int(input("Enter your choice (1/2/3): "))

# Call the function to sort and print the data
sort_and_print_employee_data(sort_parameter)
