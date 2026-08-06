T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = [list(input()) for _ in range(N)]
         #왼, 위, 아래, 오
    dx = [0, -1, 1, 0]
    dy = [-1, 0, 0, 1]

    for i in range(N):
        for j in range(N):
            if arr[i][j] == '2':
                start_i, start_j = i,j

    visited = [[False] * N for _ in range(N)]
    stack = [(start_i, start_j)]
    visited[start_i][start_j] = True
    found = 0

    while stack:
        x, y = stack.pop()

        if arr[x][y] == '3':
            found = 1
            break

        for c in range(4):
            nx = x + dx[c]
            ny = y + dy[c]
            if 0 <= nx < N and 0 <= ny < N:
                if arr[nx][ny] != '1' and not visited[nx][ny]:
                    visited[nx][ny] = True
                    stack.append((nx, ny))

    print(f'#{tc} {found}')