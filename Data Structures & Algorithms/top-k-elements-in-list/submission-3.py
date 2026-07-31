class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)
        for num in nums:
            freq[num]+=1
        bucket = [[] for _ in range(len(nums)+1)]
        for n,f in freq.items():
            bucket[f].append(n)
        max_k = []
        for i in bucket:
            if i!=[]:
                max_k.append(i)
        k_elements =  [k for sublist in max_k for k in sublist]
        return k_elements[:-k-1:-1]

