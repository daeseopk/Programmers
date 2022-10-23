# 예상 대진표
import math

def solution(n,a,b):

    count = 0
    for i in range(int(n/2)):
        if a>1 and a%2==1:
            a += 1
        if b>1 and b%2==1:
            b += 1

        count += 1
        if b-a==1 or a-b==1 or a==b:
            return count

        a = math.ceil(a / 2)
        b = math.ceil(b / 2)


    return


solution(8,4,5)