### print

'''
print('Hello python')
print('Integrated Development Environment')
print('IDE')
'''

### input

'''
print('How old are you?')
input()
print('Me too!')
'''

### 变量

'''
name = 'wang'+'xixi'
num = 1+5
price = 9.99*2
isUp = True
value = input()

print(name)
print(num)
print(price)
print(isUp)
print(value)
'''

### bool

'''
a = 1 < 3
b = False
print(a)
print(1 == 2)
print(1 != 0)
print(4 <= 2)
print( a and b)
print( a or b)
print(not a)
'''

# if

#if-example1
'''
number = bool(input())
if (not number):
    print(number)
else:
    print('false!')
'''

# if-example2(其中int()内容只能是数字(0-9)和正负号(+/-)，否则会报错)
'''
num = 10
print('Guess what I think?')
a = input()
print(a)
print(int(a))
'''

# if-example3

'''
num = 10
answer = int(input())
if answer < num:
    print('too small')
if answer > num:
    print('too big!')
if answer == num:
    print('BINGO!')
'''

# while

# while-example1

'''
a = 4
while a != 1:
    print('please input')
    a = int(input())
print('over')
'''

# while-example2

'''
num = 10
answer = int(input())
while answer != num:
    if(answer < num):
        print('too small!Please input!')
        answer = int(input())
    if(answer > num):
        print('too big!Please input!')
        answer = int(input())
print('BINGO!')
'''

