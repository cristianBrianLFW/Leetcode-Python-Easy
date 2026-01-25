class Solution:
    def longestPalindrome(self, s: str) -> int:
        table = {}

        for l in s:
            if l not in table:
                table [ l ] = 1
            else:
                table [ l ] += 1

        




s = Solution()

print ( s.longestPalindrome("abbbbccccddd"))

        