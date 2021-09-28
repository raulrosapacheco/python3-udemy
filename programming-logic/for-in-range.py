#  range(start=0, stop, step=1)

text = 'Data Science Academy'
for letter in text:
    print(letter)

print('###########')

for num in range(10):
    print(num)

print('###########')

for num in range(1, 10, 2):
    print(num)

print('###########')

list1 = ['Luiz Otavio', 'aJoao', 'Maria']

for element in list1:
    if element.lower().startswith('j'):
        print('there is a word that starts with J')
        break
else:
    print('there isn\'t  a word that starts with J')


