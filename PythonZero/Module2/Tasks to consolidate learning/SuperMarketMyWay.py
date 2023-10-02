# Declaring variables
product_dict = {}  # Empty dictionary

# Storing supermarket products in the product_dict
while True:
    product_name = input("Enter the product name:\n")
    product_price = float(input("Enter the product price:\n"))

    product_dict[product_name] = product_price
    # In line 10, I'm considering product_name as a key and product_price as its value
    option = input("Do you want to add more products to the supermarket? Enter 'Y' or 'N':\n")
    if option == "N":
        print("Supermarket products:\n", product_dict)
        break

# Storing customers
checkout = {}
total_revenue = 0
while True:
    customer_name = input("Enter the customer name:\n")
    cart = []
    customer_revenue = 0

    while True:
        product_name = input("Enter the product name:\n")
        if product_name in product_dict:
            cart.append(product_dict[product_name])
            customer_revenue = customer_revenue + product_dict[product_name]
            print("Product added successfully. Current checkout total: %f" % customer_revenue)
        else:
            print("Product not found. Please enter again.")

        option = input("Do you want to add more products? Enter 'Y' or 'N':\n")
        if option == "N":
            print("Total revenue for %s: %f" % (customer_name, customer_revenue))
            break

    checkout[customer_name] = cart  # Note that here the customer_name key is receiving a list
    total_revenue = total_revenue + customer_revenue
    option = input("Do you want to add more customers to the checkout? Enter 'Y' or 'N':\n")
    if option == "N":
        break

print("Total revenue for the day:", total_revenue)
print("Checkout details:\n", checkout)
