

class Solution:
    def hasAlternatingBits(self, n: int) -> bool:

        def toBinary ( num ):

            if num // 2 == 0:
                return num % 2
            return toBinary ( num // 2 ) * 10 + num

        
        bNumber = toBinary ( n )

        print ( bNumber )

        if bNumber >= 10:

            inicial = bNumber % 10

            bNumber //= 10

            while bNumber > 0:


                final = bNumber % 10

                print ( inicial, final )
                if inicial == final:
                    return False

                inicial = final

                bNumber //= 10

        elif bNumber == 1:
            return False
            

        return True        
    



s = Solution()

n = int ( input (": "))

print ( s.hasAlternatingBits(n))
    


