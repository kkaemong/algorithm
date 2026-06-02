T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = list(map(int,input().split()))

    ans = []
    while arr:
        current_num = arr[0]
        for j in range(1,len(arr)):
            if current_num < arr[j]:
                current_num = arr[j]
            else:
                continue

        ans.append(arr.pop(arr.index(current_num)))

        if not arr:
            break

        current_num = arr[0]

        for x in range(1,len(arr)):
            if current_num > arr[x]:
                current_num = arr[x]
            else:
                continue

        ans.append(arr.pop(arr.index(current_num)))

    ans = ans[:10]

    print(f'#{tc}', *ans)