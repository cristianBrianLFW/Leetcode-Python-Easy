from typing import List

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        table = dict ()

        for x, num in enumerate ( nums ):
            if num in table and abs ( table [ num ] - x ) <= k:
                return True
            else:
                table[ num ] = x
        return False


s = Solution ()

n = [ 1,2,3,1,2,3]

k = 2

print ( s.containsNearbyDuplicate(n, k))