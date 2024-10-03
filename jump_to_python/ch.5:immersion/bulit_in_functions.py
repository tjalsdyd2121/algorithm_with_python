print(all([1,2,3]))
print(all([1,2,3,0]))
# Like loop for AND.

print(any([1,0,0,0]))
print(any((0,0,0)))
# Like loop for OR.

# enumrate.
for q, name in enumerate(['alice','bob','me']):
  print(q,name)


# filter. literally, it does filter.
def positive(x):
    return x > 0

print(list(filter(positive, [1, -3, 2, 0, -5, 6])))

# Or, not with function, but lambda !
print(list(filter(lambda x : x >0, [1,2,3,-1,0])))

# map. == kind of filter, but more flexible use
def multiple(x):
  return x*2

print(list(map(multiple,[1,2,3,4])))