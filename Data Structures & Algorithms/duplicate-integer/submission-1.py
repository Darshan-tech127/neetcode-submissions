class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        n = nums
        s = set(nums)
        if len(n) == len(s):
            return False
        else:
            return True
