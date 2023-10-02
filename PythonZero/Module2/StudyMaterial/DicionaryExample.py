print('Example 1:')
print("--------------")

dictionary = dict()  # empty dictionary
print(dictionary)

print('Example :', "\n")

dictionary = {
    'brand': "Fiat",
    "model": "Toro",
    "electric": False,
    "year": 2020,
    "year": 2019,
}

print(dictionary)
print(dictionary["brand"])

print('Example 2:')
print("--------------")

data = {"name": "Ricardo", "visits": 25}

print(data["name"])

data["visits"] += 1
print(data["visits"])

print("name" in data)

print('Example :', "\n")
print(data.keys())

print('Example :', "\n")
print(data.values())

print('Example :', "\n")
print(data.items())
print('Example :', "\n")