N, K = map(int, input().split())
arr = [int(input()) for _ in range(N)]

result = 0
arr.reverse()
for i in range(N):
    result += K // arr[i]
    K %= arr[i]

print(result)
