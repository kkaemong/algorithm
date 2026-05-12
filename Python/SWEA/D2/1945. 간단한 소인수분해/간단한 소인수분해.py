T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    # 2 3 5 7 11

    arr = [0] * 5

    while N != 1:
        if N % 2 == 0:
            N //= 2
            arr[0] += 1
        elif N % 3 == 0:
            N //= 3
            arr[1] += 1
        elif N % 5 == 0:
            N //= 5
            arr[2] += 1
        elif N % 7 == 0:
            N //= 7
            arr[3] += 1
        elif N % 11 == 0:
            N //= 11
            arr[4] += 1

    print(f'#{tc}', *arr)