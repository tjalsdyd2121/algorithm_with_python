from copy import copy
# input frist line
vertex, edge, start_vertex = map(int, input().split())

# init adj_mat & visit
visit = [0 for q in range(vertex + 1)]

adj_matrix = []
tmp = []
for q in range(vertex + 1):
  tmp = []
  for w in range(vertex + 1):
    tmp.append(0)
  adj_matrix.append(tmp)

from_, to_ = 0, 0
for q in range(0, edge):
  from_, to_ = map(int, (input()).split())
  adj_matrix[from_][to_] = 1
  adj_matrix[to_][from_] = 1

adj_matrix_ = adj_matrix.copy()
# DFS with stack
DFS_ans = []

stack = [start_vertex]
cur_vertex = 0
while stack != []:
  # visit current node.
  cur_vertex = stack.pop()
  DFS_ans.append(cur_vertex)
  visit[cur_vertex] = 1
  # find next node
  for q in (range(vertex, 0, -1)):  # push them in  >> revere << order...
    # if there is edge and not visited
    if (adj_matrix[cur_vertex][q] == 1) & (visit[q] == 0): 
      # graph may not be Tree, we should handle it.......
      if q in stack:
        stack.remove(q)
      stack.append(q)
      
print(*DFS_ans)

visit = [0 for q in range(vertex + 1)]

# BFS with Queue
BFS_ans = []

qu = [start_vertex]
cur_vertex = start_vertex
while qu != []: 
  cur_vertex = qu[0]
  for i in range(vertex+1):
    if (adj_matrix_[cur_vertex][i] == 1) & (visit[i] == 0):
      if i not in qu:
        qu.append(i)

  del qu[0]
  BFS_ans.append(cur_vertex)
  visit[cur_vertex] = 1
  

print(*BFS_ans)
  