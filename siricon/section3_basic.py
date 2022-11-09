s = 'My name is Mike. Hi Mike'
print(s)
is_start = s.startswith('s')
print(is_start)
print('###############')
print(s.find('Mike'))
print(s.rfind('Mike'))
print(s.count('Mike'))
print(s.capitalize())
print(s.title())
print(s.upper())
print(s.lower())
print(s.replace('Mike', 'Nancy'))
print('a is {} '.format('test'))
print('a is {2} {1} {0} '.format(1, 2, 3))
print('My name is {name} {family}. Watasi ha {family} {name}'.format(name='Jun', family='Sakai'))

a = 'asad'
print(f'a is {a}')

name = 'Jun'
family= 'Sakai'
print(f'My name is {name} {family}. Watashi ha {family} {name}')