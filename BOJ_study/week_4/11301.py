N = int(input())
DP = [0] *(N+1)
DP[0], DP[1] = 4,6
for q in range(2,N+1):
  DP[q] = DP[q-2] + DP[q-1]
print(DP[N-1])