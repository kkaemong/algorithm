T = int(input())
for tc in range(1, T + 1):
    arr = input()
    brr = input()

    N = len(arr)
    M = len(brr)

    cnt = 0
    for i in range(M):
        if arr == brr[i:i+N]:
            cnt = 1
            print(f'#{tc} {cnt}')
            break
    else:
        print(f'#{tc} {cnt}')