import sys
N = int(sys.stdin.readline())
pre = sorted([int(sys.stdin.readline()) for _ in range(N)])
ans = [abs(pre[q]-(q+1)) for q in range(N)]
print(sum(ans))