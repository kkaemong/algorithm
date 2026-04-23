T = 10
for tc in range(T):
    N = int(input())
    arr = list(map(int,input().split()))

    ans = 0
    for i in range(2,N-2):
        flag = True
        bns = 0
        for j in range(1,3):
            if arr[i] > arr[i-j] and arr[i] > arr[i+j]:
                cns = max(arr[i-j],arr[i+j])
                if cns >= bns:
                    bns = cns
            else:
                flag = False
                break
        if flag:
            ans += arr[i] - bns
        else:
            continue
    print(f'#{tc+1} {ans}')