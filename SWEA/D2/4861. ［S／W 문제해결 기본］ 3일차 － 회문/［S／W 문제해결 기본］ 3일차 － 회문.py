T = int(input())
for tc in range(1,T+1):
    N,M = map(int,input().split())
    arr = [list(input()) for _ in range(N)]

    ans = None

    for i in range(N):
        for j in range(N-M+1):
            sub = arr[i][j:j+M]
            if sub == sub[::-1]:
                ans = ''.join(sub)
                break
        if ans:
            break

    if not ans:
        for k in range(N):
            col = ''.join(arr[i][k] for i in range(N))
            for l in range(N-M+1):
                sub = col[l:l+M]
                if sub == sub[::-1]:
                    ans = sub
                    break
            if ans:
                break

    print(f'#{tc} {ans}')