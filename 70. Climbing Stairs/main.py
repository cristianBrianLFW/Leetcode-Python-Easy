class Solution:
    def climbStairs(self, n: int) -> int:

        d = [ 1, 2]

        i = 2

        while i < n:
    
            if i % 2 == 0:
                d [ 0 ] += d [ 1 ]
            else:
                d [ 1 ] += d [ 0 ]
            i += 1

   
        return d [ 0 ] if ( n + 1 )% 2 == 0 else d [ 1 ]
    

s = Solution ()

for i in range ( 10 ):

    a = int (input (f"Digite um numero {i + 1} --> ") )

    print ( f"O valor eh {s.climbStairs( a )}")

