def registerClient(name, email, cpf):
    client = {}
    client['name'] = name
    client['email'] = email
    client['cpf'] = cpf

    return client

def checkExistingRegistration(cpf):
    registeredCpfList = [123, 456, 678, 990, 110]
    if cpf in registeredCpfList:
        print("Oops! You already have a registration!")

def checkValidEmail(email):
    if "@" not in email:
        print("This email is not valid")

name = str(input("Enter your name: "))
email = str(input("Enter your email: "))
cpf = int(input("Enter your CPF number: "))

clientInfo = registerClient(name, email, cpf)
checkExistingRegistration(cpf)
checkValidEmail(email)