from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        table = dict ()
        for num in nums:
            if num in table:
                table[num] += 1
            else:
                table[ num ] = 1
        maior = 0
        result = 0
        for key in table:
            if maior < table[key]:
                result = key
                maior = table[key]
        return result
    

s = Solution()

a = [1, 2, 2, 2]

s.majorityElement(a)
        