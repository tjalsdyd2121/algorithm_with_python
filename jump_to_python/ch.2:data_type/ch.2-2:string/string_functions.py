# count # of character
a= 'apple'
print(a.count('p'))

# find index of character
b = "Python is the best choice"
print(b.find('t'))
print(b.find('k'))

print(b.index('t'))
# print(b.index('k'))
# index 는 find 와 달리 char가 string에 없으면 오류 발생.

# insert some character or string
print(",".join('abcd'))
print(",,".join('abcd'))


# strip space
c = " hi "
print(c.strip())
print(c.lstrip())
print(c.rstrip())

# replace string __replace(바뀔_문자열, 바꿀_문자열)
a = "Life is too short"
print(a.replace("Life", "Your leg"))

# split
f= '''life is 
too  short'''
print(f.split()) # split() 은 enter, tab, space를 기준으로.

