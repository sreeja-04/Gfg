class Solution:
    # your task is to complete this function
    # function sort the stack such that top element is max
    # funciton should return nothing
    # s is a stack
    def Sorted(self, s):
        def sortstack(s):
            if len(s) <= 1:
                return
            
            top = s.pop()
            sortstack(s)
            insele(s, top)
        
        def insele(s, ele):
            if not s or ele >= s[-1]:
                s.append(ele)
                return
            temp = s.pop()
            insele(s, ele)
            s.append(temp)
            
        return sortstack(s)
            
            
            
        