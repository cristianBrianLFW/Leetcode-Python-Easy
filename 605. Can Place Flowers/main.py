from typing import List 

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:

        # a ideia geral é percorrer o vetor por completo

        # se o elemento for 1 tem que contar a distância até o pŕoximo 1 

        # pega essa distãncia e divide por 3, que é o espaço mínimo de uma flor cercada por outras

        # soma nas ocorrencias

        i = 0

        ocurr = 0

        n = len ( flowerbed )

        if n > 2:
            if flowerbed [ 0 ] == 0 and flowerbed [ 1 ] == 0:
                ocurr += 1

        search = False

        first, last = 0, 0

        while i < len ( flowerbed ):

            if search == True:

                print ( f"first: {first} e last { last} ")

                last = i

                ocurr += ( last - first - 1) // 3

            else:

                if flowerbed [ i ] == 1:
                    search = True
                    first = i

            i += 1

        if ocurr >= n:
            return True
        else:
            return False
        


s = Solution()

flowers = [1, 0, 0, 0, 1]

print (s.canPlaceFlowers(flowers, 1))
            
