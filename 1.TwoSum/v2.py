from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        tabela = {}
        for x, num in enumerate ( nums ):
            diff = target - num
            if ( diff in tabela ):
                return tabela[diff], x
            else:
                tabela [ num ] = x

s = Solution()

L = [ 2, 7, 9]

print ( s.twoSum (L, 11))

