class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        n = sorted(nums)

        for i in range(len(n)):
            if i>0 and n[i] == n[i-1]:
                continue
            left = i + 1
            right = len(n) - 1
            target = -(n[i])
            
            
            while left<right:
                two_sum = n[left] + n[right]

                if two_sum > target:
                    right-=1
                elif two_sum < target:
                    left+=1
                else:
                    result.append([n[i], n[left], n[right]])
                    left += 1
                    right -= 1

                    while left < right and n[left] == n[left - 1]:
                        left += 1
                    while left < right and n[right] == n[right + 1]:
                        right -= 1
        return result
        