dictionary = {}

print(dictionary)

print(type(dictionary))

print(len(dictionary))

print(type(len(dictionary)))  # curiosity

dictionary = dict()

print(dictionary)

firstDict = {'Joao': 10, 'Maria': 7.5, 'Pedro': 6}

print(firstDict)

firstDict['Joao'] = 9
print(firstDict)
firstDict['Mariana'] = 8.7
print(firstDict)
firstDict.update({"Joaquim": 7.7})  # also adds
print(firstDict)

print(len(firstDict))

dictEnPT = {
    'data science': 'Data Science',
    'Machine Learning': 'Machine Learning',
    "Deep Learning": 'Deep Learning'
}

print(dictEnPT)

print(firstDict['Joao'])

print(firstDict.get('Joao'))

# print(firstDict[0])  # error

firstDict["Pedro"] = 6.5
print(firstDict)

dictTwoGrades = {
    "Joao": [9, 9.5],
    "Maria": [7.5, 8],
    "Pedro": [6.5, 6],
    "Mariana": [8.7, 9]
}

print(dictTwoGrades)

formDict = {"name": "Joao",
            "age": 18,
            "grade1": 9,
            "grade2": 9.5,
            "passed": True}

print(formDict)

d = {"name": "Joao",
     1: 9,
     2: 9.5}

print(d)

print(type(d))

print(d["name"], d[1])
# it prints the value of the "name" key, and the key of position 1, which corresponds to Joao's grade 1, which is value 9

print(firstDict.get("Pedro"))

print(firstDict.keys())  # prints all keys

print(firstDict.values())  # prints the values of all keys

print(firstDict.items())  # prints the keys and their values

firstDict.pop("Maria")
print(firstDict.keys())

print("Original firstDict:", firstDict)

secondDict = {"Maria": 7, "Sabrina": 5, "Joao": 9.2}

firstDict.update(secondDict)  # alters the structure of firstDict
# concatenates dictionaries
print("Updated firstDict:", firstDict)

firstDict.clear()

print(firstDict)

# And how could we take two separate lists and convert them into a dictionary
# without having to do it manually?
# The following data is ordered, the first name in one list corresponds to the first grade in another list

nameList = ["Maria", "Joao", "Pedro", "Mariana"]
gradeList = [7.5, 9, 6.5, 8.7]

# LET'S USE ZIP
# we create a list with tuples, which will be our key-value pairs in the dictionary
nameGradeList = list(zip(nameList, gradeList))
print(nameGradeList)

nameGradeDict = dict(nameGradeList)

print(nameGradeDict)