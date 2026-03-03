import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    while len(scoville):
        a = heapq.heappop(scoville)
        if a >= K:
            return answer
        elif len(scoville) == 0:
            return -1
        else:
            b = heapq.heappop(scoville)
            heapq.heappush(scoville, a + 2 * b)
            answer += 1
    return -1
