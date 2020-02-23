# 1.  Напишіть скрипт-гру, яка генерує випадковим чином число з діапазону 
# чисел від 1 до 100 і пропонує користувачу вгадати це число. 
# Програма зчитує числа, які вводить користувач і видає користувачу підказки
#  про те чи загадане число більше чи менше за введене користувачем. 
#  Гра має тривати до моменту поки користувач не введе число, яке загадане програмою, 
#  тоді друкує повідомлення привітання. 
# (для виконання завдання необхідно імпортувати  модуль random, 
# а з нього функцію randint())

import random
name=input("please, enter your name: ")
user_num=int(input(f"Hi {name}. This the Number game. \n I choose the number, \n try to guess) \n write your suggestion = "))
pc_num=random.randint(0, 100)
while True:
    user_num=int(input("Wrong! please enter next suggest number = "))
    if user_num==pc_num:
        print (f"Congradulations {name}. You win!!!")
        break
    elif user_num<pc_num:
        print ("you need to write bigger number")
    elif user_num>pc_num:
        print ("you need to write less number")     
    
# 2.  Напишіть скрипт, який обчислює площу прямокутника a*b, 
# площу трикутника 0.5*h*a, площу кола pi*r**2. 
# (для виконання завдання необхідно імпортувати  
# модуль math, а з нього функцію pow() та значення змінної пі).

from math import pi as Pi, pow

def sqr_circle():
    radius=(int(input("Please, enter the radius = ")))
    return Pi*pow(radius, 2)
def area_triangle ():
    a=int(input("Please, enter the triangle\'s base = "))
    h=int(input("Please, enter the triangle\'s height = "))
    return 0.5*a*h
def area_rectangle ():
    a=int(input("Please, enter the rectangle\'s lenght = "))
    b=int(input("Please, enter the rectangle\'s wight = "))
    return a*b

area=int(input('Hi, Please choose which figure\'s area do you want to calculate?\n0-circle, 1-triangle or 2-rectangle \n = '))
while area<0 or area>2:
    print('Wrong number')
    area=int(input('Hi, Please choose which figure\'s area do you want to calculate?\n0-circle, 1-triangle or 2-rectangle \n = '))
    continue
if area==0:
    print(sqr_circle())
if area==1:
    print(area_triangle ())
elif area==2:
    print(area_rectangle ())