class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!= len(t):
            return False
        h ={}
        for e in s:
            if e in h:
                h[e]+=1
            else :
                h[e]=1
        for e in t:
            if e in h and h[e]!= 0:
                h[e]-=1
            else :
                return False
        return True
