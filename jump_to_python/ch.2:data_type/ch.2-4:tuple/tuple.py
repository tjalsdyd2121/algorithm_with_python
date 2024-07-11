t1 = ('a', ) # tuple must have comma even with one element.
t2= ('a', 'b', 'c', 1, 2, 3)
t3 = 'a', 'b', 'c', 1, 2, 3 # tuple can be written without parenthesis.

# tuple cannot be modiifed or deleted.

t4 = t3[:4] 
t5 = t1 * 4
t6 = t2 + t3
a = len(t6)
# tupple can be sliced and operated as like list.
print(t4)