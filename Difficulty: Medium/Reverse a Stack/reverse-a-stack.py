#User function Template for python3

from typing import List

class Solution:
    def reverse(self,St): 
        #code here
        
        def insert_bottom(St, ele):
            if not St:
                St.append(ele)
                return
            
            temp = St.pop()
            insert_bottom(St, ele)
            St.append(temp)
        
        def rev(St):
            if not St:
                return
            top = St.pop()
            rev(St)
            insert_bottom(St, top)
        
        rev(St)