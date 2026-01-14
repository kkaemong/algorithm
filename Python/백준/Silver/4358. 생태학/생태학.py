import sys
trees = []

for line in sys.stdin:
    trees.append(line.strip())

trees.sort()

total = len(trees)

i = 0
while i < total:
    cnt = 1
    while i + 1 < total and trees[i] == trees[i + 1]:
        cnt += 1
        i += 1
    ratio = cnt / total * 100
    print(f"{trees[i]} {ratio:.4f}")
    i += 1
