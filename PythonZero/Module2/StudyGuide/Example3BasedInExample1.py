# Usual method with dictionaries only
print("Usual method with dictionaries only:" + "\n")

student_data2 = {'Name': 'Raquel', 'grade': 95.7, 'absences': 0, 'suspension': 'N'}

print(student_data2, "\n")

# Method using a dictionary and a list for creating a sequence:
# Note that here the list contains a series of dictionaries,
# and each dictionary contains its elements, this will affect when iterating through the elements

print("Example of Collection structure:" + "\n")

students_list_dictionary = [
    {
        'Name': 'Bruno',
        'grade': 80.78,
        'absences': 3,
        'suspension': 'N'
    },  # Element 1 above

    {
        'Name': 'Raquel',
        'grade': 95.7,
        'absences': 0,
        'suspension': 'N'
    },  # Element 2 above

    {
        'Name': 'Pedro',
        'grade': 50.97,
        'absences': 1,
        'suspension': 'S'
    },  # Element 3 above

    {
        'Name': 'Maria',
        'grade': 80.3,
        'absences': 12,
        'suspension': 'S'
    }  # Element 4 above
]

for x in range(len(students_list_dictionary)):
    print(students_list_dictionary[x], "\n")

# Declaring a collection in another way, and in my opinion, the best way.
# Note that in this example, the dictionary contains keys,
# and the keys contain lists of elements, so the way of iterating will be different.

print("Another Example of Collection structure:" + "\n")

students_dictionary_list2 = {
    'Names': ['Bruno', 'Raquel', 'Pedro', 'Maria'],
    'grades': [80.78, 95.7, 50.97, 80.3],
    'absences': [3, 0, 1, 12],
    'suspensions': ['N', 'N', 'S', 'S']
}

# The correct way to iterate for this type of collection

for key in students_dictionary_list2:  # 'key' represents the keys like 'Names', 'grades', etc.
    elements = students_dictionary_list2[key]
    # The variable 'elements' will receive the list associated with this key when the for loop iterates
    print(elements)
    print(" ")

# The following way will result in an error:
# for key in range(len(students_dictionary_list2)):
#     print(students_dictionary_list2[key], "\n")