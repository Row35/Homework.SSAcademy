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

# while True:
#     for i in range(0, 5):
#         line = f"Loading{'.' * i: <12}"
#         print(line, end="\r")


# 5.  Написати функцію, яка обчислює суму цифр введеного числа.
# def sum_of(number):
#     sum = 0
#     for i in number:
#         sum += int(i)
#     return "суму цифр введеного числа: "+str(sum)

# num=input('Please enter the number: ')
# print(sum_of(num))


 

# 6.  Написати програму калькулятор, яка складається з наступних функцій: 
# головної, яка пропонує вибрати дію та додаткових, які реалізовують вибрані дії, 
# калькулятор працює доти, поки ми не виберемо дію вийти з калькулятора, після виходу, 
# користувач отримує повідомлення з подякою за вибір нашого програмного продукту!!!
# print("This is the simple calculator. Please choose your operation from list: \n1.Add; 2.Subtract; 3.Multiply; 4.Divide; \nQ.Quit")

# def calc(num1, num2): 
#     if choice == '1':
#         return str(num1)+" + "+str(num2)+" = "+ str(num1+num2)
#     elif choice == '2':
#         return str(num1)+" - "+str(num2)+" = "+ str(num1-num2)
#     elif choice == '3':
#         return str(num1)+" * "+str(num2)+" = "+ str(num1*num2)
#     elif choice == '4':
#         return str(num1)+" / "+str(num2)+" = "+ str(num1//num2)

# while True:
#     choice = input("Enter choice(1/2/3/4) or q for quit: ")
#     if choice=="q" or choice=="Q": 
#         print("thank you for you choise, good bye!")
#         break
#     if choice in ("1", "2", "3", "4"):
#         num1 = float(input("Enter first number: "))
#         num2 = float(input("Enter second number: "))
#         print (calc(num1, num2))
#         continue
#     else:
#         print("Wrong input!")
#         continue 



# 7.  Побудувати рекурсивну функцію обчислення чисел Фібоначі до числа введеного користувачем.
        
# fib=int(input("insert last n in Fib series = "))
# x, y = 0, 1
# print('Fibo series = 0, ', end= '')
# while y<fib:
#     print(y, end=', ')
#     x,y = y,x+y



# 8.  Написати програму, яка обчислює дискримінант квадратного рівняння і обчислює його корені
# def Discriminant (a, b, c):
#     D = (b**2)-4*a*c
#     if D<0:
#         return "There is no roots of your equation"            
#     if D==0:
#         x1=-b/(2*a)
#         return f"The x={round(x1,4)} root of your equation"
#     else:
#         x1=(-b+(D)**(1/2))/(2*a)
#         x2=(-b-(D)**(1/2))/(2*a) 
#         return f"The roots of your equation: x1={round(x1,4)}, x2={round(x2,4)}"
         
# a=float(input('Hi, I can solve your Quadratic equation of view: a*x^2+b*x+c \nPlease enter the a coefficient of Quadratic equation: '))
# while a==0:
#     print('\nThis equation isn\'t Quadratic!!!')
#     a=float(input('Please enter the a coefficient of Quadratic equation\n(a must not be 0): '))
#     continue
# b=float(input('Please enter the b coefficient: '))
# c=float(input('Please enter the c coefficient: '))

# print(Discriminant(a,b,c))


    
   