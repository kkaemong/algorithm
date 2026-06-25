for _ in range(1, 11):
    tc = int(input())
    T = 100
    arr = [list(map(int, input().split())) for _ in range(T)]

    # 좌, 우, 위
    dx = [0, 0, -1]
    dy = [-1, 1, 0]

    for i in range(T):
        if arr[T-1][i] == 2: # 99 대신 T-1 사용
            x = T-1
            y = i
            break

    while x != 0:
        for d in range(3):
            nx = x + dx[d]
            ny = y + dy[d]

            if 0 <= nx < T and 0 <= ny < T and arr[nx][ny] == 1:
                # [중요] 이동한 곳을 0으로 만들어 다시 되돌아가지 않게 함
                arr[x][y] = 0
                x = nx
                y = ny
                break

    print(f'#{tc} {y}')