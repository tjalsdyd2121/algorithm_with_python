if 1==1:
  print("1==1")
else:
  print("what")

# indentation : 들여쓰기의 깊이는 항상 같아야함.

a = 6
if a % 2 == 0:
  if a % 3 == 0:
    print("6은 2와 3의 배수")

#if a % 2 || a % 3:
# surprised, we cant use || , && and ! in python...

if ~(a%3) & ~(a%2): print("a는 2와 3의 배수")

# || == | , && == & , ! == ~ ...
# we can use them as and, or , not 

if not(a%3) and not(a%2): print("a는 3과 2의 배수")

list = ["apple", "banana", "pineapple"]
if "apple" in list: print("what a revolution")
if "samsung" not in list : print("not trendy")
# could use in , not in with tuple and >>> string <<<
if "10" not in "1234567890" : print("not circular")

# conditional expression, or ternary operator in python : 
test = "c"
str = "control" if test == "c" else "statement"
print(str)