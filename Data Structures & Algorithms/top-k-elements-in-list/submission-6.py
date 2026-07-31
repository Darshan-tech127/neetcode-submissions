class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        def_dt = defaultdict(int)
        for num in nums:
            def_dt[num]+=1
        max_k = heapq.nlargest(k,def_dt.items(),lambda x:x[1])
        return [num for num,count in max_k]