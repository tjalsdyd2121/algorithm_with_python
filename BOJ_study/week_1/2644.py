#input
n = int(input())
start, end = map(int, input().split())
edge = int(input())

adj = [[False] * (n+1) for q in range(n+1)]
visit = [False] * (n+1)

for q in range(1, edge+1):
  i, j = map(int, input().split())
  adj[i][j] = True
  adj[j][i] = True

# compute the depth from start to end

# DFS by recursion
def DFS(cur, end, depth):
  global result
  if cur == end :
    result = depth
    return 
  
  for q in range(1, n+1):
    if adj[cur][q] & (not visit[q]):
      visit[q] = True
      DFS(q,end,depth+1)

result = -1
visit[start] = True
DFS(start,end,0)
print(result)