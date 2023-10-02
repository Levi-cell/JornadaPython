def openAccount():
    table = int(input('Enter the table number: '))
    waiter = input('Enter the waiter\'s name who will assist: ')
    return {'tableNumber': table, 'items': [], 'waiter': waiter}

def addItem(accountList):
    table = int(input('Enter the table number: '))

    found = False
    position = 0
    while not found:

        if accountList[position]['tableNumber'] == table:
            item = input('Enter the ordered item: ')
            quantity = int(input('Enter the ordered quantity: '))
            unitPrice = float(input('Enter the unit price: '))

            accountList[position]['items'].append({'item': item, 'quantity': quantity, 'price': unitPrice})
            found = True

        position += 1

    return accountList

def closeAccount(accountList):
    table = int(input('Enter the table number: '))

    found = False
    position = 0
    totalBill = 0
    while not found:

        if accountList[position]['tableNumber'] == table:

            for x in accountList[position]['items']:
                totalItem = x['quantity'] * x['price']
                totalBill += totalItem
                print(f"{x['item']} - {x['quantity']} - {x['price']} = $ {totalItem}")

            found = True

        position += 1
    tipValue = tip(totalBill)
    print(f"Waiter's tip = $ {tipValue}")
    totalBill += tipValue

    print('-----------------------------')
    print(f'Account total: $ {totalBill}')
    print('-----------------------------')

    return totalBill

def tip(totalBill):
    return (totalBill * 10) / 100

def dailyClosing(closedAccounts):
    return sum(closedAccounts)

close = False
accountList = []
closedAccounts = []

while not close:

    menu = int(input(
        'Enter 1 to Open Account \n Enter 2 to Add Item to Account \n Enter 3 to Close Account \n Enter 4 to Calculate 10% Tip \n Enter 5 to Calculate Daily Revenue: \n  '))

    if menu == 1:
        account = openAccount()
        accountList.append(account)
    elif menu == 2:
        accountList = addItem(accountList)
    elif menu == 3:
        accountValue = closeAccount(accountList)
        closedAccounts.append(accountValue)
    elif menu == 4:
        value = float(input('Enter the value: '))
        tipValue = tip(value)
        print(tipValue)
    elif menu == 5:
        revenue = dailyClosing(closedAccounts)
        print(f"Today the restaurant has made $ {revenue}")
    else:
        print('Enter a valid option')

    option = input('Do you want to end the shift? Enter Y for yes or N for no')
    if option == 'Y':
        close = True