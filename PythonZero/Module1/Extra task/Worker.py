cpfList = []
employeeSalary = []
totalHoursPerEmployee = []

print("Let's calculate the total each employee received in the last 3 months and the total expenses." + "\n")

numOfEmployees = int(input("Enter the number of employees you want to add:"))

for x in range(numOfEmployees):

  cpf = input("Enter the employee's CPF:" + "\n")
  cpfList.append(cpf)

  position = int(input(
    """Enter the position: 
    Enter 1 for salesperson
    Enter 2 for general manager 
    Enter 3 for HR analyst
    Enter 4 for financial analyst
    Enter 5 for buyer
    Enter 6 for administrative assistant 
    Enter 7 for janitor
    What is the employee's position:?"""))

  for i in range(3):
    i += 0
    hoursPerMonth = float(input("Enter how many hours the employee worked in the %dº month:" % (i + 1) + "\n"))
    # constants
    hourSalary = float(input("How much does the employee receive per hour worked in the %dº month:" % (i + 1) + "\n"))

    if position == 1:

      totalSales = float(input("How many clothing items did the employee sell in the %dº month:" % (i + 1) + "\n"))

      if 1 <= totalSales <= 50:
        monthlySalary = (hoursPerMonth * hourSalary) + 70
      elif 51 <= totalSales <= 100:
        monthlySalary = (hoursPerMonth * hourSalary) + 110
      elif totalSales > 100:
        monthlySalary = (hoursPerMonth * hourSalary) + 200
    elif 2 <= position <= 7:
      monthlySalary = hoursPerMonth * hourSalary
    else:
      print("Enter a valid position.")

    monthlySalary += monthlySalary + monthlySalary
    hoursPerMonth += hoursPerMonth + hoursPerMonth

  employeeSalary.append(monthlySalary)
  totalHoursPerEmployee.append(hoursPerMonth)

for c in range(numOfEmployees):
  print("The employee with CPF:", cpfList[c],
        "received in these 3 months:", employeeSalary[c],
        "and worked:", totalHoursPerEmployee[c], "hours" + "\n")

print("The payroll for these 3 months for employees was:", sum(employeeSalary))

# another way

payrollTotal = 0

for x in range(3):
    while True:

        cpf = int(input('Enter your CPF using only numbers: '))
        hoursWorked = int(input('Enter the number of hours worked: '))
        hourlyRate = float(input('Enter the employee\'s hourly rate: '))
        position = int(input('Enter the position: Enter 1 for salesperson, \n Enter 2 for general manager, \n Enter 3 for HR analyst, \n Enter 4 for financial analyst, \n Enter 5 for buyer,\n Enter 6 for administrative assistant, \n Enter 7 for janitor'))

        if position == 1:
            soldPieces = int(input('Enter the number of clothing items sold: '))
            if 1 <= soldPieces <= 50:
                salary = (hoursWorked * hourlyRate) + 70
            elif 51 <= soldPieces <= 100:
                salary = (hoursWorked * hourlyRate) + 110
            elif soldPieces > 100:
                salary = (hoursWorked * hourlyRate) + 200
            else:
                salary = hoursWorked * hourlyRate
            print('The salary is $', salary)
        elif 2 <= position <= 7:
            salary = hoursWorked * hourlyRate
            print('The salary is $', salary)
        else:
            print('Enter a valid position')

        payrollTotal += salary

        option = input('Do you want to input another employee? Type S for Yes or N for No')
        if option == 'N':
            break

print('The payroll total for the last 3 months is $', payrollTotal)





