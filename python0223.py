# random

'''
from random import  randint     #from 模块名 import 方法名

num = randint(1,100)
print(num)
'''

#变量2

'''
a = 1
sum = 0
while a!= 100:
    sum = sum + a
    a = a+1
    print('a=%d'%a)         # 打印字符串+变量格式
    print('sum=%d'%sum)
print('over')

'''

# for循环
'''
for i in range(1,101):      #for i in range(a,b),即从a循环到b-1
    print(i)
'''

# 字符串

'''
str = 'string'
print(str)
print('I\'m a \"good\" teacher')        # \被称作转译字符，除了用来表示引号
'''

# 字符串格式化
'''
num = 18
price = 19.9
name = 'Lisa'
print('num is '+str(num))
print('The num is %d'%num)              #整数%d
print('The price is %f'%price)          #小数%f
print('The price is %.2f'%price)        #保留两位小数
print('my name is %s'%name)             #字符串用%s
'''

# 循环嵌套-example1
'''
for i in range(0,5):
    for j in range(0,5):
        print(i,j)
'''

# 循环嵌套-example2
'''
for i in range(1,5):
    print('*',end='')       #python3-保持在同一行，使用end=
'''

# 循环嵌套-example3

'''
for i in range(0,5):
    for j in range(0,5):
        print('*',end='')
    print()                 #print()起换行作用
'''

# 循环嵌套-example4

'''
for i in range(0,5):
    for i in range(0,i+1):
        print('*',end='')
    print()
'''

# 字符串格式化2
'''
print("%s's score is %d" %('Mike',87))
'''

# 类型转换-example1
'''
a = 1
print(a)
a = 'hello'
print(a)
a = True
print(a)
'''

# 类型转换-example2

'''
a = 1
print(int(a))
print(float(a))
print(str(a))
print(bool(a))
#print('Hello'+1)    #类型不一致会报错
#print('hello %d' %'123')  #类型不一致会报错
'''

# 类型转换-example3

'''
print(bool(-123))
print(bool(0))
print(bool('abc'))
print(bool('False'))
print(bool(''))
a = '123'
if bool(a):
    print(a)
'''

# 函数
'''
def sayhello():
    print('Hello python!')

sayhello()
'''

# 函数参数-example1
'''
def sayhello(saySomeOne):
    print( saySomeOne + 'say hello!')

sayhello('Lisa ')

def plus(num1,num2):
    print(num1+num2)
plus(1,2)
'''

# 函数参数-example2
'''
def isEqual(num1,num2):
    if num1 < num2:
        print('too Small!')
        return False        #任何地方执行return，该函数就会结束
    if num1 > num2:
        print('too Big!')
        return False
    if num1 == num2:
        print('Bingo!')
        return True

from random import randint
num = randint(1,100)
print('Guess what I think?')
bingo = False
while bingo == False:
    answer = int(input())
    bingo = isEqual(answer,num)

'''

# if elif else
'''
a = 21
if a == 1:
    print('one')
elif a == 2:
    print('two')
else:
    print('too many')
'''

# if嵌套

''''
def coordinate(x,y):
    if x >= 0:
        if y > 0:
            print('1')
        else:
            print('4')
    else:
        if y >= 0:
            print('2')
        else:
            print('3')
coordinate(-2,-14)
'''

# list数组

'''
print(list(range(1,5)))
L = [1,2,3,4]
print(L)

for i in L:
    print(i)

P = [True,'hdik',121,3.24]
print(P)

'''

# list切片
'''
P = [True,'hdik',121,3.24]
print(P[1:3])               #数组取值格式 Array[num1:num2]
print(P[:0])                #从数组第一个元素开始
print(P[3:])                #从数组第4个开始到最后一个
print(P[:])                 #拷贝整个数组
print(P[:-3])               #倒数第4个数据开始
print(P[1:-2])              #从第2个到倒数第3个
'''

# 字符串分割split()——example1

'''
str1 = 'Hello,my name is Lisa'
str2 = str1.split()
print(str2)

section1 = 'Hi. I am the one. Bye.'
section2 = section1.split('.')
print(section2)

print('aaa'.split('a'))        #分成四个空格
'''

# 字符串分割split()——example2

'''
from random import  choice
score = [0,0]
direction = ['left','center','right']

def kick():
    print('==== You Kick! ====')
    print('Choose one side to shoot:')
    print('left,center,right')

    you = input()
    print('You kicked ' + you)

    com = choice(direction)         #返回一个列表，元组或字符串的随机项
    print('Computer saved '+ com)

    if you != com:
        print('Goal!')
        score[0] += 1
    else:
        print('Oops...')

    print('Score: %d(you) - %d(com)\n' %(score[0],score[1]))

for i in range(5):
    print('==== Round %d ==== '%(i+1))
    kick()

while(score[0] == score[1]):
    i += 1
    print('==== Round %d ====' %(i+1))
    kick()
    
if score[0] > score[1]:
    print( 'You Win!')
else:
    print('You Lose.')
'''

# 字符串连接
'''
s = ';'
li = ['apple','pear','orange']
fruit = s.join(li)

print(fruit)
print(';'.join(li))
print(''.join(li))
'''

#字符串的索引和切片

## 1.遍历

'''
word = 'helloword'
for c in word:
    print(c)
'''

## 2.索引访问

'''
word = 'helloword'
print(word[3])
print(word[-2])     #字符串倒数第二个字符
'''

# 错误用法 wrod[1] = 'a'    #不能直接赋值

## 3.切片

'''
word = 'helloword'
print(word[1:2])
print(word[:-5])
print(word[3:])
'''

## 4.连接

'''
word = 'helloword'
newword = ','.join(word)
print(newword)
'''
