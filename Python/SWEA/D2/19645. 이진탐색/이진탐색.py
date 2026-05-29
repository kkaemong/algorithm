T = int(input())
for tc in range(1, T + 1):
    P, A, B = map(int, input().split())
    L = 1
    R = P
    ans = 0

    while True:
        target = (L+R) // 2
        ans += 1

        if target == A:
            break
        if target < A:
            L = target
        else:
            R = target

    # === 2. B의 탐색 (A랑 똑같이 복사해서 변수명만 변경) ===
    L_B = 1
    R_B = P
    ans_B = 0

    while True:
        target_B = (L_B + R_B) // 2
        ans_B += 1

        if target_B == B:
            break
        if target_B < B:
            L_B = target_B
        else:
            R_B = target_B

    # === 3. 승부 판정 ===
    if ans < ans_B:
        result = 'A'
    elif ans_B < ans:
        result = 'B'
    else:
        result = 0

    print(f'#{tc} {result}')