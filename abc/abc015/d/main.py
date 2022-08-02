W = int(input())
N, K = map(int, input().split())
A = [0] * N
B = [0] * N
for i in range(N):
    A[i], B[i] = map(int, input().split())
dp = [[[0 for _ in range(K + 1)] for _ in range(W + 1)] for _ in range(N + 1)]
for i in range(1, N + 1):
    for j in range(1, W + 1):
        for k in range(1, K + 1):
            if j - A[i - 1] >= 0:
                dp[i][j][k] = max(dp[i - 1][j][k], dp[i - 1][j - A[i - 1]][k - 1] + B[i - 1])
print(dp[N][W][K])