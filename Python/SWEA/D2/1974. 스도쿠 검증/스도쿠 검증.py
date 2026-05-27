T = int(input())
for tc in range(1, T + 1):
    arr = [list(map(int, input().split())) for _ in range(9)]

    is_sudoku = 1  # 일단 올바른 스도쿠(1)라고 가정

    for i in range(9):
        for j in range(9):
            num = arr[i][j]  # 현재 검사할 기준 숫자

            # 1. 가로 세로 검사 (인덱스 초과 없이 0~8까지 확인)
            for x in range(9):
                # 자기 자신(x == j 또는 x == i)이 아닌데 똑같은 숫자가 있다면 중복!
                if x != j and arr[i][x] == num:  # 가로 줄 검사
                    is_sudoku = 0
                    break
                if x != i and arr[x][j] == num:  # 세로 줄 검사
                    is_sudoku = 0
                    break

            if is_sudoku == 0: break

            # 2. 내가 속한 3x3 박스 검사
            # 내 좌표 (i, j)가 속한 박스의 시작점 구하기
            start_r = (i // 3) * 3
            start_c = (j // 3) * 3

            for y in range(start_r, start_r + 3):
                for z in range(start_c, start_c + 3):
                    # 자기 자신 좌표는 건너뛰기
                    if y == i and z == j:
                        continue
                    # 나랑 같은 숫자가 박스 안에 또 있다면 중복!
                    if arr[y][z] == num:
                        is_sudoku = 0
                        break
                if is_sudoku == 0: break

            if is_sudoku == 0: break
        if is_sudoku == 0: break

    print(f'#{tc} {is_sudoku}')