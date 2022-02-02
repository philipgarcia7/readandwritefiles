import csv

employees = open("employeepay.csv", "r")

employee_file = csv.reader(employees, delimiter=",")

# to skip a line if the file contains a header record
next(employee_file)

for record in employee_file:
    print("First Name:", record[1])

    print("Last Name:", record[2])

    print("Salary: $", record[3])

    salary = float(record[3])
    bonper = float(record[4])
    bonus = salary * bonper

    print("Bonus: $", bonus)

    total_pay = bonus + salary
    print("Total Pay: $", total_pay)
    input("Press enter to continue to next employee data:")
