"""
l = [1, 20, 4, 50, 2, 1, 2]

print(l)
print(l[0])
print(l[1])
print(l[-1])
print(l[0:2])
print(l[:2])
print(len(l))

n = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(n[::2])
a = ['a', 'b', 'c']
n = [1, 2, 3]
x = [a, n]

print(x)
print(x[0])
print(x[1])
print(x[0][1])

n = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
n.append(100)

print(n)

n.insert(0, 200)
print(n)

print(n.pop(0))
"""

r = [1, 2, 3, 4, 5, 1, 2, 3]
print(r.index(3,3))
print(r.count(3))

if 5 in r:
    print('exist')

r.sort()
print(r)
r.sort(reverse=True)
print(r)
r.reverse()
print(r)

s = 'My name is Mike.'
to_split = s.split(' ')
print(to_split)

x = ' '.join(to_split)
print(x)

min, max = 0, 100
print(min, max)
print(type(min))