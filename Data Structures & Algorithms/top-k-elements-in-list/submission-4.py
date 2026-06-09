class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        l=[[] for i in range(len(nums)+1)]
        hashmap = {}
        result = []

        for i in nums:
            hashmap[i] = hashmap.get(i, 0)+1

        for key, value in hashmap.items():
            l[value].append(key)

        for n in range(len(l)-1, 0, -1):
            for m in l[n]:
                result.append(m)
                if len(result) == k:
                    return result