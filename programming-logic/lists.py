"""
slicing
append, insert, pop, del, clear, extend, +
min, max
range
"""
#         0    1    2   3    4
list1 = ['A', 'B', 10, 20, 50.5]
#   -   ( 5    4    3   2    1 )
list1[2] = 'C'  # modifying string index 2
list1[3] = 'D'
list1[4] = 'E'
print(list1)
print(list1[1:4:1])
print(list1[::-1])

list2 = [1, 2, 3, 4, 5]
list3 = list1 + list2  # string concatenation
print(list3)
list1.extend(list2)  # list1 = list1 + list2
print(list1)

list1.append(6)

list1.insert(5, 'F')

print(list1)

list1.pop()  # remove ultimo elemento

print(list1)
del(list1[:6])
print(list1)
print(max(list1))
print(min(list1))
list1.clear()
print(list1)
