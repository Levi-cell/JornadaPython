# Question 9

s = 'Mentorama'
print(s.upper()) # Convert to uppercase
print(s.upper()[::-1]) # Reverse the string

def vowels(x):  # Define a function to print only vowels from a string
    # The (str) indicates that x is a string variable
    for c in x:  # This loop will iterate through all characters in the string
        if c == "a" or c == "e" or c == "i" or c == "o" or c == "u":
                # Condition to check if each character is a vowel
            print(c)
vowels('Mentorama')

# Other ways

def moreVowels(x): # Define a function to print only vowels from a string
    # The (str) indicates that x is a string variable
    for c in x: # This loop will iterate through all characters in the string
        if c in "aeiou":
                # Condition to check if each character is a vowel
            print(c)
moreVowels('Mentorama')

x = str('Mentorama')
for c in x:
    if c in "aeiou":
        print(c)

# Question 10
# Note: If the question mentions user input, then I won't define values. The input values will be the ones provided by the user.

print("Question 10")

firstName = str(input("Tell me your first name:"))
lastName = str(input("Tell me your last name:"))
age = int(input("Tell me your age:"))
city = str(input("Tell me your city:"))
areaCode = str(input("Tell me your area code:"))
phoneNumber = str(input("Tell me your phone number:"))
print("-------------"+"\n")

print("Full name:" + firstName + " " + lastName +"\n")
print("-------------"+"\n")
print("Phone:(%s)%s"  % (areaCode, phoneNumber) +"\n")
print("-------------" +"\n")
print("Age:", age)
print("-------------" +"\n")
print("City:", city)
print("-------------" +"\n")