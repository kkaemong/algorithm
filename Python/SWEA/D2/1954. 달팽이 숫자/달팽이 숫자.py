T = int(input())
for tc in range(1,T+1):
    N = int(input())
        # 오른쪽, 아래, 왼, 위
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    arr = [[0] * N for _ in range(N)]

    a, b, num, dir = 0, 0, 1, 0
    arr[a][b] = num
    num += 1

    while num <= N ** 2:
        nx = a + dx[dir]
        ny = b + dy[dir]
        if 0 <= nx < N and 0 <= ny < N and arr[nx][ny] == 0:
            a,b = nx, ny
            arr[a][b] = num
            num += 1
        else:
            dir = (dir + 1) % 4

    print(f'#{tc}')
    for num in arr:
        print(*num)