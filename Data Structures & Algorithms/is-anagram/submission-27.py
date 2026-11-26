class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
           return False
        h={s[i] : 0  for i in range(len(s))}
        for e in s:
            h[e]+=1
        for e in t:
            if e in s and h[e]!=0:
                h[e]-=1
            else :
                return False
        return True