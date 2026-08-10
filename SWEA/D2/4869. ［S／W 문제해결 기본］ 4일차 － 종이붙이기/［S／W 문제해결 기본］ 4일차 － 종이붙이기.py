T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    n = N // 10

    dp = [0] * (n + 1)
    dp[0] = 1
    if n >= 1:
        dp[1] = 1
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + 2 * dp[i - 2]

    print(f'#{tc} {dp[n]}')