# 최고의 집합

def solution(n, s):
    answer = []
    integer = s // n # 정수 부분
    remainder = s % n # 나머지

    if integer == 0:
        return [-1]
    for _ in range(n-remainder):
        answer.append(integer)
    for _ in range(remainder):
        answer.append(integer + 1)




    print(answer)
    return answer


solution(6, 13)