# 1.  Створити клас машина з атрибутами name,  make, model 
# та методами start та stop, які виводять інформацію про те
#  що автомобіль стартував чи зупинився відповідно.

class Car():
    def __init__ (self, name, make, model):
        self.name=name
        self.make=make
        self.model=model

    def start(self):
        print ("The car " + self.name +" "+ self.model + " from " + self.make + " started")
    def stop(self):
        print ("The car " + self.name +" "+ self.model + " from " + self.make + " stoped")

new_car=Car("Toyota", "Japan", "Raw4")
new_car.start()
new_car.stop()

# 2.  Створити клас особа,  в якому конструктор встановлює ім’я, 
# а метод info виводить повідомлення 
# “Hello, my name is {ім’я конкретного екземпляра класу}”, 
# а також створити клас автомобіль,  в якому конструктор встановлює ім’я, 
# а метод move виводить повідомлення

class Person():
	def __init__(self)
		self.name=input("Enter your name: ")
	def info(self):
		print (f"Hello, my name is {self.name})

class Auto():
	def __init__(self)
		self.name=input("Enter your's car name: ")
	def info(self):
		print (f"Hello, my name is {self.name})

