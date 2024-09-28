# basic use

list = ['han', 'ro','ro']
for q in list:
  print(q)

sum = 0
for q in range(11):
  print(sum)
  sum += q

# variable extract method 1

list2 = [(1,2),(2,3),(3,4)]
for (q,w) in list2:
  print(q+w)

# example
marks = [90, 25, 67, 45, 80]
for point in marks:
  if point >= 60:
    print("합격 축하")
  else:
    print("불합격")

# list comprehension [표현식 for 항목 in 반복_가능_객체 if 조건문]

a = range(5)
a3 = [num * 3 for num in a]
print(a3)
even_a = [num for num in a if num % 2 == 0]
print(even_a)
gugudan = [x*y for x in range(2,10)
          for y in range(1,10)]
print(gugudan)