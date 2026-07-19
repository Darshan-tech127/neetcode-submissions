class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i,num in enumerate(nums):
            conjugate = target-num
            if conjugate in seen:
                return [seen[conjugate],i]
            else:
                seen[num] = i