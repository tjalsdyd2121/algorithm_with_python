from collections import deque
#input
n = int(input())
map_ = []
border = [0] *(n+2)
map_.append(border)
for q in range(n):
  s = input()
  tmp = list(map(int,s))
  tmp.insert(0,0)
  tmp.append(0)
  map_.append(tmp)
map_.append(border)

visit = [[False] *(n+2) for _ in range(n+2)]

def BFS(target_x,target_y):
  q = deque([])
  q.append(target_x)
  q.append(target_y)
  visit[target_x][target_y] = True
  #print(target_x, target_y)
  num = 1
  while list(q) != []:
    x = q.popleft()
    y = q.popleft()
    
    if (map_[x+1][y] == 1) & (not visit[x+1][y]) :
      q.append(x+1)
      q.append(y)
      visit[x+1][y] = True
      num +=1
    if map_[x-1][y] == 1 & (not visit[x-1][y]):
      q.append(x-1)
      q.append(y)
      visit[x-1][y] = True
      num +=1
    if map_[x][y+1] == 1 & (not visit[x][y+1]):
      q.append(x)
      q.append(y+1)
      visit[x][y+1] = True
      num +=1
    if map_[x][y-1] == 1 & (not visit[x][y-1]):
      q.append(x)
      q.append(y-1)
      visit[x][y-1] = True
      num +=1
  
  return num


complex = []


for q in range(1,n+1):
  for w in range(1,n+1):
    if (not visit[q][w]) & (map_[q][w] == 1):
      complex.append(BFS(q,w))

print(len(complex))
complex.sort()
for q in range(len(complex)):
  print(complex[q])
