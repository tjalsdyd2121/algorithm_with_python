import sys
#sys.stdin = open('input.txt')
T = int(sys.stdin.readline())
for _ in range(T):
  N = int(sys.stdin.readline())
  DP = [0] * (N+5)
  DP[0],DP[1],DP[2],DP[3],DP[4] = map(int,[1,1,1,2,2])
  for q in range(5,N+1):
    DP[q] = DP[q-5]+DP[q-1]
  print(DP[N-1])