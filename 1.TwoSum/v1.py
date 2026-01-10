from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        tabela = {}
        for x, elem in enumerate ( nums ):
            tabela[elem] = x
        
        for x, num in enumerate ( nums ):
            if ( target - num in tabela and tabela [ target - num ] != x):
                return x, tabela [ target - num ]
            
        return; 

s = Solution()

L = [ 2, 7, 9]

print ( s.twoSum (L, 11))

   