# [1차] 뉴스 클러스터링

import math

def solution(str1, str2):
    tmp = []
    str1_div = []
    str2_div = []
    intersection = []
    for i in range(len(str1)-1):
        tmp.append(str1[i])
        tmp.append(str1[i+1])
        if(len(list(filter(str.isalpha, tmp)))==2):
            str1_div.append(''.join(list(filter(str.isalpha, tmp))).upper())
        tmp.clear();

    for i in range(len(str2)-1):
        tmp.append(str2[i])
        tmp.append(str2[i+1])
        if (len(list(filter(str.isalpha, tmp))) == 2):
            str2_div.append(''.join(list(filter(str.isalpha, tmp))).upper())
        tmp.clear();

    j = 0
    while str1_div:
        if j == len(str1_div):
            break
        if str1_div[j] in str2_div:
            duplicate = str1_div[j]
            intersection.append(duplicate)
            str1_div.remove(duplicate)
            str2_div.remove(duplicate)
            j = 0
            continue
        j = j + 1

    intersection = len(intersection)
    union = len(str1_div)+len(str2_div) + intersection

    if union==0:
        return 65536
    return math.trunc(intersection/union*65536)