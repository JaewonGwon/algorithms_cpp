import sys
num = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().rstrip().split()))
dp = [0 for i in A]
dp[0] = A[0]
for i in range(len(A)):
    for j in range(i):
        if A[j] < A[i] and dp[j] + A[i] >= dp[i]:
            dp[i] = dp[j] + A[i]
sys.stdout.write(str(max(dp)))