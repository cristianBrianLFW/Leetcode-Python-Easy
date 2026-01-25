

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        tableA = {}
        tableB = {}

        for ls, lt in zip(s, t):
            if ls in tableA and tableA[ls] != lt:
                return False
            if lt in tableB and tableB[lt] != ls:
                return False

            tableA[ls] = lt
            tableB[lt] = ls

        return True


a = "baba"

b = "badc"

s = Solution ()

print ( s.isIsomorphic(a, b))