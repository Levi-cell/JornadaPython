accounts = []
dailyRevenue = 0

def openAccount(tableNumber, waiterName):
    account = {
        'tableNumber': tableNumber,
        'soldItems': [],
        'waiterName': waiterName,
        'totalValue': 0
    }
    accounts.append(account)
    print(f'Account opened for table {tableNumber} with waiter {waiterName}.')

def addItem(tableNumber, item, quantity, value):
    for account in accounts:
        if account['tableNumber'] == tableNumber:
            account['soldItems'].append({
                'item': item,
                'quantity': quantity,
                'value': value
            })
            account['totalValue'] += value * quantity
            print(f'{quantity}x {item} added to the account of table {tableNumber}.')
            return
    print(f'Table {tableNumber} not found.')

def tip(tableNumber):
    for account in accounts:
        if account['tableNumber'] == tableNumber:
            tipValue = account['totalValue'] * 0.1
            account['totalValue'] += tipValue
            print(f'10% tip added to the account of table {tableNumber}.')
            return
    print(f'Table {tableNumber} not found.')

def closeAccount(tableNumber):
    for account in accounts:
        if account['tableNumber'] == tableNumber:
            print(f'Account for table {tableNumber}:')
            print(f'Waiter: {account["waiterName"]}')
            print('Items:')
            for item in account['soldItems']:
                print(f'{item["quantity"]}x {item["item"]}: ${item["value"]}')
            print(f'Total: ${account["totalValue"]}')
            tip(tableNumber)
            accounts.remove(account)
            return
    print(f'Table {tableNumber} not found.')

def endOfDay():
    global dailyRevenue
    for account in accounts:
        dailyRevenue += account['totalValue']
    print(f'Daily revenue: ${dailyRevenue}')


# Example of usage:

while True:
    print('--- Restaurant ---')
    print('1. Open account')
    print('2. Add item')
    print('3. Close account')
    print('4. End of day')
    option = input('Choose an option: ')

    if option == '1':
        tableNumber = input('Enter the table number: ')
        waiterName = input('Enter the waiter\'s name: ')
        openAccount(tableNumber, waiterName)
    elif option == '2':
        tableNumber = input('Enter the table number: ')
        item = input('Enter the item name: ')
        quantity = int(input('Enter the quantity: '))
        value = float(input('Enter the unit value: '))
        addItem(tableNumber, item, quantity, value)
    elif option == '3':
        tableNumber = input('Enter the table number: ')
        closeAccount(tableNumber)
    elif option == '4':
        endOfDay()
        break
    else:
        print('Invalid option. Try again.')