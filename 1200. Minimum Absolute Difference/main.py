from typing import List

class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:

        arr.sort()

        minimal = arr [ 1 ] - arr [ 0 ]

        for i in range ( len ( arr ) - 1):
            value =  arr [ i + 1] - arr [ i ] 
            if value < minimal:
                minimal = value

        result = []

        for i in range ( len (arr) - 1):

            if arr [ i + 1] - arr [ i ] == minimal:
                result.append ( [arr [ i ], arr [ i + 1] ])

        return result
    

s = Solution()

nums = [ 1, 2, 3, 4]

print ( s.minimumAbsDifference( nums ))


        