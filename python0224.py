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




