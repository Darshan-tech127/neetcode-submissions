class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        seq_st = 0
        longest = 0
        for num in nums:
            if num-1 in nums:
                continue
            seq_st = num
            length = 1
            while (num+1) in nums:
                length+=1
                num+=1
            if longest<length:
                longest = length
        return longest
            