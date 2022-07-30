# 크레인 인형뽑기 게임
def solution(board, moves):
    board_tmp = []
    bucket = []
    trashcan=[]
    for i in range(len(board)):
        line = []
        board_tmp.append(line)

    for i in reversed(range(len(board))):
        for j in reversed(range(len(board[i]))):
            if board[j][i] != 0:
                board_tmp[i].append(board[j][i])

    for move in moves:
        if board_tmp[move-1]:
            bucket.append(board_tmp[move-1].pop())
            if len(bucket)>=2 and bucket[len(bucket)-1] == bucket[len(bucket)-2]:
                trashcan.append(bucket.pop())
                trashcan.append(bucket.pop())

    answer = len(trashcan)

    return answer