T = int(input())
for tc in range(1, T + 1):
    arr = input()
    brr = input()

    if arr in brr:
        print(f'#{tc} 1')
    else:
        print(f'#{tc} 0')
    