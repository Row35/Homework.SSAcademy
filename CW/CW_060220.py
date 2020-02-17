# 1 number comparison
a=int(input("insert a = "))
b=int(input("insert b = "))
if a > b:
    print (f"{a} more than {b}")
if a < b:
    print (f"{a} less than {b}")
elif a==b:
    print (f"{a} equall {b}")

# 2 number comparison even or odd
a=int(input("insert a = "))
if not(a%2 == 0):
    print ("value of a= {} is odd " .format(a))
else: 
    print ("value of a= {} is even".format(a))

# 3 factorial
a=int(input("insert a = "))
fct=1
for i in range(a): 
    fct = fct * (i+1) 
print (f"The factorial of your number is : {fct}",end="") 

# 4.w Роздрукувати всі парні числа менші 100 (написати два варіанти коду: один використовуючи цикл while) 
even = 0
print("printed all even number up to 100: ", end='')
while even < 100:
    print
    print(even, end=" ")
    even += 2

# 4.f Роздрукувати всі парні числа менші 100 (з використанням циклу for).
even=range(100)
print("printed all even number up to 100: ", end='')
f=0
for i in even:
    print(f, end=" ")
    f=f+2
    if f>100:
        break

# other
print("printed all odd number up to 100: ", list(range(1,100,2)))
print("printed all even number up to 100: ", list(range(0,101,2)))
  
# 5.1 Роздрукувати всі непарні числа менші 100. (написати два варіанти коду: один використовуючи оператор continue, а інший без цього оператора).
print("all odd number up to 100: ", end='')
for odd in range(100):
  if odd %2 ==0 :
    continue
  print(odd, end=' ')

# 5.2 Роздрукувати всі непарні числа менші 100.без цього оператора continue
print("printed all even number up to 100: ", list(range(0,101,2)))

# other 5.2
odd = 1
print("printed all odd number up to 100: ", end='')
while odd < 100:
    print
    print(odd, end=" ")
    odd += 2

# 6  Перевірити чи список містить непарні числа.
s = [7, 2, 3]
for n in s:
    if not(n % 2==0):
        pass
    else:
        print('list consist the even number')
        break
else:
    print('list doesn\'t consist the even number')
       

# 7 Створити список, який містить елементи цілочисельного типу, потім за допомогою циклу перебору змінити тип даних елементів на числа з плаваючою крапкою. 
# Підказка: використати вбудовану функцію float.
l=[7, 5, 3, 4]
counter = 0
for i in l:
    l[counter] = float(l[counter])
    counter = counter+1
print(l , end=' ')


# 5.  Вивести числа Фібоначі включно до введеного числа n, використовуючи цикли. (Послідовність чисел Фібоначі 0, 1, 1, 2, 3, 5, 8, 13 і т.д.)
fib=int(input("insert last n in Fib series = "))
x, y = 0, 1
print('Fibo series = 0, ', end= '')
while y<fib:
    print(y, end=', ')
    x,y = y,x+y