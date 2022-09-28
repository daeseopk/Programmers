#JadenCase 문자열 만들기

def solution(s):
    answer = ''
    s = s.lower()
    tmp = s.split(' ')

    for i in range(len(tmp)):
        if tmp[i] == '':
            if i == len(tmp)-1:
                continue
            answer+=' '
            continue
        word_first= tmp[i][0].upper()
        word_remainder = tmp[i][1:]
        new_word = word_first+word_remainder
        if i == len(tmp)-1:
            answer += new_word
        else:
            answer += new_word+' '

    return answer
    


s="3people unfollowed me "
print(solution(s)+"1")
