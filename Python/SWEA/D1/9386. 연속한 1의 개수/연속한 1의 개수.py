T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = input() + '0'

    ans = 0
    bns = 0
    for i in arr:
        if i == "1":
            bns += 1
        else:
            ans = max(bns,ans)
            bns = 0

    print(f'#{tc} {ans}')