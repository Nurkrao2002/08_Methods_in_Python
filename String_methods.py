"""Topic: String Methods """

'''Sub-Topic'''

print(dir(str))

['capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 
'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 
'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join',
 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix', 'replace', 
 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 
 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']

a=input()
print(a.upper())
print(a.lower())
print(a.swapcase())
print(a.isupper())
print(a.islower())
print(a.capitalize())
# print(a.iscapitalize()) # AttributeError
print(a.title())
print(a.istitle())

print('_ab'.isidentifier())

a='python'
print(len(a))
print(len('programming'))

print(''.isspace())
print('  p '.isspace())
print(' '.isspace())
print('           '.isspace())

print('34'.isalnum())
print('hi5'.isalnum())
print('hi_5'.isalnum())

print('b5'.isalpha())
print('cricket'.isalpha())

print('python'.count('p'))
print('python'.count('py'))
print('python'.count('ph'))
print('python'.count('P'))

print('hello'.startswith('h'))
print('hello'.startswith('yh'))
print('hello'.startswith('he'))
print('program'.endswith('p'))
print('program'.endswith('m'))
print('program'.endswith('am'))

print('hello'.find('r'))
print('hello'.find('h'))
print('hello'.find('o'))
print('programming'.find('m'))
print('programmingm'.find('m',8))
print('programming'.rfind('g'))

print('python'[0])
print('python'[1])
print('python'[2])
print('python'[3])
print('python'[4])
print('python'[5])
# print('python'[6])  # IndexError: string index out of range

print('python'[-1])
print('python'[-2])
print('python'[-3])
print('python'[-4])
print('python'[-5])
print('python'[-6])
# print('python'[-7])


print('september friday'.find('d'))
print('september friday'.index('d'))

print('september friday'.find('n'))
# print('september friday'.index('n'))

print('september friday'.rindex('e'))
print('september friday'.index('e'))
print('september friday'.index('e',2))


print('hi'.zfill(2))
print('hi'.zfill(3))
print('hi'.zfill(4))

a,b=[(x) for x in input().split()]
print(a+b)
print(int(a)+int(b))
print(float(a)+float(b))

# print('The Value of a is {a} and b is {b}'.format(a=3,b=5.6/))
# print('The Value of a is {a} and b is {c}'.format(a=3,b=5.6))

print(len(' python pro '.strip()))
print(len(' python pro'.lstrip()))
print(len(' python pro'.rstrip()))

print('python program'.replace('program','programming'))
print('python program'.replace('program',str(3)))
print('python program'.replace('progra','programming'))
print('python program'.replace('py','programming'))
print('python program'.replace('p','programming'))

'''Types of Strings  '''

a='hello'
print(type(a))

print(r'hey\no')

a=4; b=7.8
# print(f'The value of a is {a} and b is {b}')
# print(f'The value of a is {a} and b is {c}')

