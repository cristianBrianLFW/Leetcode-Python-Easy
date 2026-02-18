
from typing import List

class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        tam = len ( nums )
        menor = nums [ tam - 1]
        i, j = 0, 0

        while i < len ( nums ):

            if i - j + 1 == k:
                diff = nums [ i ] - nums [ j ]
                if diff < menor:
                    menor = diff
                j = i
            
            i += 1
        
        return menor
