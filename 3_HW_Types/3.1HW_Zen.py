#Main text (?? how to read from file, conditions???)
a="""Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!"""
#subtask1
b=a.count('better')
e=a.count('never')
f=a.count('is')
print(f"the word 'better' was menteoined {b} times")
print(f"the word 'never' was menteoined {e} times")
print(f"the word 'is' was menteoined {f} times.")
#subtask2 
print("\n", a.upper())
#subtask2
print("\n", a.replace('i', '&'))