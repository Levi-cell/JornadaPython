# Using a list of dictionaries

orderedDictionary3 = [

    {
        'color1': 'Red',
    },

    {
        'color2': 'Green',
    },

    {
        'color3': 'Blue'
    }
]

orderedDictionary3.insert(0, {'color4': 'Orange'})

print(orderedDictionary3, "\n")

# ANOTHER WAY USING LISTS

listOfDicts = []

orderedDictionary4 = [

    {
        'color1': 'Red',
    },

    {
        'color2': 'Green',
    },

    {
        'color3': 'Blue'
    }
]
dictAuxiliary = {'color4': 'Orange'}
listOfDicts.append(orderedDictionary4)
print(listOfDicts)
listOfDicts.insert(0,{'color4': 'Orange'})  # One way to add
listOfDicts.insert(0,dictAuxiliary)  # Another way to add
print(listOfDicts)