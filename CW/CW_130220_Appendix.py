# 5.  Написати функцію, яка обчислює суму цифр введеного числа.

    

# 6.  Написати програму калькулятор, яка складається з наступних функцій: 
# головної, яка пропонує вибрати дію та додаткових, які реалізовують вибрані дії, 
# калькулятор працює доти, поки ми не виберемо дію вийти з калькулятора, після виходу, 
# користувач отримує повідомлення з подякою за вибір нашого програмного продукту!!!


# 7.  Побудувати рекурсивну функцію обчислення чисел Фібоначі до числа введеного користувачем.





# 8.  Написати програму, яка обчислює дискримінант квадратного рівняння і обчислює його корені
def Discriminant (a, b, c):
    D = (b**2)-4*a*c
    if D <0:
        return "There is no roots of your equation"            
    elif D >0:
        x1=(-b+(D)**(1/2))/(2*a)
        x2=(-b-(D)**(1/2))/(2*a) 
        return "The roots of your equation: x1 = "+str(round(x1,4))+", x2 = "+str(round(x2,4)
    else:
        return "The x = "+str(round(-b/(2*a),4))+" root of your equation"
         
a=int(input('Hi, I can solve your Quadratic equation of view: a*x^2+b*x+c \nPlease enter the a coefficient of Quadratic equation: '))
while a==0:
    print('\nThis equation isn\'t Quadratic!!!')
    a=float(input('Please enter the a coefficient of Quadratic equation\n(a must not be 0): '))
    continue
b=float(input('Please enter the b coefficient: '))
c=float(input('Please enter the c coefficient: '))

print(Discriminant(a,b,c))