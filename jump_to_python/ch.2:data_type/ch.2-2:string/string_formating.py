# basic formating
a = 1/3
number, day = 3, 2
print("I eat %.10f apples." % a)
print("I ate %d apples. so I was sick for %s days." % (number, day))
# ----------------------------------------

# format function
b = 'i ate {number} {fruits}'
c = b.format(number=3, fruits='apples')
b1 = 'i ate {0} {1}'
c1 = b1.format(6, 'bananas')
print(c)
print(c1)
# ----------------------------------------

# f string formating
name = '홍길동'
age = 30
print(f'나의 이름은 {name}입니다. 나이는 {age/2 :.0f}입니다.')
# 중괄호 안 맨 뒤에 : 를 넣어 소수점 표현 가능, 표현식 지원

