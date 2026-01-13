def solution(s):
    answer=[]
    for sen in s.split(' '):
        answer.append(sen.lower().capitalize())
    return " ".join(answer)