from copy import copy

a = [1,2,3]
b = a
print(b is a)

c = a[:]
print(c is a)

d = copy(a)
print(d is a)

[ex1, ex2] = ['a','b']
print(ex1, ex2)
ex3 = ex4 = ["k","t"]
print(ex3 is ex4)

# How to >>> Swap <<< variable
a1 , a2 = 5,6
a1,a2 = a2,a1
print(a1, a2)