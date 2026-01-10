class Solution:
    def romanToInt(self, s: str) -> int:
        tabela = {
            "I": 1, "V": 5, "X": 10, "L": 50, 
            "C" : 100, "D" : 500, "M" : 1000
        }

        tam = ( len ( s )) - 1

        ultimo = 0

        total = 0

        for i in range ( tam, -1, -1):
            if ( tabela [ s [ i ] ] >= ultimo ):
                total += tabela [ s [ i] ]
            else:
                total -= tabela [ s [ i ] ]
            ultimo = tabela [ s [ i ] ]
        
        return total
    

s = Solution()

a = input ("Digite o número em romano ( Letras Maiusculas ) --> ")

print (s.romanToInt(a))