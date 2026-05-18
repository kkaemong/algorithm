T = int(input())
for tc in range(1, T + 1):
    N = int(input())

    ans = [[0] * 10 for _ in range(10)]

    for _ in range(N):
        a,b,c,d,e = list(map(int,input().split()))
        for i in range(a,c+1):
            for j in range(b,d+1):
                ans[i][j] |= e
    bns = 0
    for x in range(10):
        for y in range(10):
            if ans[x][y] == 3:
                bns += 1

    print(f'#{tc} {bns}')