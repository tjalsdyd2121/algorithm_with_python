import sys  
for _ in range(int(input())):
  day = int(sys.stdin.readline())
  stock = list(reversed(list(map(int,sys.stdin.readline().split())))) 
  max = stock[0] 
  ans, num = 0,0 
  for q in range(day): 
    if  stock[q] >= max: 
      ans += (num * max) 
      max = stock[q] 
      num = 0 
    else: 
      num +=1 
      if q:
        ans -= stock[q]
    if q==day-1: 
      ans +=(num*max)
  print(ans)