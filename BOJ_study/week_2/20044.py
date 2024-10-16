T = int(input())
S = list(map(int,input().split()))
min = 199999
group = [[0,0] for _ in range(T)]
S.sort()
for q in range(T):
  group[q][0] = S[q]
  group[q][1] = S[2*T - 1 - q] 
  if min > sum(group[q]):
    min = sum(group[q])
print(min)
  