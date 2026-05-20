T = int(input())
for tc in range(T):
    n,m = list(map(int,input().split()))
    fly = [list(map(int,input().split())) for _ in range(n)]

    ans = 0
    for i in range(n-m+1):
        for j in range(n-m+1):
            cnt = 0
            for x in range(i,m+i):
                for y in range(j,m+j):
                    cnt += fly[x][y]
            if cnt > ans:
                ans = cnt
    print(f'#{tc+1} {ans}')