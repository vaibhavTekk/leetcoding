class Solution:
    def canBeEqual(self, s1: str, s2: str) -> bool:
        
        def helper(l1,l2,i):
            if l1 == l2:
                return True
            if i + 2 >= 4:
                return False
            
            l1[i],l1[i+2] = l1[i+2],l1[i]
            res1 = helper(l1,l2,i+1)
            l1[i],l1[i+2] = l1[i+2],l1[i]
            res2 = helper(l1,l2,i+1)
            
            return res1 or res2
        
        return helper(list(s1),list(s2),0)



            
                    