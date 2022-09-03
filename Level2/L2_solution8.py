# 짝지어 제거하기
def solution(s):
    arr = []
    for i in s:
        if arr:
            if arr[len(arr)-1]==i:
                arr.pop()
            else:
                arr.append(i)
        else:
            arr.append(i)

    if len(arr)>0:
        return 0
    else:
        return 1



s= 'baabaa'
solution(s)