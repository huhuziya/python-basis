# 查天气
# 北京天气：http://www.weather.com.cn/data/cityinfo/101010100.html
# 获取所有省/直辖市的编号：http://m.weather.com.cn/data3/city.xml
# 获取二级地区编号：http://m.weather.com.cn/data3/city省编号.xml
# 获取三级编号：http://m.weather.com.cn/data3/city二级编号.xml

# TODO:我们的程序要做的事情，就是按照用户输入的城市名称，去天气网的接口请求对应的天气信息，再把结果展示给用户

#创建类
class MyClass:
    name = 'Sam'
    def sayHi(self):	#类方法中必须有self参数
        print('Hello %s '%self.name)
mc = MyClass()	#类实例即MyClass的对象
print(mc.name)
mc.name = 'Lily'
mc.sayHi()

# 类的变量和方法——example1
class Car:
	speed = 0
	def drive(self,distance):
		time = distance/self.speed
		print(time)
car = Car()
car.speed = 60.0
car.drive(200.0)

# 类的变量和方法——example2
class Car:
	speed = 0
	def drive(self,distance):
		time = distance/self.speed
		print time
car1 = Car()
car1.speed = 60.0
car1.drive(100.0)
car1.drive(200.0)