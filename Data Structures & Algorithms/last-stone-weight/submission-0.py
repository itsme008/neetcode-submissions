class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        if len(stones) < 0:
            return 0
        if len(stones) == 1:
            return stones[0]

        while len(stones) > 1:
            stones.sort(reverse=True)
    
            if stones[0] > stones[1]:
                diff = stones[0] - stones[1]
                stones.pop(0)
                stones.pop(0)
                stones.append(diff)

            elif stones[0] == stones[1]:
                stones.pop(0)
                stones.pop(0)
                
        return stones[0] if stones else 0