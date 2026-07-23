T = int(input())
for tc in range(1,T+1):
    N, M = input().split()
    M = int(M)
    arr = input().split()

    cnt = [0] * 10

    mydict = {
        'ZRO': 0,
        'ONE': 1,
        'TWO': 2,
        'THR': 3,
        'FOR': 4,
        'FIV': 5,
        'SIX': 6,
        'SVN': 7,
        'EGT': 8,
        'NIN': 9
    }

    rev_dict = {v: k for k,v in mydict.items()}

    for num in arr:
        count = mydict[num]
        cnt[count] += 1

    print(f'#{tc}')
    for i in range(10):
        word = rev_dict[i]
        for _ in range(cnt[i]):
            print(word, end=' ')
    print()