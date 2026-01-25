from typing import List

class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:

        g.sort( reverse=True)

        s.sort()

        happyChild = 0

        for hungry in g:
            tam = len ( s )
            if tam > 0:
                if hungry <= s [ tam - 1]:
                    happyChild += 1
                    s.pop()
            else:
                return happyChild
        return happyChild
    


g = [1, 2, 3, 4]

s = [ 1, 1, 5]

teste = Solution()


print ( teste.findContentChildren(g, s))


