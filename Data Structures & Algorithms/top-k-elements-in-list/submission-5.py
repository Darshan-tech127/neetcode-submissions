class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)
        for num in nums:
            freq[num]+=1
        max_k = heapq.nlargest(k,freq.items(),key=lambda x:x[1])
        return [num for num,count in max_k]
        


