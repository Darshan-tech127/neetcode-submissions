class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        p = []
        for i in range(len(nums)):
            a = 1
            for j in range(len(nums)):
                if i==j:
                    continue
                a=a*nums[j]
            p.append(a)
        return p
