"""
while condition:
continue
break
while condition:
    while condition:
while / else

"""
x = 0
while x < 10:
    if x == 3:
        x += 1
        continue  # jump to the next loop
    print(x)
    x += 1
print('finish\n')

x = 0
while x < 10:
    if x == 3:
        x += 1
        break  # break the while loop
    print(x)
    x += 1
print('finish\n')

x = 0  # row
while x < 10:
    y = 0  # column

    while y < 5:
        print(f'({x},{y})')
        y += 1

    x += 1

print('finish')

counter = 1
accumulator = 1
while counter <= 10:
    print(counter, accumulator)
    accumulator += counter
    counter += 1
else:
    print('while condition false')
