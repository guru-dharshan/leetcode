class Solution:
    def reverse(self, x: int) -> int:
        strg = str(x)
        if x >= 0 :
            revst = strg[::-1]
        else:
            temp = strg[1:] 
            temp2 = temp[::-1] 
            revst = "-" + temp2
        if int(revst) >= 2**31-1 or int(revst) <= -2**31:
            return 0
        return int(revst)
        