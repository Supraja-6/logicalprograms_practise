# Employee Wage and Data Management
employees = {}

highest_salary = 0
highest_employee = ""

try:
    n = int(input("Enter number of employees: "))
    for i in range(n):
        print("\nEnter Employee Details")
        emp_id = input("Employee ID: ")
        name = input("Employee Name: ")
        daily_hours = []
        print("Enter working hours for 7 days:")
        for day in range(1, 8):
            while True:
                try:
                    hours = float(input(f"Day {day}: "))
                    daily_hours.append(hours)
                    break
                except ValueError:
                    print("Please enter valid numeric hours")
        salary_per_hour = float(input("Enter salary per hour: "))

        # Calculating the totol hours 
        total_hours = 0
        for h in daily_hours:
            total_hours += h

        # Calculate weekly wage by total hours to salary per hour
        weekly_wage = total_hours * salary_per_hour

        bonus = 0
        if total_hours > 40:
            bonus = weekly_wage * 0.10

        total_wage = weekly_wage + bonus

        # Daily wages using list comprehension
        daily_wages = [h * salary_per_hour for h in daily_hours]

        # Store employee data
        employees[emp_id] = {
            "Name": name,
            "Daily Hours": daily_hours,
            "Daily Wages": daily_wages,
            "Total Hours": total_hours,
            "Salary Per Hour": salary_per_hour,
            "Weekly Wage": weekly_wage,
            "Bonus": bonus,
            "Total Wage": total_wage
        }

        # Save to file
        with open("employee_data.txt", "a") as file:
            file.write(f"{emp_id} - {name} - Total Wage: {total_wage}\n")

        # Find highest earning employee
        if total_wage > highest_salary:
            highest_salary = total_wage
            highest_employee = name

        print("Employee record saved successfully")

    print("\nHighest Earning Employee:", highest_employee)
    print("Highest Weekly Salary:", highest_salary)
except ValueError:
    print("Invalid input! Please enter correct values.")
