print("\nPython Dictionaries")

myDict = {'name': 'Eva', 'age': 17, 'city': 'Norwood'}

print('My name is: ', myDict['name'])

print('\nAdding/Updating Items in a Dictionary\n')

myDict['country'] = 'USA' # adding a key/value pair.  not using append b/c adding new key/value

print(myDict)

myDict['age'] = 18

print(myDict)

print("\nRemove Items from a dictionary")

del myDict['country']

print(myDict)

print("\n Delete the an item from the Dictionary, and return it's value")

rem_value = myDict.pop('age')

print(rem_value)
print(myDict)

print("\nA New Dictionary\n")

dictionary2 = {'fruits': ['apple', 'banana', 'orange'], 'vegetables': ['broccoli', 'brussel sprouts', 'carrots']}

#add another fruit:
dictionary2['fruits'].append('cherry') #using append b/c adding to pre-existing key

#print the dictionary
print(dictionary2)

print(dictionary2['fruits'])


