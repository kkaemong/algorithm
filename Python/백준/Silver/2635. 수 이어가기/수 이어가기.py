N = int(input())

max_len = 0
best_seq = []

for second in range(N, -1, -1):
    seq = [N, second]

    while True:
        next_num = seq[-2] - seq[-1]
        if next_num < 0:
            break
        seq.append(next_num)

    if len(seq) > max_len:
        max_len = len(seq)
        best_seq = seq

print(max_len)
print(*best_seq)