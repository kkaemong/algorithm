T = int(input())

for tc in range(1,T+1):
    N, M = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(N)]
            # 상 하 좌 우
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]

    ans = 0
    for i in range(N):
        for j in range(M):

            cnt = arr[i][j]
            k = arr[i][j]

            for d in range(4):
                for dist in range(1, k + 1):  # 1칸부터 k칸까지 뻗어 나감
                    nx = i + dx[d] * dist
                    ny = j + dy[d] * dist

                    # 범위 체크: 0 이상이고 N, M 미만이어야 함
                    if 0 <= nx < N and 0 <= ny < M:
                        cnt += arr[nx][ny]
                    else:
                        # 경계를 벗어나면 더 이상 뻗어 나갈 필요가 없음 (break)
                        break

            ans = max(cnt,ans)

    print(f'#{tc} {ans}')