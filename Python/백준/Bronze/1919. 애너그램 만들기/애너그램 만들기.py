arr = input()
brr = input()
cnt = 0

for char in "abcdefghijklmnopqrstuvwxyz":
    count_a = arr.count(char)
    count_b = brr.count(char)
    cnt += abs(count_a - count_b)

print(cnt)