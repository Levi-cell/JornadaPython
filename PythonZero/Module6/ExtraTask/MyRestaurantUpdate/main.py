from menu import *

def openBill():
    while True:
        try:
            tableNumber = int(input("Enter the table number: " + "\n"))
            break
        except ValueError:
            print("Invalid input. Please enter the table number again:" + "\n")

    waiter = input("Enter the waiter's name:" + "\n")
    while len(waiter) <= 2 or not waiter.isalpha():
        waiter = input("Invalid waiter name, please enter again:" + "\n")

    bill = {
        'Table Number': tableNumber,
        'Waiter Name': waiter,
        'Items': [],
    }

    return bill

def addItem(accountList):
    data = open('restaurantData.txt', 'a')
    while True:
        try:
            tableNumber = int(input("Enter the table number: " + "\n"))
            break
        except ValueError:
            print("Invalid input." + "\n")

    if not accountList:
        print("You haven't opened any accounts yet..." + "\n")
        return accountList

    foundTable = False
    position = 0
    while not foundTable and position < len(accountList):
        if accountList[position]['Table Number'] == tableNumber:

            item = input("Enter the name of the item you want to add:" + "\n")
            if item not in dailyMenu:
                while item not in dailyMenu:
                    print("This dish is not in the menu. Check the menu:" + "\n")
                    for dish in dailyMenu:
                        print(f"{dish} : $ {dailyMenu[dish]}")
                    print(" ")
                    item = input("Enter the item again (be careful with uppercase and lowercase letters):" + "\n")

            while True:
                try:
                    quantity = int(input("Enter the quantity you want to add:" + "\n"))
                    break
                except ValueError:
                    print("Invalid input." + "\n")

            unitPrice = dailyMenu[item]

            item = {
                'Item Name': item,
                'Quantity': quantity,
                'Unit Price': unitPrice
            }

            totalValue = quantity * unitPrice
            print("----------------------")
            print(f"Added {quantity} portions of {item['Item Name']} for {totalValue}"
                  f" to table {accountList[position]['Table Number']}" + "\n")
            print("----------------------")
            accountList[position]['Items'].append(item)
            foundTable = True
            data.writelines(f"{item}" + "\n")
        position += 1
    data.close()
    if not foundTable:
        print("Table not found")
    return accountList

def closeBill(accountList):
    while True:
        try:
            tableNumber = int(input("Enter the table number: " + "\n"))
            break
        except ValueError:
            print("Invalid input." + "\n")

    totalBillValue = 0
    if not accountList:
        print("You haven't opened any accounts yet..." + "\n")
        return totalBillValue

    foundTable = False
    position = 0
    while not foundTable and position < len(accountList):
        if accountList[position]['Table Number'] == tableNumber:
            print("Items:")
            for item in accountList[position]['Items']:
                totalOrder = item['Quantity'] * item['Unit Price']
                totalBillValue += totalOrder
                print(f"{item['Item Name']}: {item['Quantity']} x {item['Unit Price']} = $ {totalOrder}")
            accountList.remove(accountList[position])
            foundTable = True
        position += 1

    if not foundTable:
        print("No account open for this table..." + "\n")
        return totalBillValue

    ten_percent_tip = calculateTip(totalBillValue)
    totalBillValue += ten_percent_tip
    print(f"The waiter will receive $ {ten_percent_tip}")
    print("----------------------")
    print(f"The bill has been closed with a total of $ {totalBillValue}")
    print("----------------------")

    return totalBillValue

def calculateTip(totalValue):
    return totalValue * 0.1

def dailyEarnings(closedAccounts):
    return sum(closedAccounts)

def salesHistory():
    data = open('restaurantData.txt', 'r')
    lines = data.readlines()
    for line in lines:
        data1 = line.split(';')
        print(f"{data1}")
    data.close()

dailyMenu = menu()
accountList = []
closedAccounts = []

# MENU

while True:

    mainMenu = (input("""
       Choose an option:
       1 - Open an account.
       2 - Add an item to an account.
       3 - Close an account and Calculate waiter's value.
       4 - Check the Menu
       5 - Check earnings so far.
       6 - Check open accounts.
       7 - Update Menu
       8 - Sales history
       9 - End of shift (Recommended to close all accounts first).
       What do you want to do:""" + "\n"))
    print("-----------------")

    if mainMenu == "1":
        receivedBill = openBill()
        accountList.append(receivedBill)
        print("-----------------------")
        print(f"Account added, Check:")
        print(f"Table Number: {receivedBill['Table Number']}, Waiter: {receivedBill['Waiter Name']}" "\n")
        interactive = input("Enter anything to return to the menu:" + "\n")

    elif mainMenu == "2":
        accountList = addItem(accountList)
        interactive = input("Enter anything to return to the menu:" + "\n")

    elif mainMenu == "3":
        billValue = closeBill(accountList)
        closedAccounts.append(billValue)

        interactive = input("Enter anything to return to the menu:" + "\n")

    elif mainMenu == "4":
        print("Updated Menu:", "\n")
        for item in dailyMenu:
            print(f"{item} : $ {dailyMenu[item]}")
        interactive = input("Enter anything to return to the menu:" + "\n")

    elif mainMenu == "5":
        earnings = dailyEarnings(closedAccounts)
        print(f"The earnings so far are {earnings}")
        interactive = input("Enter anything to return to the menu:" + "\n")

    elif mainMenu == "6":
        for item in accountList:
            print(f"Table Number: {item['Table Number']}, Waiter Name: {item['Waiter Name']}, Items: {item['Items']}")
            print("------------------------------------------------ ")
        if len(accountList) == 0:
            print("No open accounts")
        interactive = input("Enter anything to return to the menu:" + "\n")

    elif mainMenu == "7":
        dailyMenu = menu()

    elif mainMenu == "8":
        salesHistory()

    elif mainMenu == "9":
        earnings = dailyEarnings(closedAccounts)
        print(f"The earnings have closed at: {earnings}")
        break
    else:
        print("Invalid option")
        interactive = input("Enter anything to return to the menu:" + "\n")