class Solution:
    def longestPalindrome(self, s: str) -> int:
        table = {}

        for l in s:
            if l not in table:
                table [ l ] = 1
            else:
                table [ l ] += 1
        
        output = 0

        diff = 0

        for key in table:
            if table [ key ] % 2 == 1:
                diff += 1
            output += table [ key ]

        if diff == 0:
            return output
        
        return output - diff + 1
    

teste = Solution()

print ( teste.longestPalindrome("aeeebccccdd"))
            
