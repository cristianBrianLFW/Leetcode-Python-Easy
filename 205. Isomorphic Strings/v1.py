
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len ( s ) == len ( t ):
            tableA = dict ()
            tableB = dict ()
            for ls, lt in  zip (s, t):
                if ls not in tableA:
                    tableA[ls] = lt
                elif tableA[ls] != lt:
                    return False
                if lt not in tableB:
                    tableB[lt] = ls
                elif tableB[lt] != ls:
                    return False
        else: 
            return False
        return True


a = "baba"

b = "badc"

s = Solution ()

print ( s.isIsomorphic(a, b))
