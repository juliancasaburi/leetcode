class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for i in range(len(stones)):
            stones[i] *= -1
        heapq.heapify(stones)

        while stones:
            s1 = -heappop(stones)

            if not stones:
                return s1

            s2 = -heappop(stones)

            if s1 > s2:
                heappush(stones, s2-s1)
        
        return 0
        