# class Polygon:
#     def __init__(self, no_of_sides):
#         self.n = no_of_sides
#         self.sides = [0 for i in range(no_of_sides)]

#     def inputSides(self):
#         self.sides = [float(input("Enter side "+str(i+1)+" : ")) for i in range(self.n)]

#     def dispSides(self):
#         for i in range(self.n):
#             print("Side",i+1,"is",self.sides[i])

# class Triangle(Polygon):
#     def __init__(self):
#         Polygon.__init__(self,3)  #super().__init__(3) 

#     def findArea(self):
#         a, b, c = self.sides
#         s = (a + b + c) / 2
#         area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
#         print('The area of the triangle is %0.2f' %area)

# class Rectangle(Polygon):
#     def __init__(self):
#         Polygon.__init__(self,2)  #super().__init__(3) 

#     def findArea(self):
#         a, b = self.sides
#         area = a*b
#         print('The area of the rectangle is %0.2f' %area)

# class Quadrat(Polygon):
#     def __init__(self):
#         Polygon.__init__(self,1)  #super().__init__(3) 

#     def findArea(self):
#         a = self.sides
#         area = a[0]**2
#         print('The area of the quadrat is %0.2f' %area)
    
# t = Triangle()
# t1 = Rectangle()
# t2 = Quadrat()

# t.inputSides()
# t.dispSides()
# t.findArea()

# t1.inputSides()
# t1.dispSides()
# t1.findArea()

# t2.inputSides()
# t2.dispSides()
# t2.findArea()


# 1.  Створити клас машина з атрибутами name,  make, model та методами start та stop, 
# які виводять інформацію про те що автомобіль стартував чи зупинився відповідно.
# class Car():
#     def __init__ (self, name, make, model):
#         self.name=name
#         self.make=make
#         self.model=model

#     def start(self):
#         print ("The car " + self.name +" "+ self.model + " from " + self.make + " started")
#     def stop(self):
#         print ("The car " + self.name +" "+ self.model + " from " + self.make + " stoped")

# new_car=Car("Toyota", "Japan", "Raw4")
# new_car.start()
# new_car.stop()


# 2.  Створити клас особа,  в якому конструктор встановлює ім’я, а метод info виводить повідомлення 
# “Hello, my name is {ім’я конкретного екземпляра класу}”, а також створити клас автомобіль, 
#  в якому конструктор встановлює ім’я, а метод move виводить повідомлення


class Person():
	def __init__(self)
		self.name=input("Enter your name: ")
	def info(self):
		print (f"Hello, my name is {self.name})

class Auto():
	def __init__(self)
		self.name=input("Enter your's car name: ")
	def move(self):
		print (f"Hello, my name is {self.name})