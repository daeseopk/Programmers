# 키패드 누르기
def solution(numbers, hand):
    answer=''
    current_L = [0,3]
    current_R = [2,3]
    coordinate=[[0,0],[1,0],[2,0],
                [0,1],[1,1],[2,1],
                [0,2],[1,2],[2,2],
                [1,3]]
    for num in numbers:
        if num==1 or num==4 or num==7:
            answer=answer+"L"
            current_L = coordinate[num-1]
        elif num == 3 or num==6 or num==9:
            answer=answer+"R"
            current_R = coordinate[num-1]
        else:
            gap_left = abs(coordinate[num-1][0]-current_L[0])+abs(coordinate[num-1][1]-current_L[1])
            gap_right = abs(coordinate[num-1][0]-current_R[0])+abs(coordinate[num-1][1]-current_R[1])
            if gap_right==gap_left:
                if hand == "right":
                    answer=answer+"R"
                    current_R = coordinate[num - 1]
                else:
                    answer=answer+"L"
                    current_L = coordinate[num - 1]
            elif gap_right>gap_left:
                answer=answer+"L"
                current_L=coordinate[num-1]
            else:
                answer=answer+"R"
                current_R = coordinate[num - 1]
    return answer