numbers = [int(input()) for _ in range(3)]

result = numbers[0] * numbers[1] * numbers[2]
result_srt = str(result)

arr = [0]* 10

for char in result_srt:
    num = int(char)
    arr[num] += 1

for i in arr:
    print(i)