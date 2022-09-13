# 정수 삼각형

def solution(triangle):
    dp = [triangle[0]]
    for i in range(len(triangle)):
        if i == 0:
            continue
        lst = []
        rowlst = triangle[i]
        rowlength = len(rowlst)-1

        for k, value in enumerate(rowlst):
            if k == 0:
                lst.append(dp[i-1][0] + value)
            elif k == rowlength:
                lst.append(dp[i-1][rowlength-1] + value)
            else:
                lst.append(max(dp[i-1][k-1],dp[i-1][k]) + value)

        dp.append(lst)

    return max(dp[len(dp)-1])



solution(triangle=[[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]])