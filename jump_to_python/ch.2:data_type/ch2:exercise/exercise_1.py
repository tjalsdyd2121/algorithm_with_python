# exercise 1 
lang,english ,mathmatics = 80,75,55
avg = (lang + english + mathmatics ) / 3

print(int(avg))

# exercise 2
num = 13
if num % 2 == 0:
  print("짝수")
else:
  print("홀수")

# exercise 3 
id = "881120-1068234"
birth = id[:id.find("-")]
extra = id[id.find("-") + 1 :]

print(birth, extra)

# exercise 4
gender = id[id.find('-')+1:id.find('-')+2]
print(gender)

# exercise 5
text1 = "a:b:c:d"
text2 = text1.replace(":","#")
print(text2)

# exercise 6
a = [1,3,5,4,2]
a.sort()
a.reverse()
print(a)

# exercise 7
b = ['Life', 'is', 'too', 'short'] 
c = " ".join(b)
print(c)

# exercise 8 
tpl = (1,2,3)
tpl = tpl + (4,)
print(tpl)

# exercise 9
matter = """
a = dict()
a
{}
"""
a = dict()
#a[[]] = 'python'
#print(a.pop([]))
# a[[]] = 'python'
# ~^^^^
# TypeError: unhashable type 'list'

# exercise 10
a = {'A' : 10 , 'B' : 20}
val = a.pop('B')
print(val)

# exercise 11 : set has no duplication
a = {1,2,3,3,4}
set = set(a)
print(set)

# exercise 12 : 파이썬은 다음처럼 동일한 값에 여러 개의 변수를 선언할 수 있다.
# 다음과 같이 a, b 변수를 선언한 후 a의 두 번째 요솟값을 변경하면 b 값은 어떻게 될까? 
# 그리고 이런 결과가 오는 이유에 대해 설명해 보자.
prob = """
>>> a = b = [1, 2, 3]
>>> a[1] = 4
>>> print(b)

 [1, 4, 3]
"""

