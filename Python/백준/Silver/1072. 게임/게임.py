X,Y = map(int, input().split())

current_Z = (Y * 100) // X

if current_Z >= 99:
    print(-1)
else:
    answer = -1
    low = 1
    high = 1000000000

    while low <= high:
        mid = (low + high) // 2

        new_Z = ((Y + mid) * 100) // (X + mid)

        if new_Z > current_Z:
            answer = mid
            high = mid - 1
        else:
            low = mid + 1

    print(answer)