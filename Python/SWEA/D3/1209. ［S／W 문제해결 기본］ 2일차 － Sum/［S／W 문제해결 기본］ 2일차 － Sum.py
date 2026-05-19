T = 10
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(100)]
    ans = 0
    for i in range(100):
        num = 0
        num2 = 0
        num3 = 0
        num4 = 0
        for j in range(100):
            num += arr[i][j]
            num2 += arr[j][i]
            num3 += arr[j][j]
            num4 += arr[j][100-1-j]

        ans = max(ans,num,num2,num3,num4)

    print(f'#{tc} {ans}')