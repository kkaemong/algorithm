T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))

    ans = 10e8
    bns = 0
    for i in range(N-M+1):
        num = sum(arr[i:i+M:])
        if num <= ans:
            ans = num
        if num >= bns:
            bns = num

    print(f'#{tc} {bns-ans}')