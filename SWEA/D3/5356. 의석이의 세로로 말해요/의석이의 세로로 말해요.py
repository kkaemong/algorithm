T = int(input())
for tc in range(1, T + 1):
    arr = [list(input()) for _ in range(5)]
    max_len = max(len(row) for row in arr)

    ans = ''

    for i in range(max_len):
        for j in range(5):  # 행: 5줄 고정
            k = len(arr[j])
            if i < k:  # 그 줄에 i번째 글자가 있는지 체크
                ans += arr[j][i]

    print(f'#{tc} {ans}')