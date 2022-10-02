def solution(s):
    convert_count = 0
    zero_count = 0

    def convert(num, zero_count, convert_count):
        tmp_s = ''
        
        for i in num:
            if i == '1':
                tmp_s+=i
            else:
                zero_count+=1

        convert_count+=1
        return bin(len(tmp_s))[2:], zero_count, convert_count

    while s != '1':
        s, zero_count, convert_count = convert(s,zero_count, convert_count)

    return [convert_count, zero_count]




s="110010101001"
solution(s)