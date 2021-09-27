"""
if, elif, else
and, or, not
"""
grade1 = 7
grade2 = 5
grade3 = 10

media = (grade1 + grade2 + grade3) / 3

if media < 5:
    print('disapproved')
elif 5 <= media <= 7:  # media >= 5 and media <= 7
    print('approved')
else:
    print('approved with excellence')

if not media == 10:
    print('can improve')
else:
    print('highest grade')

"""
in, not in
"""

name = 'raul rosa'
if 'u' in name:
    print('have ""u"')
else:
    print("not have")

if 'u' not in name:
    print('have ""u"')
else:
    print("not have")
