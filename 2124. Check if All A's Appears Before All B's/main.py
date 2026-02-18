class Solution:
    def checkString(self, s: str) -> bool:

        l = len ( s )

        if l > 1 :
            i, prev = 0, s [ 0 ]
            while i < l:
                if s [ i ] == 'a' and prev == 'b':
                    return False
                prev = s [ i ]
                i += 1
        return True