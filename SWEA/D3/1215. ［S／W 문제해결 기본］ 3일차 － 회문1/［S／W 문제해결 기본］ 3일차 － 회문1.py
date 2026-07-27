T = 10
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(input()) for _ in range(8)]

    def palin(word):
        if word == word[::-1]:
            return True
        else:
            return False

    cnt = 0

    for i in range(8):
        for j in range(8 - N + 1):
            temp = []
            for k in range(N):
                temp.append(arr[j + k][i])
            if palin(arr[i][j:j + N]):
                cnt += 1
            if palin(temp):
                cnt += 1
    print(f'#{tc} {cnt}')