# 读文件 open
'''
f = open('./data.txt','r', encoding='UTF-8')    #打开文件
data = f.read()                                 #读取文件
print(data)                                     #打印文件内容
f.close()                                       #关闭文件
'''

# 写文件——example1

'''
str1 = 'a string you want to write111'
str2 = 'a string you want to write222'

f1 = open('./data1.txt','w', encoding='UTF-8')          #写入模式,原来的文件内容会被覆盖
f2 = open('./data2.txt','a', encoding='UTF-8')          #写入模式，原来的文件内容不会被覆盖

data1 = f1.write(str1)
data2 = f2.write(str2)

print(data1)
print(data2)

f1.close()
f2.close()
'''

# 写文件——example2

'''
f2 = open('./data2.txt','r',encoding='UTF-8')
data2 = f2.read()
f1 = open('./data1.txt','a',encoding='UTF-8')
f1.write(data2)
print(f1)
f1.close()
f2.close()
'''

# 写文件——example3
'''
print('Please input something:')
str = input()
f1 = open('./data1.txt','a',encoding='UTF-8')
str1 = f1.write(str)
f1.close()
f2 = open('./data1.txt','r',encoding='UTF-8')
data = f2.read()
print(data)
f2.close()
'''

# 处理文件中的数据
'''
f = open('./score.txt','r',encoding='UTF-8')

lines = f.readlines()

#print lines

f.close()

results = []

for line in lines:
   #print line
   data = line.split()
   #print data

   sum = 0
   for score in data[1:]:
       sum += int(score)

   result = '%s \t: %d\n' % (data[0], sum)

   #print result
   results.append(result)


#print results

output = open('./result.txt', 'w',encoding='UTF-8')

output.writelines(results)

output.close()
'''

# break 语句  —— 彻底跳出循环
'''
i = 0
while i < 3:
    if i == 1:
        print('老师来啦')
        print('关闭歌曲')
        break
    print('正在播放：双节棍')
    i += 1  
'''

# continue 语句 —— 略过本次循环的余下内容，直接进入下一次循环

'''
songs = ['安静', '蜗牛', '稻香']

for i in range(len(songs)):
    if i == 1:
        print('不想听', songs[i])
        print('快进，下一曲')
        continue
    print("正在播放：", songs[i])
'''

# try...except处理异常
'''
try:
   print(int('0.5'))
except:
   print('ERROR!')

'''

# 字典key-value

'''
score = {
   '萧峰': 95,
   '段誉': 97,
   '虚竹': 89
}

print(score['段誉'])

for name in score:
   print(score[name])

score['虚竹'] = 99      #修改键值
score['慕容复'] = 88    #给新键赋值
del score['萧峰']       #删除字典
d = {}                 #新建空字典

print(score)
'''

# 使用模块 import module
''''
import random

a = random.randint(1,5)          # 使用格式random.
print(a)
print(dir(random))               # 打印random有哪些变量

# 仅用到模块中某一函数或变量   from module import function
from random import randint

print(randint(1,5))

from math import pi as math_pi      #为避免冲突，给引入的函数重新命名

print(math_pi)
'''

