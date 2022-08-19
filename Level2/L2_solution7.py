#더 맵게
import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)

    while scoville[0] < K and len(scoville) != 1:
        new_scoville = heapq.heappop(scoville) + (heapq.heappop(scoville) * 2)
        heapq.heappush(scoville, new_scoville)
        answer += 1
    return -1 if scoville[0] < K else answer


scoville = [1, 2, 3, 9, 10, 12]
K = 7
solution(scoville, K)