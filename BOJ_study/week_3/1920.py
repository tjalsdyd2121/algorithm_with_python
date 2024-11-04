from math import ceil
import sys
def Bsearch(A,target):
  loc_pivot = ceil((len(A))/2)
  if target == A[loc_pivot-1]:
    print(1)
  elif len(A) == 1:
    print(0)
  elif target > A[loc_pivot-1]:
    #print(A[pivot])
    Bsearch(A[loc_pivot:],target)
  else:
    #print(A[: loc_pivot], loc_pivot)
    Bsearch(A[:loc_pivot],target)
  
N = int(sys.stdin.readline())
A = sorted(map(int,sys.stdin.readline().split()))
M = int(sys.stdin.readline())
for q in list(map(int,sys.stdin.readline().split())):
  Bsearch(A,q)