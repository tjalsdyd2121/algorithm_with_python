# version with in & out
def add_func(a,b):
  return a+b
# note that a and b is parameter,
print(add_func(1,2))
# 1 and 2 are argument.

# version with only out
def hello_world():
  print("hello world!")

hello_world()

# version with unknown # of parameter.
# same as C !

def add_many(*args):
  result = 0
  for i in args:
    result = result + i
  return result

print(add_many(1,2,3,4,5,6))

# keyword parameter
def print_kw_args(**kwargs):
  print(kwargs)

print_kw_args(a=65, b=66)

# detail about return value
def add_and_mul(a,b):
  return a+b,a*b
print(add_and_mul(1,2))
# add , mul = add_and_mul(2,3)
# seems like error, but it returns >> tuple <<.


# init value with parameter
def hanroro(han,ro,rooo = "^___^"):
  print(han)
  print(ro)
  if rooo == "^___^":
    print("happy")
  else:
    print("...what")

hanroro('hanroro','is')
# whether insert rooo or not, it does not occur error.
# init value must be later of non-init parameter.
# e.g : hanroro(han,rooo = "^___^",ro)
#        hanroro('hanroro', 'is')    ---> error. dont know where to put it.

# local variable with parameter.
# there is no method like "*" OR "&" as C lang
var = 1

def vartest(a):
  a = a+1
  return a

var = vartest(var)
print(var)

def vartest_():
  global var
  var +=1

vartest_()
print(var)

# simple function : lambda.

add_last = lambda c,d:c+d
no_return = add_last(4,5)
# lambda works with no return.
print(no_return)