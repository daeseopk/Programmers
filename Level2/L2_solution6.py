def solution(s):
    tmp = []
    for i in s:
        if i=="(":
            tmp.append(i)
        else:
            if len(tmp)>=1:
                tmp.pop()
            elif len(tmp)==0:
                return False
    if len(tmp) >= 1:
        return False
    else:
        return True

s = ")()("
solution(s)