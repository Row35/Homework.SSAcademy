# # 1.  Написати функцію, яка знаходить середнє арифметичне значення довільної кількості чисел. 
# def mid(*numlist):
#     print(sum(numlist)/len(numlist))
# mid(10, 20, 17, 90)

# 2.  Написати функцію, яка повертає абсолютне значення числа
# def abs_n(a):
#     print(f"absolut value of this number is: {abs(a)}")
# abs_n(int(input('enter the number = ')))

# ver02
# abs_n =int(input('enter the number = '))
# if abs_n >=0:
#     print(f"abs of your nmber = {abs_n }")
# else:
#     print(f"abs of your nmber = {abs_n *-1}")


# # 3.  Написати функцію, яка знаходить максимальне число з двох чисел, 
# # а також в функції використати рядки документації DocStrings.
# def max_of_two(a=0, b=0):

#     return(a if a > b else b)
# def max_finder (num1, num2):
#   '''Написати функцію, яка знаходить максимальне число з двох чисел'''
#   if num1>num2:
#     print (f"{num1} is max number")
#   else:
#     print (f"{num2} is max number")
# max_finder(int(input("Please, enter the 1st number = ")), int(input("Please, enter the 2nd number to compare = ")))



# 4.  Написати програму, яка обчислює площу прямокутника, 
# трикутника та кола (написати три функції для обчислення площі, 
# і викликати їх в головній програмі в залежності від вибору користувача)

# area=int(input('Hi, Please choose which figure\'s area do you want to calculate?\n0-circle, 1-triangle or 2-rectangle \n = '))
# while area<0 or area>2:
#     print('Wrong number')
#     area=int(input('Hi, Please choose which figure\'s area do you want to calculate?\n0-circle, 1-triangle or 2-rectangle \n = '))
#     continue
# if area==0:
#     def circle(radius):
#         Pi=3.14
#         print(f"The circle\'s square is: {Pi*radius**2}")
#     circle(int(input("Please, enter the radius = ")))
# if area==1:
#     def triangle(b, h):
#         print(f"The triangle\'s area is: {abs(0.5*b*h)}")
#     triangle(int(input("Please, enter the base = ")), int(input("Please, enter the height = ")))    
# elif area==2:
#     def rectangle(b, h):
#         print(f"The rectangle\'s area is: {abs(b*h)}")
#     rectangle(int(input("Please, enter the lenght = ")), int(input("Please, enter the wight = "))) 


# #ver02
# def sqr_circle():
#     Pi=3.14
#     radius=(int(input("Please, enter the radius = ")))
#     return Pi*radius**2
# def area_triangle ():
#     a=int(input("Please, enter the triangle\'s base = "))
#     h=int(input("Please, enter the triangle\'s height = "))
#     return 0.5*a*h
# def area_rectangle ():
#     a=int(input("Please, enter the rectangle\'s lenght = "))
#     b=int(input("Please, enter the rectangle\'s wight = "))
#     return a*b

# area=int(input('Hi, Please choose which figure\'s area do you want to calculate?\n0-circle, 1-triangle or 2-rectangle \n = '))
# while area<0 or area>2:
#     print('Wrong number')
#     area=int(input('Hi, Please choose which figure\'s area do you want to calculate?\n0-circle, 1-triangle or 2-rectangle \n = '))
#     continue
# if area==0:
#     print(sqr_circle())
# if area==1:
#     print(area_triangle ())
# elif area==2:
#     print(area_rectangle ())


while True:
    for i in range(0, 5):
        line = f"Loading{'.' * i: <12}"
        print(line, end="\r")
   