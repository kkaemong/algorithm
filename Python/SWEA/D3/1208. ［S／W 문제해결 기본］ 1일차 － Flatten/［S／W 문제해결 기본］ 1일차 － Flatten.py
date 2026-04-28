for tc in range(10):
    dump = int(input())
    arr = list(map(int, input().split()))

    for _ in range(dump):
        # 1. 매번 최댓값과 최솟값의 위치를 찾음
        max_idx = arr.index(max(arr))
        min_idx = arr.index(min(arr))

        # 2. 평탄화 완료 조건 체크 (중요!)
        if arr[max_idx] - arr[min_idx] <= 1:
            break

        # 3. 덤프 수행
        arr[max_idx] -= 1
        arr[min_idx] += 1

    # 4. 마지막으로 다시 계산
    ans = max(arr) - min(arr)
    print(f'#{tc + 1} {ans}')