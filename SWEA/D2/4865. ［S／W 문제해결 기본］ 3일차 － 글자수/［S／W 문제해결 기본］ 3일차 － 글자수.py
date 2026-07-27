T = int(input())
for tc in range(1, T + 1):
    arr = list(input())
    brr = list(input())

    cnt = []

    for i in arr:
        if i in brr:
             cnt.append(brr.count(i))
    print(f'#{tc} {max(cnt)}')