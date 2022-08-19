# 최소 직사각형
def solution(sizes):
    big = []
    small = []

    for i in sizes:
        big.append(max(i))
        small.append(min(i))

    return max(big) * max(small)

sizes = [[60, 50], [30, 70], [60, 30], [80, 40]]
solution(sizes)
