revenue = int(input('Enter tne revenue: '))
costs = int(input('Enter tne costs: '))

if revenue > costs:
    print('The company is profitable')
    profitability = (revenue - costs) / costs
    print('Profitability is ', profitability*100, '%')
    employees = int(input('Enter the number of employees: '))
    profit_per_employee = (revenue - costs) / employees
    print('Profit per employee is', profit_per_employee)
else:
    print('The company has some financial problems')

