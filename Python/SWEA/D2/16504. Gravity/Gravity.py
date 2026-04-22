T = int(input())
for tc in range(T):
    N = int(input())
    arr = list(map(int, input().split()))

    max_cnt = 0
    for i in range(N):
        cnt = 0
        for j in range(i+1,N):
            if arr[i] > arr[j]:
                cnt += 1
        if cnt > max_cnt:
            max_cnt = cnt

    print(f'#{tc+1} {max_cnt}')