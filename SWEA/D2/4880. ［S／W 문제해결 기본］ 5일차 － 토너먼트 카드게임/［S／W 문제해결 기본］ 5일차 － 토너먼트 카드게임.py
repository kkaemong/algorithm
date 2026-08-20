T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    cards = [0] + list(map(int, input().split()))

    def battle(a, b):
        ca = cards[a]
        cb = cards[b]
        if ca == cb:
            return min(a, b)
        if (ca == 1 and cb == 3) or (ca == 2 and cb == 1) or (ca == 3 and cb == 2):
            return a
        else:
            return b

    def find_winner(i, j):
        if i == j:
            return i
        mid = (i + j) // 2
        left_winner = find_winner(i, mid)
        right_winner = find_winner(mid + 1, j)
        return battle(left_winner, right_winner)

    winner = find_winner(1, N)
    print(f'#{tc} {winner}')