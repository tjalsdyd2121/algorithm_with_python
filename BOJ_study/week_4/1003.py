import sys
#sys.stdin = open('input.txt')
T = int(sys.stdin.readline())
DP, Ns= [0,1,1], [2] * (T+1)
for q in range(1,T+1):
  N = int(sys.stdin.readline())
  Ns[q] = N
  if N > Ns[q-1]:
    for w in range(len(DP), N +1):
      DP.append(DP[w-1] + DP[w-2])
  if N:
    print(DP[N-1], DP[N])
  else :
    print(1,0)