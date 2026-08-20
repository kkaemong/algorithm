def dfs(row, visited, total):
    global min_total
    if total >= min_total:   # 이미 최솟값보다 커지면 더 볼 필요 없음 (가지치기)
        return
    if row == N:
        min_total = min(min_total, total)
        return

    for col in range(N):
        if not visited[col]:
            visited[col] = True
            dfs(row + 1, visited, total + arr[row][col])
            visited[col] = False   # 백트래킹: 다시 시도할 수 있게 되돌림


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    visited = [False] * N
    min_total = float('inf')

    dfs(0, visited, 0)
    print(f'#{tc} {min_total}')