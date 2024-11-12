
emp_list = []
values = [1, 2, 'rahul', 4, 5]

# print(values[0])
# print(values[1])
# print(values[2])
# print(values[3])
# print(values[4])
# print(values[-1]) # last element
# print(values[1:3])
values.insert(3, 'name') # adds an element at required index
print(values)
values.append(6) # adds an element at the last position of the list
print(values)
values[2] = "RAHUL"
print(values)
values.remove(6) # Deletes the mentioned value
print(values)
del values[0] # Deletes the value at the mentioned index
print(values)

values.clear() # Empties the list
print(values)