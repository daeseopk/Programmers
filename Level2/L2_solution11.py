#최대값과 최솟값
def solution(s):
    answer=''
    num_array = s.split(' ')
    num_array = list(map(int,num_array))
    
    answer += str(min(num_array))
    answer += ' '+str(max(num_array))
    

    return answer



s = '-1 -2 -3 -4'
print(solution(s))