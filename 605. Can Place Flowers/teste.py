from typing import List 

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        
        occur = 0

        lenght = len ( flowerbed )

        if len ( flowerbed ) >= 2:
            if flowerbed[ 0 ] == flowerbed [ 1 ] == 0:
                flowerbed [ 0 ] = 1
                occur += 1

        for i in range ( 1, lenght - 1):

            if flowerbed [ i - 1] == flowerbed [ i ] == flowerbed [ i + 1] == 0:
                flowerbed [ i ] = 1
                occur += 1

        if lenght >= 3:
            if flowerbed [ lenght - 3 ] == 1 and flowerbed [  lenght - 2 ] == flowerbed [ lenght - 1] == 0:
                flowerbed [ lenght - 1 ] = 1
                occur += 1 
        
        if occur >= n:
            return True
        return False
    
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:

        l = len ( flowerbed )

        count = 0

        prev = 0

        for i in range ( l ):

            curr = flowerbed [ i ]
            nxt = flowerbed [ i + 1] if i + 1 < l else 0

            if prev == curr == nxt == 0:
                prev = 1
                count += 1

                if count >= n:
                    return True
            else:
                prev = curr
                
        return False