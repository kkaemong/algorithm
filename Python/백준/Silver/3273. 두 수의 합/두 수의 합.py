N = int(input())
arr = sorted(list(map(int, input().split())))
X = int(input())

cnt = 0
left = 0
right = N - 1

while left < right:
    current_sum = arr[left] + arr[right]

    if current_sum == X:
        cnt += 1
        left += 1
        right -= 1
    elif current_sum < X:
        left += 1
    else:
        right -= 1

print(cnt)