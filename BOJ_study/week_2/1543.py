doc = str(input())
_search = str(input()) 
num = 0
for _ in range(50):
  for q in range(len(doc)):
    if doc[q : q + len(_search)] == _search:
      doc = doc[q  + len(_search) :]
      num+=1
      break
print(num)