# K번째수
def solution(array, commands):
    answer = []
    array_tmp = []
    for command in commands:
        array_tmp = array[command[0]-1:command[1]]
        array_tmp.sort()
        answer.append(array_tmp[command[2]-1])
        array_tmp.clear()

    return answer