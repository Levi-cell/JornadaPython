from Menu import *


def openAccount():

    while True:
        try:
            tableNumber = int(input("Enter the table number: " + "\n"))
            break
        except ValueError:
            print("Invalid input. Please enter the table number again:" + "\n")

    waiter = input("Enter the waiter's name:" + "\n")
    while len(waiter) <= 2 or not waiter.isalpha():
        waiter = input("Invalid waiter's name, please enter again" + "\n")

    account = {

        'Table Number': tableNumber,
        'Waiter Name': waiter,
        'Items': [],

    }

    return account


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
                    print("This item is not on the menu, check the menu:" + "\n")
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

            newItem = {
                'Item Name': item,
                'Quantity': quantity,
                'Unit Item Price': unitPrice

            }

            totalValue = quantity * unitPrice
            print("----------------------")
            print(f"Added {quantity} portions of {newItem['Item Name']} for {totalValue}"
                  f" to table {accountList[position]['Table Number']}" + "\n")
            print("----------------------")
            accountList[position]['Items'].append(newItem)
            foundTable = True
            data.writelines(f"{item}" + "\n")
        position += 1
    data.close()
    if not foundTable:
        print("Table not found")
    return accountList


def closeAccount(accountList):
    while True:
        try:
            tableNumber = int(input("Enter the table number: " + "\n"))
            break
        except ValueError:
            print("Invalid input." + "\n")
    totalAccountValue = 0
    if not accountList:
        print("You haven't opened any accounts yet...." + "\n")
        return totalAccountValue

    foundTable = False
    position = 0
    while not foundTable and position < len(accountList):
        if accountList[position]['Table Number'] == tableNumber:
            print("Items:")
            for item in accountList[position]['Items']:
                totalOrder = item['Quantity'] * item['Unit Item Price']
                totalAccountValue += totalOrder
                print(f"{item['Item Name']}: {item['Quantity']} x {item['Unit Item Price']} "
                      f"= $ {totalOrder}")
            accountList.remove(accountList[position])
            foundTable = True
        position += 1

    if not foundTable:
        print("There is no open account at this table...." + "\n")
        return totalAccountValue

    tip = calculateTip(totalAccountValue)
    totalAccountValue += tip
    print(f"The waiter will receive $ {tip} as tip")
    print("----------------------")
    print(f"The account was closed with a value of $ {totalAccountValue}")
    print("----------------------")

    return totalAccountValue


def calculateTip(totalValue):
    return totalValue * 0.1


def dailyRevenue(closedAccounts):
    return sum(closedAccounts)


def salesHistory():
    data = open('restaurantData.txt', 'r')

    lines = data.readlines()
    for line in lines:
        data1 = line.split(';')
        print(f"{data1}")
    data.close()


dailyMenu = menu()
accountList = []  # Stores accounts
closedAccounts = []  # Stores closed account values

# MENU

while True:

    menuOption = (input("""
       Check the options:
       1 - Open an account.
       2 - Add an item to an account.
       3 - Close an account and Calculate waiter's value.
       4 - Consult the Menu
       5 - Consult revenue so far.
       6 - Consult open accounts.
       7 - Update Menu
       8 - Sales History
       9 - Close business hours (It's recommended to close all accounts first).
       What would you like to do:""" + "\n"))
    print("-----------------")

    if menuOption == "1":
        receivedAccount = openAccount()
        accountList.append(receivedAccount)
        print("-----------------------")
        print(f"Account added, Check:")
        print(f"Table Number: {receivedAccount['Table Number']}, Waiter: {receivedAccount['Waiter Name']}" "\n")
        interactive = input("Type anything to return to the menu:" + "\n")

    elif menuOption == "2":
        accountList = addItem(accountList)
        interactive = input("Type anything to return to the menu:" + "\n")

    elif menuOption == "3":
        accountValue = closeAccount(accountList)
        closedAccounts.append(accountValue)

        interactive = input("Type anything to return to the menu:" + "\n")

    elif menuOption == "4":
        print("Updated Menu:", "\n")
        for x in dailyMenu:
            print(f"{x} : $ {dailyMenu[x]}")
        interactive = input("Type anything to return to the menu:" + "\n")

    elif menuOption == "5":
        revenue = dailyRevenue(closedAccounts)
        print(f"The revenue so far is {revenue}")
        interactive = input("Type anything to return to the menu:" + "\n")

    elif menuOption == "6":
        for x in accountList:
            print(f"Table Number: {x['Table Number']}, Waiter Name: {x['Waiter Name']}, Items {x['Items']}")
            print("------------------------------------------------ ")
        if len(accountList) == 0:
            print("No open accounts")
        interactive = input("Type anything to return to the menu:" + "\n")

    elif menuOption == "7":
        dailyMenu = menu()

    elif menuOption == "8":
        salesHistory()

    elif menuOption == "9":
        revenue = dailyRevenue(closedAccounts)
        print(f"The revenue was closed at: {revenue}")
        break
    else:
        print("Invalid option")
        interactive = input("Type anything to return to the menu:" + "\n")