# list slice
a = [1, 2, 3, 4, 5]
print(a[0:3])

b= [1,2, [3,5]]
print(b[2][:1])

# list operation
c = [1]
d= [4,5,6,7,8]
print(c+d)
print(c*d[0])

print (len(d))
d[d[0]] = 10
print(d)
del d[4] # 모든 data type에 "del 객체" 형식으로 사용가능.
print(d)
del d[:2]
print(d)

# list methods
d.append(1)
print(d)
d.append([12,13]) 
# append로는 어떠한 data type도 추가 가능.
# d.sort()
print(d)
d.reverse()
print(d)

s = ['apple', 'banana', 'carrot']
print(s.index('banana'))
# list 에 대한 find 는 없나...?

s.insert(2,'pineapple')
print(s)

s.remove('apple') # remove는 del 과 달리 index가 아닌 원소로 접근.
print(s)
print(s.pop(), s)