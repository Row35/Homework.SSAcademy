print("This is the simple calculator. Please choose your operation from list: \n1.Add; 2.Subtract; 3.Multiply; 4.Divide; \nQ.Quit")

def calc(num1, num2): 
    if choice == '1':
        return str(num1)+" + "+str(num2)+" = "+ str(num1+num2)
    elif choice == '2':
        return str(num1)+" - "+str(num2)+" = "+ str(num1-num2)
    elif choice == '3':
        return str(num1)+" * "+str(num2)+" = "+ str(num1*num2)
    elif choice == '4':
        return str(num1)+" / "+str(num2)+" = "+ str(num1//num2)

while True:
    choice = input("Enter choice(1/2/3/4) or q for quit: ")
    if choice=="q" or choice=="Q": 
        print("thank you for you choise, good bye!")
        break
    if choice in ("1", "2", "3", "4"):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        print (calc(num1, num2))
        continue
    else:
        print("Wrong input!")
        continue    