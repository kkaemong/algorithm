T = int(input())
for tc in range(1, T + 1):
    N,M = map(int,input().split())

    arr = [list(map(int,input().split())) for _ in range(N)]
    ans = 0

    for i in range(N):
        bns = 0
        for j in range(N):
            if arr[i][j] == 1:
                bns += 1
            else:
                if bns == M:
                    ans += 1
                bns = 0

        if bns == M:
            ans += 1

    for i in range(N):
        bns = 0
        for j in range(N):

            if arr[j][i] == 1:
                bns += 1
            else:
                if bns == M:
                    ans += 1
                bns = 0
        if bns == M:
            ans += 1

    print(f'#{tc} {ans}')