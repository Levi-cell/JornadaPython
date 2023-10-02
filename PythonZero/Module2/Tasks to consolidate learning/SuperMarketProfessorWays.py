products = {
    'name': [],
    'value': []
}

while True:
    name = input('Enter the product name: ')
    value = float(input('Enter the product value: '))

    products['name'].append(name)
    products['value'].append(value)

    option = input('Do you want to add another product? Type "Y" for yes or "N" for no: ')
    if option == 'N':
        break

purchaseHistory = {}
checkoutRevenue = 0

while True:
    name = input('Enter the customer name: ')
    purchaseHistory[name] = []
    purchaseValue = 0

    while True:
        product = input('Enter the product name: ')
        purchaseHistory[name].append(product)

        entered = False
        k = 0
        while entered == False:
            if product == products['name'][k]:
                purchaseValue += products['value'][k]
                entered = True

            k += 1

        option = input('Did the customer complete the purchase? Type "Y" for yes or "N" for no: ')
        if option == 'Y':
            print(f'Your purchase amount is ${purchaseValue}')
            checkoutRevenue += purchaseValue
            break

    closeCheckout = input('Do you want to close the checkout? Type "Y" for yes or "N" for no: ')
    if closeCheckout == 'Y':
        print(f'Your checkout revenue is ${checkoutRevenue}')
        break