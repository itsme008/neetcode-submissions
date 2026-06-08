class Solution:
    def singleNumber(self, nums: List[int]) -> int:

        #hashmap
        count = {}

        for i in nums:
            count[i] = count.get(i, 0) +1

        for n in count:
            if count[n] == 1:
                return n