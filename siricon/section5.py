# a = 10
# c = 30
# b = 20

# if a > 0:
#     print('True')
# elif a == 0:
#     print('zero')
# else:
#     print('False')


# y = [1, 2, 3]
# x = 1

# if x in y:
#     print('in')
# if 100 not in y:
#     print('not in')

# is_ok = True

# if not is_ok:
#     print('hello')

# count = 0
# while True:
#     if count > 5:
#         break
#     if count == 2:
#         count += 1
#         continue

#     print(count)
#     count += 1

# count = 0
# while count < 5:
#     print(count)
#     count += 1

# else:
#     print(count)


# while True:
#     word = input('Enter: ')
#     if word == 'ok':
#         break
#     print('next')

# some_list = [1, 2, 3, 4, 5]
# i = 0

# while i < len(some_list):
#     print(some_list[i])
#     i += 1

# some_list = [1, 2, 3, 4, 5]

# for i in some_list:
#     print(i)
# for s in 'asdfgdja':
#     print(s)

# for i in range(2, 10, 3):
#     print(i)
# ピラミッドをfor文で作成
n = 0
ranges = int(input('Enter: '))
for i in range(ranges):
    n = ranges - i
    for j  in range(n):
        print(' ', end=' ')
    m = i * 2 + 1
    for k in range(m):
       print('*', end=' ')
    print('\n')
  
