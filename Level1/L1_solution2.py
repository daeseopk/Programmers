# 숫자 문자열과 영단어
def solution(s):
    numbers={"zero":"0",
             "one":"1",
             "two":"2",
             "three":"3",
             "four":"4",
             "five":"5",
             "six":"6",
             "seven":"7",
             "eight":"8",
             "nine":"9"}
    for num in numbers:
        if num in s:
            s = s.replace(num, numbers[num])
    
    answer=int(s)
    return answer