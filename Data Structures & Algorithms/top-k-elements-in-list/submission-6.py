class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        count_map = {}

        frq_list = [[] for i in range(len(nums)+1)]

        result = []

        for i in nums:
            count_map[i] = count_map.get(i, 0)+1

        for value, index in count_map.items():
            frq_list[index].append(value)

        for values in range(len(frq_list)-1, 0, -1):
            for value in frq_list[values]:
                result.append(value)
                if len(result) == k:
                    return result

       