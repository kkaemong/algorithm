import sys

# 1. 입력 받기
N, M = map(int, sys.stdin.readline().split())
arr = [list(map(int, sys.stdin.readline().strip())) for _ in range(N)]
brr = [list(map(int, sys.stdin.readline().strip())) for _ in range(N)]

cnt = 0

# 2. 3x3 뒤집기 수행 (범위는 N-2, M-2까지)
# i, j는 3x3 영역의 왼쪽 위 꼭짓점 좌표입니다.
for i in range(N - 2):
    for j in range(M - 2):
        # 만약 현재 위치의 값이 목표값과 다르다면?
        if arr[i][j] != brr[i][j]:
            cnt += 1
            # 여기서 바로 3x3 영역을 뒤집습니다.
            for x in range(i, i + 3):
                for y in range(j, j + 3):
                    # 1에서 빼주면 0은 1로, 1은 0으로 바뀝니다.
                    arr[x][y] = 1 - arr[x][y]

# 3. 마지막에 두 행렬이 완전히 같은지 확인
is_same = True
for i in range(N):
    for j in range(M):
        if arr[i][j] != brr[i][j]:
            is_same = False
            break
    if not is_same:
        break

# 4. 결과 출력
if is_same:
    print(cnt)
else:
    print(-1)