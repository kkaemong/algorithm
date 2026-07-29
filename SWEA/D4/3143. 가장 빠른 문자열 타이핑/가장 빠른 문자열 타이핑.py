T = int(input())
for tc in range(1, T + 1):
    a, b = input().split()

    cnt = 0
    ans = 0
    a_len = len(a)
    b_len = len(b)

    while a_len > cnt:
        if a[cnt:cnt+b_len] == b:
            cnt += b_len
            ans += 1
        else:
            cnt += 1
            ans += 1

    print(f'#{tc} {ans}')