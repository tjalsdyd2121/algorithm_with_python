n = int(input())
DP = [1] * (n+2)
for q in range(2,n+1):
  DP[q] = DP[q-1] + DP[q-2]
print(DP[n] % 10007)