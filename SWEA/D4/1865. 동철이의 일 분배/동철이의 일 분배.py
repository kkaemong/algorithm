def backtrack(total, idx):
    global ans

    if ans >= total:
        return

    if idx == N:
        ans = max(ans, total)
        return

    for i in range(N):
        if visited[i]:
            continue
        visited[i] = True
        backtrack(total * (arr[idx][i] / 100), idx + 1)
        visited[i] = False


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    ans = float('-inf')
    visited = [False] * N
    backtrack(1, 0)

    print(f'#{tc} {ans * 100:.6f}')