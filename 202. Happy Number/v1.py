class Solution:
    def isHappy(self, n: int) -> bool:
        num = n

        table = set ()

        while num not in table:
            table.add (num)
            temp = num
            num = 0
            while ( temp != 0 ):
                num += ( temp % 10 )**2
                temp //= 10
            if num == 1:
                return True
        
        return False
    

s = Solution ()

print (s.isHappy( 100))
