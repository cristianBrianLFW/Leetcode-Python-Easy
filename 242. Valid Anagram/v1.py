class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len ( s ) == len ( t ):

            tableA = {}
            tableB = {}
            
            for ls, lt in zip (s, t ):
                if ls in tableA:
                    tableA[ls] += 1
                else:
                    tableA[ls] = 1
                
                if lt in tableB:
                    tableB [ lt ] += 1
                else:
                    tableB [ lt ] = 1

            
            for key in tableA:
                if key in tableB:
                    if tableA [ key ] != tableB [ key ]:
                        return False
                else:
                    return False
            
            return True
        
        return False
