class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def_dt = defaultdict(list)
        for s in strs:
            count = [0]*26
            for ch in s:
                count[ord(ch)-ord('a')]+=1
            def_dt[tuple(count)].append(s)
        return list(def_dt.values())
