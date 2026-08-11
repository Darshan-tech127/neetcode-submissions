class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1] * n

        prefix = 1
        for i in range(1,n):
            prefix *= nums[i-1]
            res[i] = prefix

        suffix = 1
        for i in range(n - 2, -1, -1):
            suffix *= nums[i+1]
            res[i] *= suffix

        return res