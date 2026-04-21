T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = list(input().rstrip())
    ans = [0 * i for i in range(10)]

    for i in arr:
        a = int(i)
        ans[a] += 1

    max_count = 0  # 가장 많은 장수
    best_num = 0  # 가장 많은 카드의 숫자

    for num in range(10):
        if ans[num] >= max_count:
            max_count = ans[num]
            best_num = num

    print(f'#{tc} {best_num} {max_count}')