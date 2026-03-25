word = input()
arr = [0] * 26
alpa = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

for i in range(len(word)):
    char = word[i]
    if char in alpa:
        # 단어의 글자가 alpa 리스트의 몇 번째에 있는지 찾아서
        idx = alpa.index(char)
        # 그 위치(idx)의 숫자를 1 증가시킨다!
        arr[idx] += 1

print(*arr)