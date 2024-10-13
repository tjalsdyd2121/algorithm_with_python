# DFS with cost
def isHappy():
  storenum = int(input())
  home = list(map(int,input().split()))
  store = []
  visit = [False]* (storenum)
  for _ in range(storenum):
    a = list(map(int,input().split()))
    store.append(a)
  rockFe = list(map(int,input().split()))

  #print(storenum, home, store, visit,rockFe)
  stack = []
  stack.append(home[:])
  walkable = 1000
  cur_loc = home[:]
  answer = False
  #print(answer)

  def DFS_with_cost(cur,rockFe):
    nonlocal answer
    #print('cur', cur)
    #print('sum' , sum(abs(cur[i] - rockFe[i]) for i in range(2)))
    if sum(abs(cur[i] - rockFe[i]) for i in range(2)) <= walkable:
      answer = True
      return
    for q in range(storenum):
      
      #print(sum(abs(cur[i] - store[q][i]) for i in range(2)))
      if (sum(abs(cur[i] - store[q][i]) for i in range(2)) <= walkable) & (not visit[q]):
        #print('cur', cur)
        visit[q] = True
        DFS_with_cost(store[q],rockFe)

  DFS_with_cost(cur_loc,rockFe)
  return answer

#for _ in range(testnum):

testnum = int(input())

for _ in range(testnum):
  if isHappy():
    print('happy')
  else : 
    print('sad')
