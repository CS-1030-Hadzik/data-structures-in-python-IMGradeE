'''
Name: Payton Wilkes
Date: 11/14/22
Description: Data structures in python assignment
PS: I want to extend my gratitude to whoever decided that this assignment would be done in python. While I remain
ambivalent towards the multitudes of java, I avoid it like the plague. Also, I hope you don't mind my use of
docstrings as multi-line comments.
'''

print("Payton Wilkes\n")
# I typically use double quotes for strings since apostrophes are more common than double quotes, and it saves me from
# Having to use escape characters as often.
cars = ['Ford','Chrysler','Dodge','Ram','Jeep','Chevy','GMC']
print(cars,'\n')
print(len(cars),'\n')

cars.append('Buick')
print(cars,'\n')
print(cars[3])

cars.insert(2,'Toyota')
print(cars,'\n')

cars.pop(4)
print(cars,'\n')

cars.sort()
print(cars,'\n')

cars.sort(reverse=True)
print(cars,'\n')

my_array_length = str(len(cars))
# Why?

array_string = 'The length of my array is '
# I understand why to do this, by the way, just not the length thing.

print(array_string + my_array_length)

# I would do this
print(f"{array_string}{len(cars)}")
