# 1.  Напишіть програму, яка пропонує користувачу ввести ціле число 
# і визначає чи це число парне чи непарне, чи введені дані коректні.

# try:
#     x=int(input("enter the natural number: "))
#     if x<0:
#         raise ValueError("Error!, Please write the NATURAL number")
#     if x%2==0:
#         print("number is even")
#     else:
#         print("number is odd")    
# except ValueError:
#     print ("Value Error!!!")
# except TypeError:
#     print ("TypeError")
# finally:
#     print("Try again")




# 2.  Напишіть програму, яка пропонує користувачу ввести свій вік, 
# після чого виводить повідомлення про те чи вік є парним чи непарним числом.
#  Необхідно передбачити можливість введення від’ємного числа, в цьому випадку 
# згенерувати власну виняткову ситуацію. Головний код має викликати 
# функцію, яка обробляє введену інформацію.

try:
    age = int(input("Enter your age: "))
    if age<0:
        raise ValueError("Error!, U not born yet")
    if age>170:
        print ("Hmm, Are u sure? I dont know any people with this age. Please try again")
    if age%2==0:
        print ("your age even")
    else:
        print ("your age odd") 
except ValueError:
    print ("ValueError!!!")
except TypeError:
    print ("TypeError!!!")
except SyntaxError:
    print ("SyntaxError!!!")
finally:
    print ("Try again")


# 3.  Напишіть програму для обчислення частки двох чисел, 
# які вводяться користувачем послідовно через кому, передбачити 
# випадок ділення на нуль, випадки синтаксичних помилок та випадки
#  інших виняткових ситуацій. Використати блоки else та finaly.


# try:
#     num1, num2 = eval(input("Enter two numbers separate by comma: "))
#     divis = num1 / num2
#     print(divis)
 
# except ZeroDivisionError:
#     print("division by zero!!!")
# except ValueError:
#     print("ValueError!!!")
# except SyntaxError:
#     print("SyntaxError!!!")
# else:
#     ("All is good!") 
# finally:
#     print("Try again")


# 4.  Написати  програму, яка аналізує введене число та в залежності 
# від числа видає день тижня, який відповідає цьому числу 
# (1 це Понеділок, 2 це Вівторок і т.д.) . Врахувати випадки введення 
# чисел від 8 і більше, а також випадки введення не числових даних.

# try:
#     week={1:"Monday", 2:"Tuesday", 3:"Wednesday", 4:"Thursday", 5:"Friday", 6:"Saturday", 7:"Sunday"}
#     num = int(input("Enter the number of day: "))
#     if num>7 and num<1:
        #key error if dict doesnt 
#         print("The week has 7 days, try again!")
#     else:
#         print (week[num])
# except ValueError:
#     print("ValueError!!!")
# except SyntaxError:
#     print("SyntaxError!!!")
# else:
#     ("All is good!") 
# finally:
#     print("Try again")



