"""
str - string
str[index]
str[start(in):end(out):step]
        012345
text = 'python'
      -(654321)
"""
username = 'python'

print(username[0])

new_string = username[2:6]  # thon
print(new_string)
new_string = username[:6]  # python
print(new_string)
new_string = username[2:]  # thon
print(new_string)
new_string = username[-4:]  # thon
print(new_string)

print()

new_string = username[0:6:2]
print(new_string)

lenUsername = len(username)
print(username, lenUsername, type(lenUsername))
print(username.__len__())  # special method
