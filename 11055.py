import sys
num = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().rstrip().split()))
dp = [l for l in A]
for i in range(num):
    for j in range(i):
        if A[j] < A[i] and dp[j] + A[i] > dp[i]:
            dp[i] = dp[j] + A[i]
print(max(dp))