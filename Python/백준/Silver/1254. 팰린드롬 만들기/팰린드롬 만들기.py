s = input().strip()
n = len(s)

for i in range(n):
    left = i
    right = n - 1
    ok = True

    while left < right:
        if s[left] != s[right]:
            ok = False
            break
        left += 1
        right -= 1

    if ok:
        print(n + i)
        break
