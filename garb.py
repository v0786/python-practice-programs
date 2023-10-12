# Assigning a
a= 50
print('a')
print(type(a))
print(id(a))
print('b')
# Assigning b
b= 2.5
print(type(b))
print(id(b))
# Assigning a to c
c=a
print('c')
print(type(c))
print(id(c))

#Defining a list
list_1 = ['a1','b1','c1','d1']
print('list_1')
print(type(list_1))
print(id(list_1))

# Appending E
list_1.append("e1")
print('Updated list is ', list_1)
print(type(list_1))
print(id(list_1))

# Creating an empty list
print('Empty List')
list_2 =[]
print(id(list_2))
list_2.append(list_2)
print(id(list_2))
