T = 10
for tc in range(1, T + 1):
    N, arr =input().split()
    N = int(N)
    arr = list(arr)

    i = 0
    while i != len(arr) -1 :
        if arr[i] == arr[i+1]:
            arr.pop(i)
            arr.pop(i)
            i = 0
        else:
            i += 1
    print(f"#{tc} {''.join(arr)}")