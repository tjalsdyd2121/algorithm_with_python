n, s, r = map(int,input().split())
s_set = list(map(int,input().split()))
#for _ in range(s)
r_set = list(map(int,input().split()))

able = [True] * (n+1) # use 1 ~ n
for q in range(s):
  able[s_set[q]] = False

for q in range(n+1):
  if (not able[q]) &  ((q) in r_set):
    r_set.remove(q)
    able[q] = True

for q in range(n+1):
  if not able[q]:
    #print(able)
    if ((q) in r_set):
      r_set.remove(q)
    elif (q-1) in r_set:
      r_set.remove(q-1)
    elif (q+1) in r_set:
      r_set.remove(q+1)
    else :
      continue
    able[q]= True
print(able.count(False))
