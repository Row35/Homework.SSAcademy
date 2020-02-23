file = open('1.txt') 
a = file.read()
#subtask1
b=a.count('better')
e=a.count('never')
f=a.count('is')
print(f"the word 'better' was mentioned {b} times")
print(f"the word 'never' was mentioned {e} times")
print(f"the word 'is' was mentioned {f} times.")
#subtask2 
print("\n", a.upper())
#subtask2
print("\n", a.replace('i', '&'))