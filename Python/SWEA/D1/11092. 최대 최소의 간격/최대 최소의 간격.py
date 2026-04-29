T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))

    max_num = max(arr)
    min_num = arr.index(min(arr))
    max_idx = len(arr) - 1 - arr[::-1].index(max_num)

    ans = abs(max_idx - min_num)

    print(f'#{tc} {ans}')