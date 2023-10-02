age = int(input("What is your age? "))

if age >= 18:
    print("Entered age:", age)
    print("You can now get your driver's license!")
    print("Congratulations :)")

age = int(input("What is your age? "))
vision = str(input("Do you have good vision? "))

if age >= 18 and vision == "yes":
    print("You can now get your driver's license!")
    print("Congratulations!")

availableProducts = ['rice', 'beans', 'flour', 'banana', 'milk']
product = input('Which product are you looking for? ')

if product in availableProducts:
    print("Great! We have this product in stock :)")
    print("Hurry up while supplies last!")
    print("We appreciate your preference.")

balance = 1000
withdrawalAmount = 75

if balance >= withdrawalAmount:
    print("The amount of", withdrawalAmount, "was successfully withdrawn.")
    balance = balance - withdrawalAmount  # operation within the if statement
    print("Your new balance is", balance)
