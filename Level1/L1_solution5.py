# 없는 숫자 더하기
def solution(numbers):
    originNum = [1,2,3,4,5,6,7,8,9,0]
    noneExistNum=0
    for num in originNum:
        if not num in numbers:
            noneExistNum = noneExistNum + num
    
    answer=noneExistNum
    return answer