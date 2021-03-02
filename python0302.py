# game1

f = open('./game1.txt','r',encoding='UTF-8')
score = f.read().split()
f.close()

game_times = int(score[0])
min_times = int(score[1])
total_times = int(score[2])

if game_times > 0:
    avg_time = float(total_times)/game_times
else:
    avg_time = 0;

# 函数默认参数

def sayHello(name = 'python'):
    print('hello',name)
sayHello()