class Solution:

    def encode(self, strs: List[str]) -> str:
        en = ""
        for s in strs:
            en += str(len(s))+"#"+s
        return en

    def decode(self, s: str) -> List[str]:
        dc = []
        i = 0
        while i<len(s):
            j = i
            while s[j]!="#":
                j+=1
            length = int(s[i:j])
            read = s[j+1:j+1+length]
            dc.append(read)
            i = j+1+length
        return dc
                