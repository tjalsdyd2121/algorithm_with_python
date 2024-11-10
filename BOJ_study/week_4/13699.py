import sys
N = int(sys.stdin.readline())
DP = [0] * (N+1)
DP[0] = 1
if N:
  DP[1] =1
for q in range(2,N+1):
  if (q%2):
    # q is odd
    DP[q] += DP[q//2] ** 2
    for w in range(q//2):
      DP[q] += 2 * (DP[w]*DP[q-1-w])
  else :
    # q is even
    for w in range(q//2):
      DP[q] += 2 * (DP[w]*DP[q-1-w])
print(DP[N])
  