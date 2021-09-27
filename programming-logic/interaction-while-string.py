phrase = 'the mouse gnawed at the king of rome\'s clothes'
len_phrase = len(phrase)
counter = 0
new_string = ''

while counter < len_phrase:
    print(phrase[counter], counter)
    letter = phrase[counter]
    if letter == 'r':
        new_string += 'R'
    else:
        new_string += phrase[counter]
    counter += 1

print(new_string)
