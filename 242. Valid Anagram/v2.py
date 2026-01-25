class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len ( s ) == len ( t ):
            
            tA = {}
            tB = {}

            for c in s:
                tA [ c ] = tA.get(c, 0) + 1

            for c in t:
                tB [ c ] = tB.get(c, 0 ) + 1
            
            return tA == tB
        
        return False