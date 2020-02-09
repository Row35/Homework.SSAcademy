# Посортувати цифри, що входять в дане число
a=(input("insert 4-digit number = "))

# #print multiply of digits
z=(int(a)%10)*(int(a)//10%10)*(int(a)//10//10%10)*(int(a)//10//10//10%10)
print(f"multiplyed digits of your number equal {z}")

# #print multiply of digits_2
# m = 1
# for i in a:
#     m *= int(i)
# print (f"multiply of digits equal {m}")

# #print multiply of digits_3
# a=int(a)
# m = 1
# while a > 0:
#     d = a % 10
#     m *= d
#     a = a // 10
# print (f"multiply of digits equal {m}")

#reversed
print ("reversed = {j}{k}{l}{m}".format(j=a[-1], k=a[-2], l=a[-3], m=a[-4]))

# #reversed_2
# print("_".join(reversed(a)))

# digit ordered
d=int(a)%10
s=int(a)//10%10
x=int(a)//10//10%10
y=int(a)//10//10//10%10
o=[d, s, x, y]
print ("ordered = ", sorted(o))

