name = 'Raul Rosa'
age = 27
height = 1.80
is_larger = age >= 18
weight = 75
imc = weight / (height ** 2)

print(name, 'have', age, 'years old and his imc is', imc)
print(f'{name} have {age} years old and his imc is {imc:.2f}')
print('{} have {} years old and his imc is {:.2f}'.format(name, age, imc))
print('{0} have {1} years old and his imc is {2:.2f}'.format(name, age, imc))
print('{0} have {0} years old and his imc is {2:.2f}'.format(name, age, imc))
print('{m} have {n} years old and his imc is {p:.2f}'.format(m=name, n=age, p=imc))

print()

print(f'{age:0>10}')
print(f'{age:0<10}')
print(f'{age:0^10}')
print(f'{age:.2f}')
print(f'{age:0>10.2f}')
print(f'{age:0<10.2f}')

num_1 = 10
num_2 = f'{num_1:0>10}'
print(num_2, type(num_2))  # type: str

print()

print(f'{name:#^50}')
name_format = '{n:#>50}'.format(n=name)
print(name_format)

print(name.lower())
print(name.upper())
print(name.title())
